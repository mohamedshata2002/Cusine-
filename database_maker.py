import faiss
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain.document_loaders import CSVLoader
from langchain.chains import LLMChain,SequentialChain
from dotenv import load_dotenv
from google_api import api_key
from langchain.vectorstores.faiss import FAISS

loader =CSVLoader(file_path="IndianFoodDatasetCSV.csv",encoding= 'iso-8859-1')
embedding  =GoogleGenerativeAIEmbeddings(google_api_key=api_key,model="models/embedding-001")
vectorstore = FAISS.from_documents(loader.load(),embedding)
vectorstore.save_local("fiass_index")