from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22359038"))
    API_HASH = getenv("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")
    BOT_TOKEN = getenv("BOT_TOKEN", "5630873709:AAHtEhH9rsZslFQw3dHngt37jjwkNdK16qc")
    CHID = int(getenv("CHID", None))
    SUDO = list(map(int, getenv("SUDO").split(5531461861)))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Adish4:Adish4@cluster0.dyhrj0e.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
