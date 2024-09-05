from flask import Flask, request, jsonify
from flask_cors import CORS
from model import document_model

app = Flask(__name__)
CORS(app)

v1_model = document_model()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    bot_response = v1_model(user_message, 'insert context here')

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
