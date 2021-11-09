from application import db
from application.models import Customer, Game

db.drop_all()
db.create_all()


newgame = Game( gname='Grand Theft Auto 5', age_rate='18', subtier='gold', genre='Sandbox')
db.session.add(newgame)
db.session.commit()
newgame = Game(gname='Destiny 2', age_rate='13', subtier='platinum', genre='FPS')
db.session.add(newgame)
db.session.commit()
newgame = Game( gname="Sid Meier's Civilization VI", age_rate='12', subtier='silver', genre='RTS')
db.session.add(newgame)
db.session.commit()
newgame = Game( gname='Skyrim', age_rate='17', subtier='bronze', genre='RPG')
db.session.add(newgame)
db.session.commit()
