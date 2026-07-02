from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_summary(document_text):

    prompt = f"""
You are a cybersecurity compliance expert.

Analyze the following document.

Provide:

1. Document Summary

2. Sensitive Information Found

3. Compliance Observations

4. Security Risks

5. Recommended Remediation

6. Overall Risk

Document:

{document_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text