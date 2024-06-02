# wip

from flask import Flask, request, jsonify

# for cross-file compatibility 

from pdf_extraction import pdf_extractor
from model import generateEmb, completion
from vector_storage import storeEmb, queryEmb
from config import get_key

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf(): # backend upload pdf

    file = request.files['file']
    text = pdf_extractor(file)
    embeddings = generateEmb(text)
    document_id = storeEmb(embeddings, text)

    return jsonify({"document_id": document_id})

@app.route('/query', methods=['POST'])
def query(): # backend query
    
    data = request.json
    query_text = data.get('query')
    query_embeddings = generateEmb(query_text)
    result = queryEmb(query_embeddings)

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
