from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.routers import unavailable_items

load_dotenv()

app = FastAPI(
    title="RAP System - Unavailable Items API",
    description="Bulk API for retrieving unavailable items from multiple restaurant locations",
    version="1.0.0",
)

origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:8080").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(unavailable_items.router)

@app.get("/")
async def root():
    return {
        "message": "RAP System - Unavailable Items API",
        "version": "1.0.0",
        "docs": "/docs",
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)