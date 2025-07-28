from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import pickle

def get_answer(user_query, vectordb_path='embeddings/faiss_index.pkl'):
    with open(vectordb_path, 'rb') as f:
        vectordb = pickle.load(f)

    llm = ChatOpenAI(model="gpt-4")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    result = qa_chain.run(user_query)
    return result
