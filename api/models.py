from . import db

class Order(db.Model):
    """Creates the elements of the Order table in the sqlite3 db"""
    id = db.Column(db.Integer)
    ordr_pk = db.Column(db.Integer, primary_key = True)
    ordr_barCode = db.Column(db.Integer) 
    stts_name = db.Column(db.String)
    ordr_createdBy = db.Column(db.String)


