
import os
from tinyfish import TinyFish

api_key = os.getenv("TINYFISH_API_KEY")

if not api_key:
    raise SystemExit("TINYFISH_API_KEY is missing!")

client = TinyFish(api_key=api_key)

response = client.agent.run(
    url="https://example.com",
    goal="Read the page and report its main heading."
)

print(response.result)
