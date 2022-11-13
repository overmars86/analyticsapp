import pandas as pd
from doc import doc_by_country, doc_by_continent, add_cont
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return render_template("index.html")

    #Analyize by document route start
    @app.route("/document/", methods=["GET","POST"])
    def document():
        global uuid
        uuid = request.form.get("doc_uuid")
        # if uuid is None:
        #     return render_template("error.html") #and request.form.clear("doc_uuid")
        # elif len(uuid) == 45:
        #     return render_template("document.html") #and request.form.clear("doc_uuid")
            
        # else:
        #     # chart = doc_by_country(str(uuid))
        #     # print(chart)
        #     print(uuid)
        return render_template("document.html")
            

    @app.route("/viz/")
    def viz():
        return doc_by_country(uuid)

    @app.route("/viz_2/")
    def viz_2():
        df = add_cont()
        return doc_by_continent(uuid, df)
    #Analyize by document route finsih


    @app.route("/table")
    def table():
        df = pd.read_json('../data/sample_small.json', lines=True)
        df = df.iloc[:10, :]
        tb = df.to_html()
        return str(tb)
    return app
