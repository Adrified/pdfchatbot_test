# wip since not fine-tuned yet

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer # huggingface gives u access to FLAN-T5 and BERT/BART family
import torch

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small") # small so gpu doesnt explode
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small", use_fast = True)

prompt = input("How may I help you today? ")

def completion(prompt): # generates completions given a prompt

    inputs = tokenizer(prompt, return_tensors = "pt")
    outputs = model.generate(**inputs)
    completion = (tokenizer.batch_decode(outputs, skip_special_tokens = True))

    return completion

def generateEmb(query): # encodes a query and generates embeddings

    inputs = tokenizer(query, return_tensors = "pt")

    with torch.no_grad(): # just the encodings

        encoder_outputs = model.get_encoder()(**inputs)
    
    encoder_embeddings = encoder_outputs.last_hidden_state

    return encoder_embeddings

embeddings = generateEmb(prompt)

print(embeddings)

# :) ???

#def generate(query): # full encoder/decoder function

#    inputs = tokenizer(query, return_tensors = "pt")
#    outputs = model.generate(**inputs)
#    completion = (tokenizer.batch_decode(outputs, skip_special_tokens = True))

#    with torch.no_grad(): # to isolate encodings

#        encoder_outputs = model.get_encoder()(**inputs)
    
#    encoder_embeddings = encoder_outputs.last_hidden_state

#    return completion, encoder_embeddings # double return statement, where encoder_embeddings is the input in vector form
