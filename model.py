from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

model_name = 'google/flan-t5-large'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast = True)

def completion(prompt):

    inputs = tokenizer(prompt, return_tensors = "pt")
    outputs = model.generate(**inputs)
    completion = (tokenizer.batch_decode(outputs, skip_special_tokens = True))
    return completion[0]

def generateEmb(query):
    inputs = tokenizer(query, return_tensors = "pt")

    with torch.no_grad():
        encoder_outputs = model.get_encoder()(**inputs)

    encoder_embeddings = encoder_outputs.last_hidden_state
    return encoder_embeddings
