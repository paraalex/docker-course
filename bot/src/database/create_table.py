from .connection import conn
from psycopg2 import OperationalError


def execute_query(query, connection=conn):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("table created")

    except OperationalError as e:
        print('table error')
    

create_query = """

CREATE TABLE IF NOT EXISTS message(
    id SERIAL PRIMARY KEY,
    message TEXT,
    user_id BIGINT NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
)
"""
# if __name__=='main':
execute_query(create_query)