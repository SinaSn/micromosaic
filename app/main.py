from fastapi import FastAPI
from app.api.v1.endpoints import auth

app = FastAPI(title="MicroMosaic Project")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "OK"}

# print("Creating database tables...")
# Base.metadata.create_all(bind=engine)
# print("Tables created successfully.")