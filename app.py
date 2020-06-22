from flask import *
from flask_socketio import *
import os, dotenv
"""localhost:5000"""

dotenv.load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
socketio = SocketIO(app)

@app.route('/')
def hello():
    return "hello"

@socketio.on('Event', namespace="/test")
def recv_msg(message):
    print("recved msg : ", message)
    return 2

def confirm():
    print("message recved")

@socketio.on('Event')
def reply(message):
    emit("my res", message, namespace="/chat", callback=confirm)




if __name__ == "__main__":
    socketio.run(app)




