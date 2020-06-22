from flask import *
from flask_socketio import *
import os, dotenv
"""https://localhost:5000"""

dotenv.load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
socketio = SocketIO(app)

@app.route('/')
def hello():
    return render_template("index.html")


@socketio.on('message', namespace="/test")
def testing(message):
    emit("my response", dict(data=message["data"]))

@socketio.on('my broadcast', namespace="/test")
def my_broadcast_message(message):
    emit("my response", dict(data=message["data"]), broadcast=True)

@socketio.on("connect", namespace="/test")
def test_connector():
    emit("my response",  dict(data="Connected"))



if __name__ == "__main__":
    socketio.run(app)




