from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


df = pd.read_csv("Flask CDA/CDA/tw.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    items = df.to_dict("records")
    return render_template("index.html", items = items)


if __name__ == "__main__":
    app.run(debug=True)