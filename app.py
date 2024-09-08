
from flask import Flask,render_template,request
import google.generativeai as palm
import os
import numpy as np

api = os.getenv("MAKERSUITE_API_TOKEN")
model = {"model":"models/chat-bison-001"}
palm.configure(api_key=api)

app = Flask(__name__)
user_name = ""
flag = 1

@app.route("/",methods=["GET","POST"])
def index():
    global flag
    flag = 1
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global flag,user_name
    if flag==1:
        user_name = request.form.get("q")
        flag = 0
    return(render_template("main.html",r=user_name))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/DBS",methods=["GET","POST"])
def DBS():
    return(render_template("DBS.html"))

@app.route("/DBS_prediction",methods=["GET","POST"])
def DBS_prediction():
    q = float(request.form.get("q"))
    return(render_template("DBS_prediction.html",r=90.2 + (-50.6*q)))

@app.route("/creditability",methods=["GET","POST"])
def creditability():
    return(render_template("creditability.html"))

@app.route("/creditability_prediction",methods=["GET","POST"])
def creditability_prediction():
    q = float(request.form.get("q"))
    r=1.22937616 + (-0.00011189*q)
    r = np.where(r >= 0.5, "yes","no")
    r = str(r)
    return(render_template("creditability_prediction.html",r=r))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    return(render_template("makersuite.html"))

@app.route("/makersuite_1",methods=["GET","POST"])
def makersuite_1():
    q = "Can you help me prepare my tax return?"
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_1_reply.html",r=r.last))

@app.route("/makersuite_gen",methods=["GET","POST"])
def makersuite_gen():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_gen_reply.html",r=r.last))

if __name__ == "__main__":
    app.run()

