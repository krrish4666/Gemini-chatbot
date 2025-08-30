from google import genai

# This script verifies the connection to the Gemini API using your environment's API key.

try:
    client = genai.Client()

    resp = client.models.generate_content(
        model="gemini-1.5-pro-latest",
        contents="Give a one-line greeting.",
    )

    # Print output
    print("✅ Connection successful! Gemini says:")
    print(resp.text)

except Exception as e:
    print(f"❌ Test failed: {e}")
