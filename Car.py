
from sqlalchemy import Column, BigInteger,Integer, String, DateTime, REAL, Date
from db_config import Base

class Car(Base):
    __tablename__ = 'cars'
    id = Column(BigInteger, primary_key=True)
    model = Column(String(25), nullable=False)
    brand = Column(String(25), nullable=False)
    year = Column(Integer, nullable=False)

    def __str__(self):
        return f'<Car> id:{self.id} model:{self.model} brand:{self.brand} year:{self.year}'

    def __repr__(self):
        return f'<Car> id:{self.id} model:{self.model} brand:{self.brand} year:{self.year}'
