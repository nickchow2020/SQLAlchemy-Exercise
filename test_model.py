from unittest import TestCase

from app import app
from models import db,User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_user_db'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all() 

class UserModelTestCase(TestCase):

    def setUp(self):
        User.query.delete() 
    
    def tearDown(self):
        db.session.rollback()

    def test_greeting(self):
        user = User(first_name='shumin',last_name='zhou',image_url='www.google.com')
        self.assertEqual(user.greeting(),"Hi,my name is shumin zhou!")

    def test_add_new_user(self):
        user = User(first_name='shumin',last_name='zhou',image_url='www.google.com')
        db.session.add(user)
        db.session.commit()

        shumin = User.query.get(1)
        self.assertEqual(shumin,user)

