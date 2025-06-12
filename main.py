from flask import Flask, jsonify, request
from langchain_helper import getQuestions, askMe
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [os.getenv("FRONTEND_DEV_API"), os.getenv("FRONTEND_PROD_API")]}})

@app.route('/',methods=['GET'])
def index():
    return "Hello World!"

@app.route('/questions',methods=['GET'])
def get_questions():
    questions = getQuestions()
    return jsonify(questions)

@app.route('/ask',methods=['POST'])
def ask():
    question = request.json['question']
    reply = askMe(question)
    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)