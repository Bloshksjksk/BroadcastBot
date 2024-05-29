import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5484278199:AAFyPN7RbJQC4usLJQ_WtBuE0jtqiInIGpA")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002182387390"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "945284066").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://misoc51233:ZlP391e4m0IIS85S@cluster0.8xs2zsl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
