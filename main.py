import uvicorn

from src import app, config

if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=config.PORT)
