#!/usr/bin/python3
from flask import flash,request,make_response

from config import *
from models import User
from form import RegisterForm
import hashlib
import json

hashstr="dasdsa2d"
@app.route("/",methods=["GET","POST"])
@login_required
def index():
    form=RegisterForm()
    # session["name"]="lbsystem2222"
    # print(session.get("name"))
    print(request.cookies)
    if form.validate_on_submit():
        pass

    return render_template("index.html",form=form,hash=hashstr)

@app.route("/post", methods=["POST"])
def post():

    print("start11")
    # res1 = request.query_string
    res1 = request.values.to_dict()

    # res1=json.loads(res1)
    print(res1)
    # print(res1[2]['value'])
    # sha1=hashlib.sha1(hashstr.encode())

    # try:
    #     user=User(username=res1[1]['value'],password=res1[2]['value'],email=res1[3]['value'])
    #     db.session.add(user)
    # except Exception as e:
    #     print(e)
    # else:
    #     db.session.commit()
    #
    resp=make_response("ok")
    resp.set_cookie("name","ajax")

    return resp











if __name__ == '__main__':
    app.run(debug=True)