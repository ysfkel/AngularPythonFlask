from flask import Flask
from flask import render_template
from flask import redirect, url_for,request,json
app=Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/home")
def home():
	return render_template("home.html")	
	
@app.route('/save',methods=['POST'])
def save():
	#return "saved"
	return redirect(url_for("home"))
	

	

app.run(debug=True,port=8000,host='0.0.0.0')