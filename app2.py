from flask import Flask,render_template,request,g
from flask_script import Manager
# import urllib.request


app = Flask(__name__)
app.secret_key = "123456"
manager = Manager(app)

def ggg():
    return "name"

@app.route('/')
def hello_world():
    g.name = "xixi"
    # ggg()
    return render_template("hello.html")


if __name__ == '__main__':
    manager.run()
