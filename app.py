import json, os

from flask import Flask, request, render_template, jsonify, make_response, session,send_from_directory,current_app
from pymongo import MongoClient
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
import base64
import hashlib
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA

SECRET_KEY = 'fasdfasdqwrqwe'

client = MongoClient(host="192.168.1.32", port=27017)
collections = client["javbus"]["company"]


def en_aes(data):
    key = b"1111111111111111"
    aes = AES.new(key=key, IV=b'1111111111111111', mode=AES.MODE_CBC)

    data = data
    data = pad(data.encode(), 16, style='pkcs7')

    bs = aes.encrypt(data)
    # data=aes_decrypt(bs)
    print(bs)
    bs = base64.b64encode(bs)
    return bs.decode()


def aes_decrypt(data):
    key = b"1111111111111111"
    data = base64.b64decode(data.encode())
    de_aes = AES.new(key=key, IV=b'1111111111111111', mode=AES.MODE_CBC)
    data = de_aes.decrypt(data)
    data = unpad(data, 16, style="pkcs7")
    data = data.decode()
    return data


app = Flask(__name__)

print(__name__)

app.config['SECRET_KEY'] = "dadasfgafdaf"


@app.route("/", methods=["GET", "POST"])
def index():
    item = {}
    item['name'] = "lb"
    item['age'] = 18
    item['all'] = 'sdfasdggasdgasdgaserwerwq'
    
    if request.method == "GET":
        session["session"] = "test session"
        response = make_response(render_template('index.html'))
        response.set_cookie("name", "lbsystem")

        return response
    else:
        res = request.form.to_dict()
        print(res)
        data = aes_decrypt(res['src'])
        status = hashlib.sha1(data.encode()).hexdigest()
        print(status)
        if status == res['hash']:
            print("confire")
        print(data)
        # res = collections.find_one({'code': res['src']}, {"_id": 0})
        item['encode'] = en_aes(json.dumps(item))
        print(item['encode'])
        print(hashlib.sha256("pp2323pppp".encode()).hexdigest())
        return jsonify(item)
        # if request.files:
        #     file=request.files["file"]
        #     # print("file")
        #     print(file.filename)
        # if request.form:
        #     print("form")
        #
        #     file=request.files["file"]
        # # print("file")
        #     print(file.filename)
        #
        #
        # if request.data:
        #     print("data")
        #     print(request.data)
        #


# @app.after_request
# def check():
#     print(Response.headers)


@app.route("/test")
def test():
    print(request.headers['User-Agent'])
    return render_template('testscroll.html')


@app.route("/img", methods=['POST'])
def get_img():
    # res = collections.find_one({}, {"code":1,"_id": 0})
    res = os.listdir('./static/img')
    return jsonify(res)


@app.route("/js")
def js():
    return render_template('js.html')


@app.route("/path/<test>.m3u")
def path(test):
    res=request.args
    print(res)
    print(test)
    return "ok"
@app.route("/url/url")
def url():
    return render_template('url.html')

@app.route("/ajax", methods=["GET", "POST","TRACE","OPTION"])
def ajax():
    resp = make_response(send_from_directory(path="./static/video/a.mkv",directory='./static/video',filename="a.mkv",as_attachment=True))
    # resp =make_response("fasdfas")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    resp.headers["Content-Disposition"]="attachment;filename=FileName.mkv"
    print(request.headers)
    print(request.form.to_dict())
    p_key='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8JU1nBDZ5PgRNAxksTC/MlaBX37vjTH84ppzmuEpH7e6G43QXd7Zof8apIJ4efk6Uiw2/OJfkyMGDsAJTv/zWnuKm6UeyBYxtgP5JFGtTMKTBVuGzH8UzYWdPzybIOCmj55Qku3nYEZyro38dGhSFLSPaU3eoY1tblm5ZFJ+8ewIDAQAB  '

    # key = RSA.importKey(p_key)
    # key = PKCS1_cipher.new(p_key)
    # print(key)
    return resp



# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=81)
