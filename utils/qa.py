from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_question(document_text, question):

    prompt = f"""
You are a cybersecurity compliance assistant.

Only answer using the document below.

If the answer isn't in the document, say:

"I couldn't find that information in the uploaded document."

Document:

{document_text}

Question:

{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text