from flask import Flask, jsonify
from langchain_helper import getQuestions

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return "Hello World!"

@app.route('/questions',methods=['GET'])
def get_questions():
    output = getQuestions()
    print(output)
    questions = [q.strip().split('. ', 1)[1] for q in output.strip().split('\n') if '. ' in q]
    return {"questions": questions}

if __name__ == "__main__":
    app.run(port=8000, debug=True)