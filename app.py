from flask import *
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("API_SECRET_KEY")
peer_name = set()



@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        peer_name.add(request.form.get("name"))
        return redirect(url_for("chatArena"))

@app.route('/show')
def chatArena():
    return render_template("chat.html")




if __name__ == "__main__":
    app.run()



