from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain.chains import LLMChain,SequentialChain
from dotenv import load_dotenv
from google_api import api_key
from langchain.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA



model = GoogleGenerativeAI(google_api_key=api_key,model="gemini-pro",temperature=0.6)
embedding = GoogleGenerativeAIEmbeddings(google_api_key=api_key,model="models/embedding-001")
db = FAISS.load_local("E:\\workstation\\LLM\\project_LL\\cusine\\fiass_index",embeddings=embedding,allow_dangerous_deserialization=True)

def recipe_suggester(description):
  suggested_food_templete = """ i descripe to you what i want \
    if there is not one tell me that you dont know , but suggest for me the nearist recipe to it tell only the names not any\
      other thing only english {description} get me only one recip with ingerdient and the steps how much it will take to made in english  """
  suggested_food_prompt = ChatPromptTemplate.from_template(suggested_food_templete)
  prompt  =suggested_food_prompt.format_messages(description=description)
  qr_chain =RetrievalQA.from_chain_type(llm=model,chain_type="stuff", retriever=db.as_retriever())
  print(prompt[0].content)
  return qr_chain.run(prompt[0].content)

print( recipe_suggester("I want something for health"))

 

