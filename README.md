# LeekWarsAssistant

LeekWarsAssistant is a [Leek Wars](https://leekwars.com) Chabot to help you code in [LeekScript](https://leekwars.com/encyclopedia/en/LeekScript), powered by RAG!

## How does it works?

#### Get encyclopedia:

It uses the official Leek Wars API to get the encyclopedia page for all the Leek Script functions.

#### Create DB:

Creates the Vector Store with all the documents retrieved from the encyclopedia. Thoses informations are stored in a ChormaDB Vector Store and embedded with JinaAI API.

#### Ask LLM:

Uses a Gradio graphical interface to chat with gpt-3.5. Uses RAG to boost LLM performances.

## How to get LeekWarsAssistant?

###### First clone the repo and install the requirements

* `git clone https://github.com/3cr1sp3l/LeekWarsAssistant`
* `cd LeekWarsAssistant`
* `pip install requirements.txt`

###### Create a `.env` file with your api keys

```
JINA_API_KEY=jina_************************************************************
OPENAI_API_KEY=sk-proj-************************************************
OPENAI_ORAGNIZATION=org-************************
OPENAI_PROJECT_ID=proj_*************************
```

###### Now you need to create the vector store
`python createDB.py`

###### Finally, lauch the Assistant!
`python askLLM.py`
