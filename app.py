from flask import Flask, request, jsonify #imports flask class from flask module
from resume_ai import generate_summary



app = Flask(__name__) #creates an instance of the Flask class

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/chat', methods=['POST']) #python decorator that creates a route
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


if __name__ == '__main__': #runs the app only if the script is executed directly
    app.run(debug=True) #runs the app
