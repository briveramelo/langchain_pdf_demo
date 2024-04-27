from threading import Thread

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from queue import Queue


load_dotenv()
queue = Queue()


class StreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token, **kwargs):
        queue.put(token)

    def on_llm_end(self, response, **kwargs):
        queue.put(None)

    def on_llm_error(self, response, **kwargs):
        queue.put(None)


chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingHandler()],
)
prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}"),
])


class StreamingChain(LLMChain):
    def stream(self, input):
        def task():
            self(input)

        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token


chain = StreamingChain(llm=chat, prompt=prompt)
for output in chain.stream(intput={"tell me a joke"}):
    print(output)
