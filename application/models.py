from application import db




class Game(db.Model):
    gano = db.Column(db.Integer, primary_key = True)
    gname = db.Column(db.String(50))
    age_rate = db.Column(db.Integer)
    genre =db.Column(db.String(50))
    subtier = db.Column(db.String(50))
    customer =db.relationship('Customer',backref='game')

class Customer(db.Model):
    cuno = db.Column(db.Integer, primary_key=True)
    cust_name = db.Column(db.String(50))
    cust_age = db.Column(db.Integer)
    subtier = db.Column(db.String(50))
    gameid = db.Column(db.Integer, db.ForeignKey('game.gano'))
    
