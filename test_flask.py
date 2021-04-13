from unittest import TestCase

from app import app
from models import db,User


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_user_db'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for Pets"""

    def setUp(self):
        db.drop_all()
        db.create_all()

        test_1 = User(first_name="shumin",last_name="zhou",image_url="www.google.com")
        db.session.add(test_1)
        db.session.commit()

        self.user_id = test_1.id

    def tearDown(self):
        db.session.rollback()

    def test_redirect(self):
        with app.test_client() as client: 
            res = client.get("/",follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn('<a href="/users/1">shumin</a>',html)

    def test_add_new_form(self):
        with app.test_client() as client:
            res = client.get('/users/new')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("<h1>Create a user</h1>",html)

    def test_add_user_form(self):
        with app.test_client() as client:
            res = client.post('/users/new',data={'first_name':'hello','last_name':'world','user_url':'www.google.com'},follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<li><a href="/users/2">hello</a></li>',html)

    def test_user_detail(self):
        with app.test_client() as client:
            res = client.get('/users/1')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("<h2>shumin zhou</h2>",html)
