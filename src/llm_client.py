"""
LLM client module for interacting with language models.
Uses litellm to support various LLM providers.
"""

import time
import asyncio
import logging
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Union
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from litellm import (
    completion,
    acompletion,
    RateLimitError,
    ServiceUnavailableError,
    ModelResponse,
    InvalidRequestError,
    AuthenticationError,
    ContextWindowExceededError,
)

logger = logging.getLogger("LLMChatIndexer")


@dataclass
class LLMStats:
    """Statistics for LLM API usage"""

    request_count: int = 0
    error_count: int = 0
    total_tokens: int = 0
    last_request_time: float = 0.0


class LLMClientError(Exception):
    """Base exception for LLM client errors"""

    pass


class ProviderValidationError(LLMClientError):
    """Raised when provider validation fails"""

    pass


class LLMClient:
    """Client for interacting with LLMs via litellm."""

    # Known provider prefixes for validation
    SUPPORTED_PROVIDERS = {"gemini", "openai", "anthropic", "groq"}

    def __init__(
        self, provider: str, max_retries: int = 3, rate_limit_delay: float = 1.0, max_context_length: int = 15000
    ):
        """
        Initialize LLM client with specified provider.

        Args:
            provider: LLM provider identifier (e.g., 'gemini/gemini-2.0-flash')
            max_retries: Maximum number of retry attempts
            rate_limit_delay: Delay in seconds between API calls
            max_context_length: Maximum context length for the model

        Raises:
            ProviderValidationError: If provider string is invalid
        """
        self._validate_provider(provider)
        self.provider = provider
        self.max_retries = max_retries
        self.rate_limit_delay = rate_limit_delay
        self.max_context_length = max_context_length
        self.stats = LLMStats()

    @classmethod
    def _validate_provider(cls, provider: str) -> None:
        """
        Validate provider string format and supported providers.

        Args:
            provider: Provider string to validate

        Raises:
            ProviderValidationError: If validation fails
        """
        try:
            provider_name = provider.split("/")[0].lower()
            if provider_name not in cls.SUPPORTED_PROVIDERS:
                raise ProviderValidationError(
                    f"Unsupported provider: {provider_name}. Must be one of: {', '.join(cls.SUPPORTED_PROVIDERS)}"
                )
        except (AttributeError, IndexError):
            raise ProviderValidationError("Provider must be in format: 'provider/model'")

    def _handle_rate_limit(self) -> None:
        """
        Implement basic rate limiting between requests.
        Updates stats and enforces delay between requests.
        """
        current_time = time.time()
        time_since_last_request = current_time - self.stats.last_request_time

        if time_since_last_request < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last_request
            logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)

        self.stats.last_request_time = time.time()
        self.stats.request_count += 1

    def _truncate_text(self, text: str) -> str:
        """
        Truncate text to maximum context length.

        Args:
            text: Text to truncate

        Returns:
            Truncated text with ellipsis if needed
        """
        if len(text) > self.max_context_length:
            truncated = f"{text[: self.max_context_length]}..."
            logger.info(f"Text truncated from {len(text)} to {self.max_context_length} characters")
            return truncated
        return text

    def _update_error_stats(self, error: Exception) -> None:
        """
        Update error statistics and log error details.

        Args:
            error: Exception that occurred
        """
        self.stats.error_count += 1
        logger.error(f"LLM API error ({type(error).__name__}): {str(error)}")

    @retry(
        stop=stop_after_attempt(lambda self: self.max_retries),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((RateLimitError, ServiceUnavailableError)),
        reraise=True,
    )
    def _make_llm_request(self, messages: List[Dict[str, str]]) -> Optional[ModelResponse]:
        """
        Make a request to the LLM with retry logic.

        Args:
            messages: List of message objects

        Returns:
            ModelResponse or None if request failed
        """
        self._handle_rate_limit()

        try:
            response = completion(model=self.provider, messages=messages)
            if response and hasattr(response, "usage"):
                self.stats.total_tokens += response.usage.total_tokens
            return response

        except (RateLimitError, ServiceUnavailableError) as e:
            self._update_error_stats(e)
            raise  # Will be caught by retry decorator

        except ContextWindowExceededError as e:
            self._update_error_stats(e)
            logger.debug(f"Message length: {sum(len(m.get('content', '')) for m in messages)}")
            return None

        except (InvalidRequestError, AuthenticationError) as e:
            self._update_error_stats(e)
            logger.debug(f"Request messages: {messages}")
            return None

        except Exception as e:
            self._update_error_stats(e)
            logger.error(f"Unexpected error: {str(e)}")
            return None

    def get_stats(self) -> Dict[str, Any]:
        """
        Get current usage statistics.

        Returns:
            Dictionary containing usage statistics
        """
        return {
            "requests": self.stats.request_count,
            "errors": self.stats.error_count,
            "total_tokens": self.stats.total_tokens,
            "provider": self.provider,
        }

    async def _make_llm_request_async(self, messages: List[Dict[str, str]]) -> Optional[ModelResponse]:
        """
        Make an async request to the LLM.

        Args:
            messages: List of message objects

        Returns:
            ModelResponse or None if request failed
        """
        self._handle_rate_limit()

        try:
            response = await acompletion(model=self.provider, messages=messages)
            if response and hasattr(response, "usage"):
                self.stats.total_tokens += response.usage.total_tokens
            return response

        except (RateLimitError, ServiceUnavailableError) as e:
            self._update_error_stats(e)
            await asyncio.sleep(self.rate_limit_delay)
            return None

        except Exception as e:
            self._update_error_stats(e)
            logger.error(f"Async request error: {str(e)}")
            return None

    def extract_topics(self, messages: List[Dict[str, str]], max_topics: int = 5) -> List[str]:
        """
        Extract topics from messages using LLM.

        Args:
            messages: List of chat messages
            max_topics: Maximum number of topics to extract

        Returns:
            List of extracted topics
        """
        prompt = self._create_topic_extraction_prompt(messages, max_topics)
        response = self._make_llm_request([{"role": "user", "content": prompt}])

        if not response:
            logger.warning("Topic extraction failed, returning empty list")
            return []

        return self._parse_topics_response(response.choices[0].message.content)

    async def extract_topics_async(self, messages: List[Dict[str, str]], max_topics: int = 5) -> List[str]:
        """
        Extract topics from messages using LLM asynchronously.

        Args:
            messages: List of chat messages
            max_topics: Maximum number of topics to extract

        Returns:
            List of extracted topics
        """
        prompt = self._create_topic_extraction_prompt(messages, max_topics)
        response = await self._make_llm_request_async([{"role": "user", "content": prompt}])

        if not response:
            logger.warning("Async topic extraction failed, returning empty list")
            return []

        return self._parse_topics_response(response.choices[0].message.content)

    def summarize(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a summary of the chat messages.

        Args:
            messages: List of chat messages

        Returns:
            Generated summary string
        """
        prompt = self._create_summary_prompt(messages)
        response = self._make_llm_request([{"role": "user", "content": prompt}])

        if not response:
            logger.warning("Summarization failed, returning empty string")
            return ""

        return response.choices[0].message.content.strip()

    async def summarize_async(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a summary of the chat messages asynchronously.

        Args:
            messages: List of chat messages

        Returns:
            Generated summary string
        """
        prompt = self._create_summary_prompt(messages)
        response = await self._make_llm_request_async([{"role": "user", "content": prompt}])

        if not response:
            logger.warning("Async summarization failed, returning empty string")
            return ""

        return response.choices[0].message.content.strip()

    def _create_topic_extraction_prompt(self, messages: List[Dict[str, str]], max_topics: int) -> str:
        """
        Create prompt for topic extraction.

        Args:
            messages: List of chat messages
            max_topics: Maximum number of topics to extract

        Returns:
            Formatted prompt string
        """
        conversation = self._format_messages_for_prompt(messages)
        return (
            f"Extract up to {max_topics} main topics from this conversation. "
            f"Return them as a comma-separated list:\n\n{conversation}"
        )

    def _create_summary_prompt(self, messages: List[Dict[str, str]]) -> str:
        """
        Create prompt for summarization.

        Args:
            messages: List of chat messages

        Returns:
            Formatted prompt string
        """
        conversation = self._format_messages_for_prompt(messages)
        return (
            "Provide a concise summary of this conversation, "
            "focusing on the main points and conclusions:\n\n"
            f"{conversation}"
        )

    def _format_messages_for_prompt(self, messages: List[Union[Dict[str, str], str]]) -> str:
        """
        Format messages for inclusion in prompts.

        Args:
            messages: List of chat messages (can be dictionaries or strings)

        Returns:
            Formatted conversation string
        """
        formatted = []
        for msg in messages:
            if isinstance(msg, dict):
                role = msg.get("role", "unknown").capitalize()
                content = msg.get("content", "").strip()
                formatted.append(f"{role}: {content}")
            else:
                # If message is a string, treat it as content with unknown role
                formatted.append(f"Message: {msg.strip()}")
        return "\n".join(formatted)

    def _parse_topics_response(self, response_text: str) -> List[str]:
        """
        Parse topics from LLM response.

        Args:
            response_text: Raw response from LLM

        Returns:
            List of cleaned topic strings
        """
        if not response_text:
            return []

        topics = [topic.strip() for topic in response_text.split(",") if topic.strip()]
        return topics[:5]  # Limit to 5 topics maximum

    async def process_batch(
        self, message_batches: List[List[Dict[str, str]]]
    ) -> List[Dict[str, Union[List[str], str]]]:
        """
        Process multiple conversations in parallel.

        Args:
            message_batches: List of conversation message lists

        Returns:
            List of dictionaries containing topics and summaries
        """
        tasks = []
        for messages in message_batches:
            tasks.extend([self.extract_topics_async(messages), self.summarize_async(messages)])

        results = await asyncio.gather(*tasks, return_exceptions=True)

        processed_results = []
        for i in range(0, len(results), 2):
            topics = results[i] if not isinstance(results[i], Exception) else []
            summary = results[i + 1] if not isinstance(results[i + 1], Exception) else ""

            processed_results.append({"topics": topics, "summary": summary})

        return processed_results
