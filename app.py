from flask import *
import os, dotenv
"""https://localhost:5000"""

app = Flask(__name__)
peer_name = set()



@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        peer_name.add(request.form.get("name"))
        return redirect(url_for("show"))

@app.route('/show')
def show():
    return " , ".join(list(peer_name))


if __name__ == "__main__":
    app.run()



