"""
Itinerary service for generating personalized Jaipur itineraries.
"""
import pandas as pd
from typing import Optional
from app.ai.chains.itinerary_chain import ItineraryChain
from app.services.weather_service import WeatherService
from app.services.maps_service import MapsService


class ItineraryService:
    def __init__(self):
        self.itinerary_chain = ItineraryChain()
        self.weather_service = WeatherService()
        self.maps_service = MapsService()
        self.places_data = None
        self._load_places_data()

    def _load_places_data(self):
        """Load places data from CSV file."""
        try:
            self.places_data = pd.read_csv("data/jaipur_places.csv")
        except FileNotFoundError:
            self.places_data = pd.DataFrame()

    async def generate_itinerary(
        self, days: int, interests: Optional[str] = None, budget: Optional[str] = None
    ) -> dict:
        """
        Generate a personalized itinerary for Jaipur.

        Args:
            days: Number of days for the itinerary
            interests: User's interests (e.g., "history, culture, food")
            budget: Budget level (e.g., "low", "medium", "high")

        Returns:
            Dictionary containing the generated itinerary
        """
        # Get weather information
        weather = await self.weather_service.get_weather_forecast(days)

        # Generate itinerary using AI chain
        itinerary = await self.itinerary_chain.generate(
            days=days,
            interests=interests,
            budget=budget,
            weather=weather,
            places_data=self.places_data,
        )

        # Enhance with maps information
        itinerary = await self.maps_service.add_location_details(itinerary)

        return itinerary

    async def get_places(self) -> list:
        """
        Get list of popular places in Jaipur.

        Returns:
            List of places with details
        """
        if self.places_data is not None and not self.places_data.empty:
            return self.places_data.to_dict("records")
        return []
