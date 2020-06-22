from flask import *
from flask_socketio import *
import os, dotenv
"""https://localhost:5000"""

dotenv.load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
socketio = SocketIO(app)

# @app.route('/')
# def hello():
#     return render_template("index.html")

@socketio.on('message')
def handle(msg):
    print("hello")
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app)




