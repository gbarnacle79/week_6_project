from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField


class AddCust(FlaskForm):

    cust_name = StringField("Name")
    cust_age = IntegerField("Age")
    gname = SelectField("Game", choices=[])
    subtier = SelectField("Subscription", choices=[('bronze','Bronze'),('silver','Silver'),('gold','Gold'),('platinum','Platinum')])
    cust_submit = SubmitField('Add Customer')

class UpdateCust(FlaskForm):
    cust_name = StringField("Name")
    cust_age = IntegerField("Age")
    gname = SelectField("Game", choices=[])
    subtier = SelectField("Subscription", choices=[('bronze','Bronze'),('silver','Silver'),('gold','Gold'),('platinum','Platinum')])
    cust_submit = SubmitField('Update Customer')

class AddGame(FlaskForm):
    gname = StringField("Name")
    age_rate = IntegerField("Age")
    subtier = SelectField("Subscription", choices=[('bronze','Bronze £1'),('silver','Silver £2'),('gold','Gold £3'),('platinum','Platinum £4')])
    genre = SelectField("Genre", choices=[('Sandbox','Sandbox'),('FPS','FPS'),('RTS','RTS'),('RPG','RPG'),('Sports','Sports')])
    game_submit = SubmitField('Add Game')

class UpdateGame(FlaskForm):
    gname = StringField("Name")
    age_rate = IntegerField("Age")
    subtier = SelectField("Subscription", choices=[('bronze','Bronze £1'),('silver','Silver £2'),('gold','Gold £3'),('platinum','Platinum £4')])
    genre = SelectField("Genre", choices=[('Sandbox','Sandbox'),('FPS','FPS'),('RTS','RTS'),('RPG','RPG'),('Sports','Sports')])
    game_submit = SubmitField('Update Game')

