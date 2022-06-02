from redis import Redis
from flask import Flask
from werkzeug.routing import BaseConverter
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


class RegexConverter(BaseConverter):
    """"""

    def __init__(self, url_map, regex):
        """
                :param url_map: 固定传递的参数，用于调用父类的初始化方法
                :param regex: 从url使用（）传递过来的正则参数
                """
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

        # 2. 将自定义的转换器添加到flask的应用中
class Config:
    SECRET_KEY = "dadasfgafdaf"
    re= RegexConverter
    RECAPTCHA_PUBLIC_KEY="fasdfasdfsadfasdfas"
    SESSION_TYPE= 'redis'
    SESSION_REDIS = Redis(host='192.168.1.32', port=6379, db=7, password='p34mv160')
    SQLALCHEMY_DATABASE_URI="sqlite:////sql/flask2.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False


app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)