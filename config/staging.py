DATABASE_CONFIG = {
    'dbname': 'tehelka',
    'user': 'satish',
    'password': 'satishwoodworks',
    'host': '192.168.0.103',
    'port': '5432'
}

OTPS = {
    
}

import os
SERVER_KEY = os.getenv("SERVER_KEY", "testserverkey")
