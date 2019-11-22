from tuber import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), default="")
    active = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.username

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    secret = db.Column(db.String(64))
    last_active = db.Column(db.DateTime)

    def __repr__(self):
        return '<Session %r>' % self.id

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(64))
    role = db.Column(db.Integer, db.ForeignKey('role.id'))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128))
    event = db.Column(db.Integer, nullable=True)

class Grant(db.Model):
    # Null values become wildcards, i.e. if event is NULL, then the grant applies to all events
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=True)
    role = db.Column(db.Integer, nullable=True)
    department = db.Column(db.Integer, nullable=True)