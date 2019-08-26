from flask import Flask,make_response,request,session

# import urllib.request


app = Flask(__name__)
app.secret_key = "123456"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/set_cookie')
def set_cookie():
    respon = make_response()
    respon.set_cookie("name","小哥哥")
    respon.set_cookie("age","18")
    res="存储成功"
    # key = urllib.request.quote(res)
    print(res)
    return res
@app.route('/get_cookie')
def  get_cookie():
    info=request.cookies
    print(info)
    name=info.get('name')
    print(name)
    return '已取出'
@app.route('/set_session')
def set_session():
    session["room"] = "关山"
    return "session存储成功了"
@app.route('/get_session')
def get_session():
    cc = session.get('room')
    return "%s取出来了"%cc

if __name__ == '__main__':
    app.run(debug=True)
