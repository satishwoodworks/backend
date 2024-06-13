from psycopg2 import pool
from config import DATABASE_CONFIG

# Create a connection pool
connection_pool = pool.SimpleConnectionPool(
    # min and max number of connections
    minconn=1, 
    maxconn=20,
    **DATABASE_CONFIG
)

def get_connection():
    return connection_pool.getconn()

def put_connection(conn):
    connection_pool.putconn(conn)

def close_all_connections():
    connection_pool.closeall()