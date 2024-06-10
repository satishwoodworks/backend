from fastapi import FastAPI

from .routes import users

app = FastAPI()

app.include_router(users.router, prefix="/users")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
