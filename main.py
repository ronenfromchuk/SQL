from datetime import datetime
from User import User
from sqlalchemy import text
from db_cofig import local_session, create_all_entities

# create tables
create_all_entities()

# local_session.add(User(username='bob', email='bob@bob.com'))
# local_session.commit()

# add a list of users
users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
local_session.add_all(users_list)
local_session.commit()

# delete a user
local_session.query(User).filter(User.id == 2).delete(synchronize_session=False)
local_session.commit()

# print all users
users = local_session.query(User).all()
print(users)
