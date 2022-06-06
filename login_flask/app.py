#!/usr/bin/python3
from flask import flash,request,make_response

from config import *
from models import m_to_a,Movie_name,Art_name
from form import RegisterForm
import hashlib
import json

hashstr="dasdsa2d"

res= Art_name.query.filter(Art_name.name=="刘德华").all()
for i in res:
    for y in i.movies:
        print(y.name)

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

# @app.route("/sql/<int:page_c>")
# def sql(page_c=None):
#     page_list=[1,2,3,4,5]
#     res=ANS.query.paginate(page=page_c,per_page=25)
#     if page_c>3 and page_c+3<res.pages:
#         page_list=[i for i in range(page_c-2,page_c+3)]
#     elif page_c+3>=res.pages:page_list=[i for i in range(res.pages-4,res.pages+1)]
#     print(res.pages)
#     return render_template("sql.html",sqldata=res,page_list=page_list)










if __name__ == '__main__':
    app.run(debug=True)