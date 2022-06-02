#!/usr/bin/python3
from flask import flash

from config import *
from models import User
from form import RegisterForm
@app.route("/",methods=["GET","POST"])
def index():
    form=RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        print(username)
        user = User.query.filter_by(username=username).first()
        print(user.username)
    else:
        print("invalidata")
    return render_template("index.html",form=form)




if __name__ == '__main__':
    app.run(debug=True)