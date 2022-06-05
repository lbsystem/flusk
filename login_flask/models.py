#!/usr/bin/python3
from config import db



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(35),unique=True,nullable=False)
    password = db.Column(db.String(35),nullable=False)
    email = db.Column(db.String(64),unique=True,nullable=False)

    def __str__(self):
        return 'User: %s' % self.username


class ANS(db.Model):
    __tablename__ = 'ASN'
    id = db.Column(db.Integer,primary_key=True)
    BGPAS = db.Column(db.String(50))
    IP = db.Column(db.String(50))
    communities = db.Column(db.String(50))

asn=ANS()
rep=ANS.query.paginate(page=1,per_page=350)
print(rep.pages)
# if __name__ == '__main__':
#     db.create_all()

