
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # <--- Replace this

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def generate_joke(topic="cats"):
    prompt = f"Tell me a funny, short joke about {topic}. Keep it clean."
    response = model.generate_content(prompt)
    return response.text

print(generate_joke("programmers"))
