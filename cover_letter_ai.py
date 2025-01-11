import google.generativeai as genai
from dotenv import load_dotenv
import os



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



INSTRUCTIONS = """Use the following message body format to generate a cover letter of a resume.

The generated cover letter must have the following highlights:
1. What motivates the potential employee to apply for the job and also working for the companies
2. How the potential employee can provide value to the employer 
3. Ability of the potential employee to meet time deadlines 
4. How the potential employee can be of value to the the team in terms of his/her soft skills, such as communication and more
5. A brief feedback expetation summary
```Note: If the information is not enough, you are free to generate anything.
   only generate the body of the cover letter.
   No matter the limited information you get, use your large language model and your current knowledge to generate a complete cover letter body
    that is industry standard.```
"""

model=genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction=INSTRUCTIONS)

chat_session = model
def generate_cover_letter(input):
    
    response = chat_session.generate_content(input)


    return response.text




if __name__ == '__main__':
    pass