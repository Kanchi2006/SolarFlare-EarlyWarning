import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_risk(risk):

    prompt = f"""
    Explain the solar flare risk level {risk}.

    Mention:
    - GPS impact
    - Satellite impact
    - Communication impact

    Keep it under 100 words.
    """

    response = model.generate_content(prompt)

    return response.text