import os

if os.getenv("PRODUCTION_ENV").lower() == "production":
    from .production import *
else:
    from .staging import *