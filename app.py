from flask import Flask,request,render_template,jsonify


app = Flask(__name__)

print(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    item={}
    item['name']="lb"
    item['age']=18
    if request.method=="GET":

        html=""
        list1=str(request.headers).split("\r\n")
        for i in list1:
            str1="<p>"+i+"</p>"+"\r\n"
            html+=str1
    else:
        if request.files:
            file=request.files["file"]
            # print("file")
            print(file.filename)
        if request.form:
            print("form")
            print(request.form.to_dict())
            file=request.files["file"]
        # print("file")
            print(file.filename)

            return jsonify(item)
        if request.data:
            print("data")
            print(request.data)


    return render_template("fetch.html")


if __name__ == '__main__':
    app.run()