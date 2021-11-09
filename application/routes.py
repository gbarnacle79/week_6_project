from flask import request, redirect, render_template
from application import app, db
from application.forms import AddCust, UpdateCust, AddGame, UpdateGame
from application.models import Customer, Game
from sqlalchemy import or_




@app.route('/')
def home():
    games = Game.query.all()
    return render_template('homepage.html', gamerecords=games)
    
@app.route('/customers')
def customers():
    
    customer = Customer.query.all()
    return render_template('customers.html', customerrecords=customer)

@app.route('/editgameRecord/<int:gano>', methods=['GET', 'POST'])
def editgameRecordForm(gano):
    form = UpdateGame()
    game = Game.query.filter_by(gano=gano).first()
    if request.method == 'POST':
        game.gname = form.gname.data
        game.age_rate = form.age_rate.data
        game.subtier = form.subtier.data
        game.genre = form.genre.data
        db.session.commit()
        return redirect("/")
    return render_template('editgameform.html', form=form)

@app.route("/filtergames" , methods=["POST"])
def filtergames():
    if request.form["subtier"]=="all":
        return redirect("/")
    if request.form["subtier"]=="platinum":
        data = Game.query.filter(or_(Game.subtier=='platinum',Game.subtier=='gold',Game.subtier=='silver',Game.subtier=='bronze')).all()
        return render_template("homepage.html",gamerecords=data)
    if request.form["subtier"]=="gold":  
        data = Game.query.filter(or_(Game.subtier=='gold',Game.subtier=='silver',Game.subtier=='bronze')).all()
        return render_template("homepage.html",gamerecords=data)
    if request.form["subtier"]=="silver":
        data = Game.query.filter(or_(Game.subtier=='silver',Game.subtier=='bronze')).all()
        return render_template("homepage.html",gamerecords=data)
    if request.form["subtier"]=="bronze":
        data = Game.query.filter(Game.subtier=='bronze').all()
        return render_template("homepage.html",gamerecords=data)

@app.route("/savegameRecord",methods=["GET","POST"])
def savegameRecord():
    form = AddGame()
    if request.method == 'POST':
        name=form.gname.data
        agerate=form.age_rate.data
        sub=form.subtier.data
        genre = form.genre.data
        newgame = Game(gname=name, age_rate=agerate, subtier=sub, genre=genre)
        db.session.add(newgame)
        db.session.commit()
        return redirect("/")
    return render_template("inputgameform.html", form=form)

@app.route("/savecustRecord",methods=["GET","POST"])
def savecustRecord():
    form = AddCust()
    if request.method == 'POST':
        name=form.cust_name.data
        age=form.cust_age.data
        sub=form.subtier.data
        newcust = Customer(cust_name=name, cust_age=age, subtier=sub)
        db.session.add(newcust)
        db.session.commit()
        return redirect("/")
    return render_template("inputcustform.html", form=form)

@app.route("/savecustplat",methods=["GET","POST"])
def savecustplat():
    form = AddCust()
    data = Game.query.filter(or_(Game.subtier=='platinum',Game.subtier=='gold',Game.subtier=='silver',Game.subtier=='bronze')).all()
    form.gname.choices =[(game.gano,game.gname) for game in Game.query.all()]
    if request.method == 'POST':
        name=form.cust_name.data
        age=form.cust_age.data
        game = form.gname.data
        newcust = Customer(cust_name=name, cust_age=age, subtier='platinum', gameid=game)
        db.session.add(newcust)
        db.session.commit()
        return redirect("/")
    return render_template("savecust.html", form=form)


@app.route("/savecustgold",methods=["GET","POST"])
def savecustgold():
    form = AddCust()
    data = Game.query.filter(or_(Game.subtier=='gold',Game.subtier=='silver',Game.subtier=='bronze')).all()
    form.gname.choices =[(game.gano,game.gname) for game in Game.query.all()]
    if request.method == 'POST':
        name=form.cust_name.data
        age=form.cust_age.data
        game = form.gname.data
        newcust = Customer(cust_name=name, cust_age=age, subtier='gold', gameid=game)
        db.session.add(newcust)
        db.session.commit()
        return redirect("/")
    return render_template("savecust.html", form=form)

@app.route("/savecustsilver",methods=["GET","POST"])
def savecustsilver():
    form = AddCust()
    data = Game.query.filter(or_(Game.subtier=='silver',Game.subtier=='bronze')).all()
    form.gname.choices =[(game.gano,game.gname) for game in Game.query.all()]
    if request.method == 'POST':
        name=form.cust_name.data
        age=form.cust_age.data
        game = form.gname.data
        newcust = Customer(cust_name=name, cust_age=age, subtier='silver', gameid=game)
        db.session.add(newcust)
        db.session.commit()
        return redirect("/")
    return render_template("savecust.html", form=form)

@app.route("/savecustbronze",methods=["GET","POST"])
def savecustbronze():
    form = AddCust()
    data = Game.query.filter(Game.subtier=='bronze').all()
    form.gname.choices =[(game.gano,game.gname) for game in Game.query.all()]
    if request.method == 'POST':
        name=form.cust_name.data
        age=form.cust_age.data
        game = form.gname.data
        newcust = Customer(cust_name=name, cust_age=age, subtier='bronze', gameid=game)
        db.session.add(newcust)
        db.session.commit()
        return redirect("/")
    return render_template("savecust.html", form=form)

@app.route("/gamedetails/<int:gano>")
def gamedetails(gano):
	data = Game.query.filter_by(gano=gano).first()
	return render_template("gameinfo.html",gamerecord=data)

@app.route("/customerdetails/<int:cuno>")
def customerdetails(cuno):
	data = Customer.query.filter_by(cuno=cuno).first()
	return render_template("custinfo.html",customerrecord=data)

@app.route("/deletegame/<int:gano>")
def deletegame(gano):
    game = Game.query.filter_by(gano=gano).first()
    db.session.delete(game)
    db.session.commit()
    return redirect("/")

@app.route("/deletecustomer/<int:cuno>")
def deletecustomer(cuno):
    customer = Customer.query.filter_by(cuno=cuno).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect("/")

@app.route('/editcustRecord/<int:cuno>', methods=['GET', 'POST'])
def editcustRecordForm(cuno):
    form = UpdateCust()
    customer = Customer.query.filter_by(cuno=cuno).first()
    if request.method == 'POST':
        customer.cust_name = form.cust_name.data
        customer.cust_age = form.cust_age.data
        customer.subtier = form.subtier.data
        customer.gname = form.gname.data
        db.session.commit()
        return redirect("/")
    return render_template('editcustform.html', form=form)