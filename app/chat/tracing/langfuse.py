import os
from langfuse.client import Langfuse


langfuse = Langfuse(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host="http://localhost:3000",  # must clone the langfuse git repo and run docker compose up
    # https://langfuse.com/docs/deployment/local
)
