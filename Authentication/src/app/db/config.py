import os

class Config:
    MONGO_USER = os.getenv("MONGO_USER", "mongodb")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "")
    MONGO_NAME = os.getenv("MONGO_NAME", "TSP")
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = os.getenv("MONGO_PORT", 27017)
    #MONGO_CONFIG = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_NAME}"
    MONGO_CONFIG = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"