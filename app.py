from flask import *
from flask_socketio import SocketIO
import os, dotenv
dotenv.load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")



