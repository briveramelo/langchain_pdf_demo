from threading import Thread

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from queue import Queue


load_dotenv()





chat = ChatOpenAI(
    streaming=True,
)
prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}"),
])





class StreamingChain(StreamableChain, LLMChain):
    pass


chain = StreamingChain(llm=chat, prompt=prompt)
for output in chain.stream(input={"tell me a joke"}):
    print(output)
