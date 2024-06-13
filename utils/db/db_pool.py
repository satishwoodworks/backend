from psycopg2 import pool
from config import DATABASE_CONFIG

# Create a connection pool
connection_pool = pool.SimpleConnectionPool(
    1, 20,  # min and max number of connections
    **DATABASE_CONFIG
)

def get_connection():
    return connection_pool.getconn()

def put_connection(conn):
    connection_pool.putconn(conn)

def close_all_connections():
    connection_pool.closeall()