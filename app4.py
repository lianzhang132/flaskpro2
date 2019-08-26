from flask import Flask,render_template,request,Markup

# import urllib.request


app = Flask(__name__)
# app.secret_key = "123456"

# @app.template_global('adds')
# def adds(a,b):
#     return a+b

@app.route('/')
def hello_world():
    # str1 = "北京天纳闷"
    # str2 = Markup("<b>只有学习才能让我快乐</b>")

    # return render_template("hello_word.html",str2=str2,str1=str1)
    return render_template("hello_word.html")




if __name__ == '__main__':
    app.run(debug=True)
