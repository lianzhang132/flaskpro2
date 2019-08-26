from flask import Flask,render_template,request

# import urllib.request


app = Flask(__name__)
app.secret_key = "123456"

@app.template_global('adds')
def adds(a,b):
    return a+b
#
@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/login')
def login():
    msg = "hhahhah"
    return render_template("login.html")

@app.route('/logindl',methods=['get','post'])
def logindl():
    print(request.method)

    # get方式提交
    print(request.args.get("name"))
    print(request.args.get("password"))
    # post方式提交
    print(request.form.get("name"))
    print(request.form.get("password"))

    return "获取成功"

if __name__ == '__main__':
    app.run(debug=True)
