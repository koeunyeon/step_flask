from flask import Flask
from flask import url_for # (1)

app = Flask(__name__)


@app.route("/hello_world/")
def helloworld(): 
    return "hello world"

@app.route("/url_for/")  #(2)  
def sample_url_for():
    url = url_for("helloworld")
    return url
