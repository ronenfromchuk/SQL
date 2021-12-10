#eyx3n97ex3ye9q

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_cofig import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True, index=True)  # https://docs.sqlalchemy.org/en/14/core/constraints.html#indexes
    date_created = Column(DateTime(), default=datetime.utcnow())

    def __repr__(self):
        return f'\n<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'

    def __str__(self):
        return f'<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'
