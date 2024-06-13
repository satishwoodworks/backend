import os

PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "staging").lower()

if PRODUCTION_ENV == "production":
    from .production import *
else:
    from .staging import *