from flask import *
import os
import dotenv
from DataHandling import Data
from ColorPickerModel import ML_Model
import random as rd
import requests


dotenv.load_dotenv()
df = Data()
result = list()
model = ML_Model()
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
        return render_template("main.html", name=peer_name[0])
    else:
        request.form.get('message')
        return render_template("main.html", name=peer_name[0])


@app.route('/3318440929cb74', methods=["POST"])
def recv_sketch():
    res = request.get_data()
    df.update(eval(res))
    while True:
        r = rd.randint(1,255)
        g = rd.randint(1, 255)
        b = rd.randint(1, 255)
        if model.predictor(r, g, b)[0][0] > 2:
            data = dict(r=r, g=g, b=b, rate=model.predictor(r, g, b)[0][0])
            result.append(data)
            break
    return jsonify(eval(res))


@app.route("/b7438d633dd9915c", methods=["GET"])
def sender_ml():
    # print(df.json)
    return jsonify(df.json)






if __name__ == "__main__":
    app.run()
