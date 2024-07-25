import chromadb
import os
import chromadb.utils.embedding_functions as embedding_functions
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
import json



# Load the API keys
load_dotenv()
jina_api_key = os.getenv('JINA_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_organization = os.getenv('OPENAI_ORAGNIZATION')
openai_project_id = os.getenv('OPENAI_PROJECT_ID')


# Load the openai client
client = OpenAI(
    api_key=openai_api_key,
    organization=openai_organization,
    project=openai_project_id,
)

# Create the embedding function
jinaai_ef = embedding_functions.JinaEmbeddingFunction(
    api_key=jina_api_key,
    model_name="jina-embeddings-v2-base-en"
)

# Connect to the existing database
chroma_client = chromadb.PersistentClient(path="encyclopedia.db")
collection = chroma_client.get_collection(name="documents", embedding_function=jinaai_ef)



question = "How to attack an enemy?"

# Query the database
rag_results = collection.query(
    query_texts=[question],
    n_results=3
)

prompt = "Based on the folling informations from the Leek Script Encyclopedia, answer the following question: "  + question + "\n\nEncyclopedia pages: \n"
for result in rag_results['documents'][0]:
    prompt += result + "\n\n\n"

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that knows everything about Leek Wars, an online strategy game where players program the AI of their leeks to compete in turn-based battles. The game involves coding in a language called LeekScript, designed specifically for the game."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)