from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/document/", methods=["GET","POST"])
def document():
    uuid = request.form.get("doc_uuid")
    print(uuid)
    return render_template("document.html")

@app.route("/table")
def table():
    df = pd.read_json('../data/sample_small.json', lines=True)
    df = df.iloc[:10, :]
    tb = df.to_html()
    return str(tb)
