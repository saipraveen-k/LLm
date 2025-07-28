from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import pickle

def create_vector_store(documents, save_path='embeddings/faiss_index.pkl'):
    texts = [Document(page_content=doc) for doc in documents]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(texts)

    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(docs, embeddings)
    with open(save_path, 'wb') as f:
        pickle.dump(vectordb, f)
    return vectordb
