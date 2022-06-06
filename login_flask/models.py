#!/usr/bin/python3
from config import db



# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(35),unique=True,nullable=False)
#     password = db.Column(db.String(35),nullable=False)
#     email = db.Column(db.String(64),unique=True,nullable=False)
#
#     def __str__(self):
#         return 'User: %s' % self.username

class ASN(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    BGPAS = db.Column(db.String(50))
    IP = db.Column(db.String(50))
    communities = db.Column(db.String(50))
    # bgp_id=db.Column(db.Integer,db.ForeignKey('Agasn.id'))


class Agasn(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    ASN= db.Column(db.String(16),nullable=False)
    des = db.Column(db.String(600),nullable=True)



class Sqlclmfor(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(16),nullable=False)
    asn_id = db.Column(db.Integer,db.ForeignKey("agasn.id"))
    asn = db.relationship("Agasn",backref="test")










# if __name__ == '__main__':
#     # db.create_all()
