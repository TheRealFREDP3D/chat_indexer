"""
Integration tests for LLMClient using real API calls.
"""

import os
import sys
import asyncio
import pytest

# Add parent directory to path to make imports work
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Now we can import from src
from src.llm_client import LLMClient
from src.config import Config

# Test mock conversations data with real API calls
REAL_CONVERSATIONS = [
    [
        {"role": "user", "content": "What are the key principles of clean code?"},
        {
            "role": "assistant",
            "content": "Clean code principles include: 1) Meaningful names 2) Single responsibility 3) DRY (Don't Repeat Yourself) 4) KISS (Keep It Simple, Stupid) 5) Write good comments 6) Proper formatting 7) Error handling 8) Unit testing",
        },
        {"role": "user", "content": "Can you elaborate on the Single Responsibility Principle?"},
        {
            "role": "assistant",
            "content": "The Single Responsibility Principle (SRP) states that a class or function should have only one reason to change. This means it should have only one job or responsibility. For example, a class that handles user authentication shouldn't also be responsible for logging or data validation. This makes code more maintainable, testable, and easier to understand.",
        },
    ],
    [
        {"role": "user", "content": "Explain the difference between unit testing and integration testing"},
        {
            "role": "assistant",
            "content": "Unit tests focus on testing individual components or functions in isolation, often using mocks for dependencies. Integration tests verify that multiple components work together correctly. For example, a unit test might check a single database query function, while an integration test would verify the entire data access layer working with a real database.",
        },
        {"role": "user", "content": "What are some popular testing frameworks?"},
        {
            "role": "assistant",
            "content": "Popular testing frameworks include: 1) JUnit for Java 2) pytest for Python 3) Jest for JavaScript 4) NUnit for .NET 5) RSpec for Ruby. These frameworks provide tools for test organization, assertions, mocking, and test running.",
        },
    ],
]


@pytest.mark.asyncio
async def test_real_topic_extraction():
    """Test topic extraction with real API calls."""
    client = LLMClient(Config.LLM_PROVIDER)

    print("\nTesting real topic extraction...")
    topics = await client.extract_topics_async(REAL_CONVERSATIONS[0])

    print(f"Extracted topics: {topics}")
    assert isinstance(topics, list)
    assert len(topics) > 0
    assert any("clean code" in topic.lower() for topic in topics)


@pytest.mark.asyncio
async def test_real_summarization():
    """Test summarization with real API calls."""
    client = LLMClient(Config.LLM_PROVIDER)

    print("\nTesting real summarization...")
    summary = await client.summarize_async(REAL_CONVERSATIONS[0])

    print(f"Generated summary: {summary}")
    assert isinstance(summary, str)
    assert len(summary) > 50  # Reasonable summary length
    assert "clean code" in summary.lower() or "single responsibility" in summary.lower()


@pytest.mark.asyncio
async def test_real_batch_processing():
    """Test batch processing with real API calls."""
    client = LLMClient(Config.LLM_PROVIDER)

    print("\nTesting real batch processing...")
    results = await client.process_batch(REAL_CONVERSATIONS)

    print("\nBatch processing results:")
    for i, result in enumerate(results):
        print(f"\nConversation {i + 1}:")
        print(f"Topics: {result['topics']}")
        print(f"Summary: {result['summary']}")

        assert isinstance(result, dict)
        assert "topics" in result
        assert "summary" in result
        assert len(result["topics"]) > 0
        assert len(result["summary"]) > 0


@pytest.mark.asyncio
async def test_real_rate_limiting():
    """Test rate limiting with real API calls."""
    client = LLMClient(Config.LLM_PROVIDER, rate_limit_delay=1.0)

    print("\nTesting rate limiting...")
    start_time = asyncio.get_event_loop().time()

    # Make multiple requests
    for _ in range(3):
        await client.extract_topics_async(REAL_CONVERSATIONS[0])

    elapsed = asyncio.get_event_loop().time() - start_time
    print(f"Time elapsed for 3 requests: {elapsed:.2f} seconds")

    # Should take at least 2 seconds due to rate limiting
    assert elapsed >= 2.0


async def main():
    """Run all tests sequentially and display results."""
    print(f"Running integration tests with provider: {Config.LLM_PROVIDER}")

    client = LLMClient(Config.LLM_PROVIDER)

    # Test topic extraction
    topics = await client.extract_topics_async(REAL_CONVERSATIONS[0])
    print("\nTopic Extraction Test:")
    print(f"Topics: {topics}")

    # Test summarization
    summary = await client.summarize_async(REAL_CONVERSATIONS[0])
    print("\nSummarization Test:")
    print(f"Summary: {summary}")

    # Test batch processing
    results = await client.process_batch(REAL_CONVERSATIONS)
    print("\nBatch Processing Test:")
    for i, result in enumerate(results):
        print(f"\nConversation {i + 1}:")
        print(f"Topics: {result['topics']}")
        print(f"Summary: {result['summary']}")

    # Display final stats
    stats = client.get_stats()
    print("\nFinal Stats:")
    print(f"Total requests: {stats['requests']}")
    print(f"Total tokens: {stats['total_tokens']}")
    print(f"Errors: {stats['errors']}")


if __name__ == "__main__":
    asyncio.run(main())
