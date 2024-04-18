import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
import openai
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

from urllib.parse import quote_plus

username = quote_plus("anamolewi")
password = quote_plus("2004@Lewi")

MONGO_URL = f"mongodb+srv://{username}:{password}@chatgptclone.cslcylh.mongodb.net/?retryWrites=true&w=majority&appName=ChatgptClone"

openai.api_key = openai_api_key

app = Flask(__name__)
CORS(app, origins='*', allow_headers=['Access-Control-Allow-Origin','Content-Type'])

app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app=app)


@app.route("/api/home", methods=["GET", "POST"])
@cross_origin(origin='*',headers=['Access-Control-Allow-Origin','Content-Type'])
def get_response():
    data = {"answer": "It looks like you entered a random string of characters. If there's something specific you would like to discuss or any questions you have, feel free to let me know, and I can help!"}

    if request.method != "POST":
        return jsonify(data)
    
    messages = request.json.get("messages")
    print(messages)
    model = request.json.get("model")

    if len(messages) == 1:
        # then this is a new message
        

#     question = request.json.get("question")
#     chat = mongo.db.chats.find_one({"question": question})
#     print(chat)

#     if chat:
#         data = {"answer": chat['answer']}
#         return jsonify(data)
#     else:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{
#                 "role": "user",
#                 "content": question
#             }],
#             temperature=0.7,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
        
#         print(response)
#         data = {"question": question, "answer": response['choices'][0]['message']['content']}
#         mongo.db.chats.insert_one({"question": question, "answer": response['choices'][0]['message']['content']})

        
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)