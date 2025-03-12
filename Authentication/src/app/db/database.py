import motor.motor_asyncio as motor #type: ignore
from .config import Config

client = motor.AsyncIOMotorClient(Config.MONGO_CONFIG)

db = client[Config.MONGO_NAME]