from sqlalchemy import asc, text, desc
from User import User
from Company import Company

class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_all(self, table_class):
        return self.local_session.query(table_class).all()

    def get_all_limit(self, table_class, limit_num):
        return self.local_session.query(table_class).limit(limit_num).all()

    def get_all_order_by(self, table_class, column_name, direction=asc):
        return self.local_session.query(table_class).order_by(direction(column_name)).all()

    def add(self, table_class, one_row):
        pass

    def add_all(self, table_class, rows_list):
        pass

    def delete_by_id(self, table_class, id_column_name, id):
        pass

    def update_by_id(self, table_class, id_column_name, id, data):
        pass

    def get_by_column_value(self, table_class, column_name, value):
        pass