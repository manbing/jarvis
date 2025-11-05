from langchain_community.document_loaders import TextLoader, PyPDFLoader, PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.callbacks import CallbackManager
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage


class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

# Read PDF file
directory_path = "./Documentation"
loader = PyPDFDirectoryLoader(directory_path)

# LLM
llm = OllamaLLM(model="llama3", 
             temperature=0.1, 
             top_p=0.4, 
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
             )

# Embedding
token = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
documents = loader.load_and_split(token)
embedding = OllamaEmbeddings(model="nomic-embed-text")
vectors = Chroma.from_documents(documents, embedding)

# Question
AI = ConversationalRetrievalChain.from_llm(llm, vectors.as_retriever())
chat_history = []
while True:
    query = input('\nQ: ')
    if not query:
        break
    result = AI.invoke({"question": query, 'chat_history': chat_history})
    print(color.BOLD + 'Jarvis:' + color.END, result['answer'])
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=result['answer']))
