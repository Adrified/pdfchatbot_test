# AI Chatbot for Document Question Answering

This repository holds the code for an experimental AI Chatbot designed to extract text from documents (specifically PDFs) and answer questions about the document. <br/><br/>

In this fullstack project, I am designing a model that converts document text to strings for LLM-powered Q&Aing. </br> 
Methods for question answering and text vectorization have been provided <br/> 
To use, initialize a `document_model` object in the main class, and implementation is self-explanatory so please refer to method args and return types. 

### Raw Python Usage:
Step 1: Install dependencies <br/><img width="466" alt="image" src="https://github.com/user-attachments/assets/2d128503-8bff-4079-aca5-217a9d72bf66"><br/>
Step 2: Initialize a `document_model` object. <br/><img width="158" alt="image" src="https://github.com/user-attachments/assets/babbd266-60f4-46aa-bd2c-ba283277eb17"><br/>
Step 3: Test performance with examples <br/><img width="861" alt="image" src="https://github.com/user-attachments/assets/d71fb1dd-fbe7-4b45-a5b0-0c9394a3341e"><br/>
Output: <br/><img width="869" alt="image" src="https://github.com/user-attachments/assets/9f42e163-3ed2-455e-9409-84c24c75e56a"><br/>

### Progress:

Frontend ❌ | Backend ✅ | AI Integration ✅ | PDF Parsing ✅ | Vector Database w/ API ❌

### IMPORTANT:
For `document_model.answer()` to take documents, you must insert a local path or an accessible URL
