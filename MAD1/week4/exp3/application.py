#from requests import request
from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

#@app.route("/")
@app.route("/hello",methods=["GET","POST"])

def hello_world():
   # return render_template("hello_world.html")
   # return render_template("get_details.html")
    if request.method == "GET":
        return render_template("get_details.html")
    elif request.method == "POST":
        username = request.form["user_name"]
        return render_template("get_display_details.html", display_name=username)
    else:
        print("Error")

if __name__=='__main__':
    app.debug=True   #to get error message
    app.run()