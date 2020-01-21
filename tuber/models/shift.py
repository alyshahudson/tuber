from tuber import db

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    department = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
