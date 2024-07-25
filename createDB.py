import chromadb
import os
import chromadb.utils.embedding_functions as embedding_functions
from dotenv import load_dotenv

# Load the API keys
load_dotenv()
jina_api_key = os.getenv('JINA_API_KEY')

# Load the encyclopedia pages
directory = "encyclopedia"

# Create the embedding function
jinaai_ef = embedding_functions.JinaEmbeddingFunction(
    api_key=jina_api_key,
    model_name="jina-embeddings-v2-base-en"
)

# Create a new database
chroma_client = chromadb.PersistentClient(path="encyclopedia.db")
collection = chroma_client.create_collection(name="documents", embedding_function=jinaai_ef)
print("Collection created")

# Insert encyclopedia pages
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

        # Insert document
        collection.add(
            documents=[content],
            ids=[filename[:-3]]
        )
    print(" Document " + filename[:-3] +  " inserted")

print("All documents inserted")
