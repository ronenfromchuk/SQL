import sys
from sqlalchemy import asc, text, desc

class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session

    def reset_auto_inc(self, table_class):
        self.local_session.execute(f'TRUNCATE TABLE {table_class.__tablename__} RESTART IDENTITY CASCADE')

    def get_by_id(self, table_class, id):
        return self.local_session.query(table_class).get(id)

    def get_all(self, table_class):
        return self.local_session.query(table_class).all()

    def get_all_limit(self, table_class, limit_num):
        return self.local_session.query(table_class).limit(limit_num).all()

    def get_all_order_by(self, table_class, column_name, direction=asc):
        return self.local_session.query(table_class).order_by(direction(column_name)).all()

    def get_by_condition(self, table_class, cond):
        #return self.local_session.query(table_class).filter(Company.salary > 70000).all()
        query_result = self.local_session.query(table_class)
        result = cond(query_result)
        return result
        #return cond( self.local_session.query( table_class ) )

    def add(self, one_row):
        # what about PK
        self.local_session.add(one_row)
        # one_row.id  = will get the next id
        self.local_session.commit()

    def add_all(self, rows_list):
        self.local_session.add_all(rows_list)
        self.local_session.commit()

    def delete_by_id(self, table_class, id_column_name, id):
        self.local_session.query(table_class).filter(id_column_name == id).delete(synchronize_session=False)
        self.local_session.commit()

    def update_by_id(self, table_class, id_column_name, id, data):
        self.local_session.query(table_class).filter(id_column_name == id).update(data)
        self.local_session.commit()

    def update_by_column_value(self, table_class, column_name, value, data):
        self.local_session.query(table_class).filter(column_name == value).update(data)
        self.local_session.commit()

    def get_by_column_value(self, table_class, column_name, value):
        return self.local_session.query(table_class).filter(column_name == value).all()

    def get_by_ilike(self, table_class, column_name, exp):
        return self.local_session.query(table_class).filter(column_name.ilike(exp)).all()
