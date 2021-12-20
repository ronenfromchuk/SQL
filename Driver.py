from sqlalchemy import Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref
from Car import Car

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=True)

    # how to unique constrain 2 fields
    __table_args__ = (UniqueConstraint('name', 'address', name='una_1'),)

    # 1:1
    #car_id = Column(BigInteger, ForeignKey('cars.id'), unique=True, nullable=False)
    car_id = Column(BigInteger, ForeignKey('cars.id'), unique=False, nullable=False)

    # 1: 1
    #car = relationship("Car", backref=backref("driver", uselist=False))

    # 1: N
    car = relationship("Car", backref=backref("driver", uselist=True))

    def __str__(self):
        return f'<Driver> id:{self.id} name:{self.name} car:{self.car}'

    def __repr__(self):
        return f'<Driver> id:{self.id} name:{self.name} car:{self.car}'
