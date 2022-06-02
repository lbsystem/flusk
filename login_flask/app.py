#!/usr/bin/python3
from flask import flash,request

from config import *
from models import User
from form import RegisterForm
import hashlib
import json
hashstr="dasdsa2d"
@app.route("/",methods=["GET","POST"])
def index():
    form=RegisterForm()
    if form.validate_on_submit():
        pass

    return render_template("index.html",form=form,hash=hashstr)

@app.route("/post", methods=["POST"])
def post():

    print("start11")
    res1 = request.values.get("json1")
    res1=json.loads(res1)
    print(res1)
    print(res1[2]['value'])
    sha1=hashlib.sha1(hashstr.encode())
    res1[2]['value']=sha1.update(res1[2]['value'].encode()).hexdigest()
    try:
        user=User(username=res1[1]['value'],password=res1[2]['value'],email=res1[3]['value'])
        db.session.add(user)
    except Exception as e:
        print(e)
    else:
        db.session.commit()

    return "ok"











if __name__ == '__main__':
    app.run(debug=True)