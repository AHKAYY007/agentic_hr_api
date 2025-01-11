from flask import Flask, request, jsonify 
from resume_ai import generate_summary
from cover_letter_ai import generate_cover_letter
from flask_cors import CORS

import os



app = Flask(__name__) #creates an instance of the Flask class
CORS(app) # Enables CORS for all routes and origins


@app.route("/coverletter", methods=['POST'])
def cover_letter():
    data = request.json
    user_input = data

    print(user_input)  
    cover_letter = generate_cover_letter(f"{user_input}")

    response = {
        "cover_letter": cover_letter
    }

    print(cover_letter)
    return jsonify(response)


@app.route('/chat', methods=['POST']) 
def chat():
    data = request.json
    user_input = data

    print(user_input)  
    professional_summary = generate_summary(f"{user_input}")

    response = {
        "professional_summary": professional_summary
    }

    print(professional_summary)
    return jsonify(response)

debug_val = False
if os.getenv("PYTHON_ENV") == "development":
    debug_val = True


if __name__ == '__main__': #runs the app only if the script is executed directly
    app.run(debug=debug_val) #runs the app
