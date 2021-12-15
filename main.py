import sys
from datetime import datetime
from User import User
from sqlalchemy import text
from db_config import local_session, create_all_entities

# create tables
create_all_entities()

# get_all
users = local_session.query(User).all()
print(users)

# select * from users where username like '%moshe%'
if len(local_session.query(User).filter(User.username.ilike('%moshe%')).all()) > 0:
    local_session.query(User).filter(User.id >= 1).delete(synchronize_session=False)
    local_session.commit()

# Insert
moshe = User(username='moshe', email='moshe@jb.com')
local_session.add(moshe)
#local_session.add(User(username='moshe', email='moshe@jb.com'))
local_session.commit()

users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
local_session.add_all(users_list)
local_session.commit()

local_session.query(User).filter(User.username == 'moshe').update({User.username: 'new moshe', 'email':'moshe@walla.com'},\
                                                                  synchronize_session=False)
local_session.commit()
