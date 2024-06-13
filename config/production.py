import os


DATABASE_CONFIG = {
    "dbname": os.getenv("DB_NAME", "tehelka"),
    "user": os.getenv("DB_USERNAME", "satish"),
    "password": os.getenv("DB_PASSWORD", "satishwoodworks"),
    "host": os.getenv("DB_HOST", "10.168.0.103"),
    "port": os.getenv("DB_PORT", "5432"),
}

OTPS = dict()
SERVER_KEY = os.getenv("SERVER_KEY", "testserverkey")
