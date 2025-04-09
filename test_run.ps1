# 1. Create required directories (if they don't exist)
mkdir -p input output logs assets

# 2. Set environment variables
export LLM_API_KEY=AIzaSyAXAHE1b1F9XR5CenP5TTVli
export LLM_PROVIDER=gemini/gemini-2.0-flash

# 3. Create a sample chat file to process
echo "User: What are the key principles of clean code?
Assistant: Clean code principles include: 1) Meaningful names 2) Single responsibility 3) DRY (Don't Repeat Yourself) 4) KISS (Keep It Simple, Stupid) 5) Write good comments 6) Proper formatting 7) Error handling 8) Unit testing
User: Can you elaborate on the Single Responsibility Principle?
Assistant: The Single Responsibility Principle (SRP) states that a class or function should have only one reason to change. This means it should have only one job or responsibility." > input/sample_chat.txt

# 4. Run the indexer
python chat-indexer.py --input-dir ./input --output-dir ./output --log-level INFO