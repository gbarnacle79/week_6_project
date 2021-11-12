from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Customer, Game

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
         SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        
        return app
    
    def setUp(self):
        db.create_all()
        samplegame = Game(gano=5,gname='Halo Reach', age_rate='15', subtier='gold', genre='FPS')
        db.session.add(samplegame)
        db.session.commit()
        newgame = Game(gano=4, gname='Grand Theft Auto 5', age_rate='18', subtier='gold', genre='Sandbox')
        db.session.add(newgame)
        db.session.commit()
        newgame = Game(gano=3,gname='Destiny 2', age_rate='13', subtier='platinum', genre='FPS')
        db.session.add(newgame)
        db.session.commit()
        newgame = Game(gano=2, gname="Sid Meiers Civilization VI", age_rate='12', subtier='silver', genre='RTS')
        db.session.add(newgame)
        db.session.commit()
        newgame = Game(gano=1, gname='Skyrim', age_rate='17', subtier='bronze', genre='RPG')
        db.session.add(newgame)
        db.session.commit()
        samplecustomer = Customer(gameid = 1, cust_name='Bob',cust_age=24,subtier='gold')
        db.session.add(samplecustomer)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_games_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Halo Reach', response.data)
    
    def test_add_game(self):
        response = self.client.post(
            url_for('savegameRecord'),
            data = dict(gano =5,gname='Halo 3', age_rate='15', subtier='gold', genre='FPS'),
            follow_redirects = True)
        self.assertIn(b'Halo 3', response.data)
    
    def test_customers_get(self):
        response = self.client.get(url_for('customers'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bob', response.data)

    def test_add_customer_plat(self):
        response = self.client.post(
            url_for('savecustplat'),
            data = dict(gameid = 1, cust_name='Joan',cust_age=23,subtier='platinum'),
            follow_redirects = True)
        self.assertIn(b'Joan', response.data)

    def test_add_customer_gold(self):
        response = self.client.post(
            url_for('savecustgold'),
            data = dict(gameid = 1, cust_name='Joan',cust_age=23,subtier='gold'),
            follow_redirects = True)
        self.assertIn(b'Joan', response.data)

    def test_add_customer_silver(self):
        response = self.client.post(
            url_for('savecustsilver'),
            data = dict(gameid = 1, cust_name='Joan',cust_age=23,subtier='gold'),
            follow_redirects = True)
        self.assertIn(b'Joan', response.data)

    def test_add_customer_bronze(self):
        response = self.client.post(
            url_for('savecustbronze'),
            data = dict(gameid = 1, cust_name='Joan',cust_age=23,subtier='gold'),
            follow_redirects = True)
        self.assertIn(b'Joan', response.data)

    def test_update_game(self):
        response = self.client.post(
        url_for('editgameRecordForm', gano=5),
        data = dict(gname='Halo Reach', age_rate='15', subtier='platinum', genre='FPS'),
        follow_redirects = True)
        self.assertIn(b'Halo Reach', response.data)

    def test_update_customer(self):
        response = self.client.post(
        url_for('editcustRecordForm', cuno=1),
        data = dict(gameid = 1, cust_name='Bob',cust_age=25,subtier='gold'),
        follow_redirects = True)
        self.assertIn(b'Bob', response.data)
    
    def test_del_game(self):
        response = self.client.get(url_for('deletegame', gano=5), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"George's Gaming Garage", response.data)

    def test_del_customer(self):
        response = self.client.get(url_for('deletecustomer', cuno=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Customer Information System", response.data)

    def test_view_update_game(self):
        response = self.client.get(url_for('editgameRecordForm', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)

    def test_view_update_cust(self):
        response = self.client.get(url_for('editcustRecordForm', cuno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)
 
    def test_view_add_game(self):
        response = self.client.get(url_for('savegameRecord', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)

    def test_view_add_customerplatinum(self):
        response = self.client.get(url_for('savecustplat', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Name", response.data)

    def test_view_add_customergold(self):
        response = self.client.get(url_for('savecustgold', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Name", response.data)

    def test_view_add_customersilver(self):
        response = self.client.get(url_for('savecustsilver', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Name", response.data)

    def test_view_add_customerbronze(self):
        response = self.client.get(url_for('savecustbronze', gano=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Name", response.data)
        

    def test_filter_gold(self):
        response = self.client.post(url_for('filtergames'),
        data = dict(subtier='gold'))
        self.assertIn(b'Halo Reach', response.data)

    def test_filter_all_records(self):
        response = self.client.post(url_for('filtergames'),
        data = dict(subtier='all'), follow_redirects=True)
        self.assertIn(b'Halo Reach', response.data)
    
    def test_filter_bronze(self):
        response = self.client.post(url_for('filtergames'),
        data = dict(subtier='bronze'), follow_redirects=True)
        self.assertIn(b'Skyrim', response.data)

    def test_filter_silver(self):
        response = self.client.post(url_for('filtergames'),
        data = dict(subtier='silver'), follow_redirects=True)
        self.assertIn(b"Sid Meiers Civilization VI", response.data)
    
    def test_filter_platinum(self):
        response = self.client.post(url_for('filtergames'),
        data = dict(subtier='platinum'), follow_redirects=True)
        self.assertIn(b'Destiny 2', response.data)

