from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import Union

class document_model:

    def __init__ (self):

        model_name = 'deepset/roberta-base-squad2'
        self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def answer(self, prompt: str, context: Union[str, Document]) -> str:

        if type(context) == str:
            inputs = self.tokenizer(prompt, context, return_tensors = 'pt')

        elif type(context) == Document:
        
            loader = PyPDFLoader(
                context
            )
            pages = loader.load_and_split()
            text = ""
            for i in range(len(pages)):
                text += pages[i].page_content + "\n\n"
            
            inputs = self.tokenizer(prompt, text, return_tensors = 'pt')

        with torch.no_grad():
            outputs = self.model(**inputs)

        i = outputs.start_logits.argmax()
        j = outputs.end_logits.argmax()
                
        tokens = inputs['input_ids'][0][i:j+1]
        completion = self.tokenizer.decode(tokens)

        return completion

    def tokenize(self, query: str) -> torch.Tensor:

        inputs = self.tokenizer(query, return_tensors = 'pt')
        encoded_embeddings = self.model(**inputs)
        return encoded_embeddings
