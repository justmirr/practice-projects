# this file demonstrates fundamental LangChain concepts, including environment setup, custom tool creation, LLMChain usage for text translation, and the implementation of a ReAct agent with a custom tool for specific tasks

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# tool definitions
def add_numbers(x: str) -> str:
    nums = list(map(int, x.split()))
    return str(sum(nums))

agent_tool = Tool(
    name="add_numbers",
    func=add_numbers,
    description="add space-separated numbers - input: '3 4 5'"
)

# llm initialization
groq_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="qwen/qwen3-32b",
    max_tokens=2048,
    temperature=0.7
)

prompt = ChatPromptTemplate.from_template("change {user_queery} to german language")

chain = LLMChain(llm=groq_llm, prompt=prompt)

response = chain.invoke({"user_query": "hi, my name is mir"})
print(response['text'])

# agent setup and execution
agent_prompt_template = """
answer the following questions as best you can. you have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
{agent_scratchpad}
"""

agent_prompt = PromptTemplate.from_template(agent_prompt_template)

agent_react = create_react_agent(llm=groq_llm, tools=[agent_tool], prompt=agent_prompt)

agent_executor = AgentExecutor(agent=agent_react, tools=[agent_tool], verbose=True)

agent_executor.invoke({"input": "add 4 13 65"})