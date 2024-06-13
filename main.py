import os
import dotenv

from fastapi import FastAPI

ENV = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(ENV, override = True)

from server.routes import users, login


app = FastAPI()

@app.get("/")
def startup():
    return {"response": "Welcome to Tehelka App"}

app.include_router(users.router, prefix="/users")
app.include_router(login.router, prefix="/login")


# TODO: Remove in Production
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
