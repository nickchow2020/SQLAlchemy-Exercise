from models import User,db 
from app import app 

db.drop_all()
db.create_all() 

User.query.delete()

shumin = User(first_name='shumin',last_name='zhou',image_url='https://pickaface.net/gallery/avatar/9036435260091952bdb.png')
nick = User(first_name="nick",last_name='zhou',image_url='https://pickaface.net/gallery/avatar/20150418_075523_3821_t_pain.png')
stephen = User(first_name='stephen',last_name='zhou',image_url='https://pickaface.net/gallery/avatar/74841945_161206_2228_2op3n44.png')

db.session.add(shumin)
db.session.add(nick)
db.session.add(stephen)

db.session.commit()