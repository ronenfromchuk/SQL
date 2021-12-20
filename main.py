import sys
from datetime import datetime
from User import User
from DbRepo import DbRepo
from sqlalchemy import asc, text, desc
from sqlalchemy import text
from Company import Company
from db_config import local_session, create_all_entities

# create tables
create_all_entities()

repo = DbRepo(local_session)

repo.reset_auto_inc(User)
repo.reset_auto_inc(Company)

# get_all
#users = local_session.query(User).all()
users = repo.get_all(User)
print(users)
companies = repo.get_all_limit(Company, 3)
print(companies)

users = repo.get_all_order_by(Company, Company.name, asc)
print('asc', users)

users = repo.get_all_order_by(Company, Company.name, desc)
print('desc', users)

# select * from users where username like '%moshe%'
#if len(local_session.query(User).filter(User.username.ilike('%moshe%')).all()) > 0:
#    local_session.query(User).filter(User.id >= 1).delete(synchronize_session=False)
#    local_session.commit()

# Insert
#moshe = User(username='moshe', email='moshe@jb.com')
#local_session.add(moshe)
#local_session.add(User(username='moshe', email='moshe@jb.com'))
moshe = User(username='moshe', email='moshe@jb.com')
repo.add(moshe)

users_list = [User(username='rob', email='rob@rob.com'), User(username='job', email='job@job.com')]
#local_session.add_all(users_list)
#local_session.commit()
repo.add_all(users_list)

#local_session.query(User).filter(User.username == 'moshe').update({User.username: 'new moshe', 'email':'moshe@walla.com'},\
#                                                                  synchronize_session=False)
#local_session.commit()
repo.update_by_column_value(User, User.username, 'moshe', {User.username: 'new moshe', 'email':'moshe@walla.com'})

#local_session.query(Company).filter(Company.id >= 1).delete(synchronize_session=False)

#local_session.add(Company(name='Elad23', age=22, address='Sokolov 11', salary='60000'))
#local_session.commit()
repo.add(Company(name='Elad23', age=22, address='Sokolov 11', salary='60000'))

com1 = Company(name='Yishay13', age=22, address='Sokolov 11', salary='60000')
com2 = Company(name='Uri13', age=22, address='Sokolov 11', salary='70000')
com_ls = [com1, com2]
#local_session.add_all(com_ls)
#local_session.commit()
repo.add_all(com_ls)

print(repo.get_by_ilike(User, User.username, '%moshe%'))
print(repo.get_by_id(User, 2))
#local_session.execute('select * from Company where salary > 60000')
print('> 60,000', repo.get_by_condition(Company, lambda query: query.filter(Company.salary > 60000).all()))
print('> 20, first', repo.get_by_condition(Company, lambda query: query.filter(Company.age > 20).first()))
print('> 20, first', repo.get_by_condition(Company, lambda query: query.filter(Company.age > 20 \
                                                                               and Company.salary > 60000).first()))



