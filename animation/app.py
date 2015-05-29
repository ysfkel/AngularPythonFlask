from flask import Flask
from flask import render_template
from flask import (redirect, url_for,
                   request,json,make_response)


app=Flask(__name__)



@app.route("/")
def index():
	data=get_cookie()
	return render_template("index.html",saves=data)
	
@app.route("/home")
def home():
	return render_template("home.html")	
	
@app.route('/save',methods=['POST'])
def save():
	#return "saved"
	response=make_response(redirect(url_for("index")))
	data=get_cookie()
	data.update(dict(request.form.items()))
	response.set_cookie('character',json.dumps(data))
	return response
	

		
def get_cookie():
	try:
		data=json.loads(request.cookies.get('character'))
	except TypeError:
		data={}
	return data

	

app.run(debug=True,port=8000,host='0.0.0.0')