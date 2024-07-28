import chromadb
import os
import chromadb.utils.embedding_functions as embedding_functions
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI



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


def generate_response(question, history):
    # Build history
    formatted_history = []
    for user, assistant in history:
        formatted_history.append({"role": "user", "content": user })
        formatted_history.append({"role": "assistant", "content":assistant})

    # Query the database
    rag_results = collection.query(
        query_texts=[question],
        n_results=5
    )
    print(rag_results['ids'][0])

    # Build the prompt
    prompt = "Based on the folling informations from the Leek Script Encyclopedia, answer the following question: "  + question + "\n\nEncyclopedia pages: \n"
    for result in rag_results['documents'][0]:
        prompt += result + "\n\n\n"

    formatted_history.append({"role": "user", "content": prompt})

    # Ask GPT
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages= formatted_history
    )

    return response.choices[0].message.content

# Launch interface
gr.ChatInterface(
    fn=generate_response,
    chatbot=gr.Chatbot(scale=1),
    textbox=gr.Textbox(placeholder="You can ask me anything", container=False, scale=3),
    title="Leek Wars Assistant",
    examples=["How to attack an enemy?", "Give a basic AI"],
    cache_examples=False,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear"
).launch(share=False)