"""
Itinerary routes for the Jaipur Itinerary AI API.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.itinerary_service import ItineraryService

router = APIRouter(prefix="/api/itinerary", tags=["itinerary"])

itinerary_service = ItineraryService()


class ItineraryRequest(BaseModel):
    days: int
    interests: Optional[str] = None
    budget: Optional[str] = None


@router.post("/generate")
async def generate_itinerary(request: ItineraryRequest):
    """
    Generate a personalized itinerary for Jaipur based on user preferences.
    """
    try:
        itinerary = await itinerary_service.generate_itinerary(
            days=request.days,
            interests=request.interests,
            budget=request.budget
        )
        return {"itinerary": itinerary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/places")
async def get_places():
    """
    Get list of popular places in Jaipur.
    """
    try:
        places = await itinerary_service.get_places()
        return {"places": places}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
