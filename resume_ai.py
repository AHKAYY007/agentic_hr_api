import google.generativeai as genai
from dotenv import load_dotenv
import os



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



INSTRUCTIONS = """Use the following message body format to generate a professional summary of a resume.

The generated professional summary must have the following highlights:
1. The years of experience
2. Different languages and technologies worked on
3. An estimation of the level of expertise based on the years of experience
4. How the user can use his skills to benefit the company
```Note: If the information is not enough, you are free to generate anything.```
"""

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction=INSTRUCTIONS)

chat_session = model
def generate_summary(input):
    
    response = chat_session.generate_content(input)


    return response.text



if __name__ == '__main__':
    pass