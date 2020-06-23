from flask import *
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("API_SECRET_KEY")
peer_name = list()
peer_list = list()


@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        peer_name.append(request.form.get("name"))
        peer_list.append(request.form.get("name"))
        return redirect(url_for("chatArena"))


@app.route('/show', methods=["GET", "POST"])
def chatArena():
    if request.method == "GET":
        return render_template("main.html", name=peer_name[0])
    else:
        request.form.get('message')
        return render_template("main.html", name=peer_name[0])


@app.route('/api', methods=["POST"])
def recv():
    res = request.get_data()
    print(eval(res))
    return jsonify(eval(res))


if __name__ == "__main__":
    app.run()
