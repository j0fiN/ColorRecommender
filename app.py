from flask import *
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("API_SECRET_KEY")
peer_name = list()



@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        peer_name.append(request.form.get("name"))
        return redirect(url_for("chatArena"))

@app.route('/show', methods=["GET", "POST"])
def chatArena():
    if request.method == "GET":
        return render_template("chat.html", chatter_name=peer_name[0])
    else:
        return render_template("chat.html", chatter_name=peer_name[0])





if __name__ == "__main__":
    app.run()



