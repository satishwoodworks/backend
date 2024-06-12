import os

if os.getenv("PRODUCTION_ENV") == "PRODUCTION":
    from .production import *
else:
    from .staging import *