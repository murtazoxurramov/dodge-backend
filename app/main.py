from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods='*',
    allow_headers='*'
)


@app.get(path='/')
def root():
    return "send request to http://127.0.0.1:8000/docs to access to the documentation :)sheers! - "\
        "rsc 💻"
