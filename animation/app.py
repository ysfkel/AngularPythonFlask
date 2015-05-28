from flask import Flask
from flask import render_template
app=Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

app.run(debug=True,port=8000,host='0.0.0.0')