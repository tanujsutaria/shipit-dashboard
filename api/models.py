from . import db

class Order(db.Model):
    """Creates the elements of the Order table in the sqlite3 db"""
    id = db.Column(db.Integer, primary_key = False)
    pk = db.Column(db.Integer, primary_key = True)
    order_number = db.Column(db.Integer)
    order_status = db.Column(db.String)
    order_created_date = db.Column(db.String)
    order_finished_date = db.Column(db.String)
    order_target_finish_date = db.Column(db.String)
    order_late_comment = db.Column(db.String)


