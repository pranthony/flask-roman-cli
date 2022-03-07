from urllib import request
from flask import Flask, render_template, request
from convert import Convert
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/conversor",methods=["GET","POST"])
def convert():
    if request.method == "GET":
        return "Respueta: "+Convert.toRoman(int(request.args.get('num')))