import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_test_cases(context: str):
    prompt = f"""
You are an experienced QA Engineer.

Generate software test cases from the following document section.

Return ONLY valid JSON in this format:

{{
  "test_cases": [
    {{
      "title": "",
      "preconditions": "",
      "steps": [],
      "expected_result": ""
    }}
  ]
}}

Document:
{context}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text