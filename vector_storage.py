# also wip havent tested embeddings yet

import pinecone
import hashlib
from pdf_extraction import pdf_extractor # cross file compatibility since api is dependent on all files

pinecone.init(api_key = 'put api key here when rdy') # hidden on the backend
index = pinecone.Index('INSERT PDF EMBEDDINGS FROM EXTRACTION HERE')

def generate_document_id(text): # generates a unique doc id

    return (hashlib.md5(text.encode()).hexdigest())

def storeEmb(embeddings, text): # stores the embeddings in the Pinecone index, also used for continuity

    document_id = generate_document_id(text)
    index.upsert(vectors = [(document_id, embeddings)])

    return document_id
    
def queryEmb(embeddings): # query the index from pinecone to find the most similar embedding

    result = index.query(embeddings, top_k = 1)

    return result['matches'][0]

# :)
