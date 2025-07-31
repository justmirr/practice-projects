import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# initialize llm
groq_llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=GROQ_API_KEY,
)

prompt = ChatPromptTemplate.from_template("translate the following to german: {text}")

# chain using lcel
chain = prompt | groq_llm | StrOutputParser()

result = chain.invoke({"text": "are you an actor?"})
print("translation:", result)