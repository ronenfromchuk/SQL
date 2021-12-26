import sys
from datetime import datetime
from DbRepo import DbRepo
from sqlalchemy import asc, text, desc
from sqlalchemy import text
from Car import Car
from Driver import Driver
from Many2Many import *
from db_config import local_session, create_all_entities

# create tables


repo = DbRepo(local_session)

local_session.execute('drop TABLE if exists driver cascade')
local_session.commit();
local_session.execute('drop TABLE if exists cars cascade')
local_session.commit();
local_session.execute('drop TABLE if exists orders cascade')
local_session.commit();
local_session.execute('drop TABLE if exists products cascade')
local_session.commit();
local_session.execute('drop TABLE if exists mix_orders_products cascade')
local_session.commit();

create_all_entities()

car1 = Car(model = 'honda', brand = 'civic', year = 2020)
repo.add(car1)
#driver1 = Driver(name='moshe', car_id=2) # error
driver1 = Driver(name='moshe', address='tel aviv', car_id=1)
repo.add(driver1)
# how to unique constrain 2 fields
#driver_error = Driver(name='moshe', address='tel aviv', car_id=1)
#repo.add(driver_error)
driver2 = Driver(name='danny', car_id=1)
repo.add(driver2)

d1 = repo.get_by_id(Driver, 1)
print('d1', d1)
print('d1 car', d1.car)
#print(d1.car.driver)
c1 = repo.get_by_id(Car, 1)
print('c1 driver', c1.driver)

o1 = Order(name='computers')
repo.add(o1)
o2 = Order(name='pricey computers')
repo.add(o2)
p1 = Product(product='Lenovo', price=5002)
repo.add(p1)
p2 = Product(product='Dell', price=12999)
repo.add(p2)
p3 = Product(product='Mac', price=15000)
repo.add(p3)
p3 = Product(product='Mac pro M3', price=45000)
repo.add(p3)

m1 = MixOrdersProducts(order_id = 1, product_id = 1, quantity = 3)
repo.add(m1)
m2 = MixOrdersProducts(order_id = 1, product_id = 2, quantity = 3)
repo.add(m2)
m3 = MixOrdersProducts(order_id = 2, product_id = 3, quantity = 5)
repo.add(m3)


