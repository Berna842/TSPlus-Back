from fastapi import FastAPI                             #type: ignore
from fastapi.middleware.cors import CORSMiddleware      #type: ignore
from starlette.requests import Request                  #type: ignore
from starlette.responses import HTMLResponse            #type: ignore

from .authentication import app as authentication_app

VERSION = '0.1.0'

app = FastAPI(
    title="Authentication-service",
    description="API List for Authentication",
    version=VERSION,
)

origins=[
    ### DEV sources or services required on localhost ###
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://127.0.0.1:8001",
    "http://host.docker.internal:8001/",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    ### Production sources or services required ###

]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.mount("/authentication", authentication_app)

app.get("/", response_class=HTMLResponse, status_code=200)
def root(request: Request):
    return "Authentication Service " + VERSION