import pandas as pd
from doc import doc_by_country, doc_by_continent, add_cont
from browser import by_borw, by_os
from time_spent import by_time
from doc_list import list_by_doc, list_by_user
from flask import Flask, render_template, request, send_file


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


    #----------------->Analyizing by browser and OS<-----------------------------------------#
    @app.route("/browser/")
    def browser():
        return render_template("browser.html") #Landing page to analyize by browser and OS


    @app.route("/viz_3/")
    def viz_3():
        return by_borw() #Analyize by browser function


    @app.route("/viz_4/")
    def viz_4():
        return by_os() #Analyize by OS function
    #----------------->Analyizing by browser and OS<-----------------------------------------#



    #----------------->Analyizing by time spent<-----------------------------------------#
    @app.route("/time/")
    def time():
        return render_template("time.html") #The landing page for analytzing by time spent

    @app.route("/viz_5/")
    def viz_5():
        return by_time() #Analyie by time spent function
     #----------------->Analyizing by time spent<-----------------------------------------#


    #----------------->Listing by user based on doc UUID<-----------------------------------------#
    @app.route("/listbydoc/",  methods=['GET', 'POST'])
    def listbydoc():
        return render_template("listbydoc.html") # Landing page for list by user


    @app.route("/table_1", methods=['GET', 'POST'])
    def table_1():
        uuid3 = request.form.get("doc_uuid_2")
        tb = list_by_doc(uuid3)
        return render_template("table_1.html", tables= [tb], 
        titles=[f'All readers for this Doc {uuid3}'])
    #----------------->Listing by user based on doc UUID<-----------------------------------------#


    #----------------->Listing by doc based on user UUID<-----------------------------------------#
    @app.route("/listbyuser/",  methods=['GET', 'POST'])
    def listbyuser():
        return render_template("listbyuser.html") # Landing page for list by doc

    @app.route("/table_2", methods=['GET', 'POST'])
    def table_2():
        uuid4 = request.form.get("user_uuid")
        tb = list_by_user(uuid4)
        return render_template("table_1.html", tables= [tb], 
        titles=[f'All Docs for this User {uuid4}'])

    #----------------->Listing by doc based on user UUID<-----------------------------------------#

    return app
