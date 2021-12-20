
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_config import Base

# create a table based on this class
class User(Base):
    __tablename__ = 'users'

    # static fields
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(25), nullable=False, unique=True)
    # https://docs.sqlalchemy.org/en/14/core/constraints.html#indexes
    email = Column(String(80), nullable=False, unique=True, index=True)
    date_created = Column(DateTime(), default=datetime.utcnow())
    # address = Column(String(80), nullable=False, default="nowhere")

    def __repr__(self):
        return f'\n<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'

    def __str__(self):
        return f'<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'