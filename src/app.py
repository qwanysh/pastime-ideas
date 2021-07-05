from fastapi import FastAPI

from src import sxodim

app = FastAPI(docs_url=None)

app.include_router(sxodim.router, prefix='/sxodim', tags=['sxodim'])
