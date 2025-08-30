import os
from google import genai


client = genai.Client()

# Send a simple prompt
resp = client.models.generate_content(
    model="gemini-2.5-pro",   # you can also try "gemini-1.5-pro" for a stronger model
    contents="Give a one-line greeting.",
)

# Print output
print(resp.text)
