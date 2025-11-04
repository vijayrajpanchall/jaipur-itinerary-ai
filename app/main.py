"""
Main application entry point for Jaipur Itinerary AI.
"""
from fastapi import FastAPI
from app.routes import itinerary_routes

app = FastAPI(title="Jaipur Itinerary AI", version="1.0.0")

# Include routers
app.include_router(itinerary_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Jaipur Itinerary AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
