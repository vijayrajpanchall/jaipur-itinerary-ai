"""
Itinerary chain for generating personalized itineraries using LangChain.
"""
from typing import Optional, Dict, Any
import pandas as pd
from app.ai.chains.prompt_templates import ITINERARY_PROMPT_TEMPLATE  # noqa: F401
from app.ai.chains.output_parser import ItineraryOutputParser


class ItineraryChain:
    def __init__(self):
        self.output_parser = ItineraryOutputParser()
        self.llm = None  # Will be initialized with actual LLM (e.g., OpenAI)

    async def generate(
        self,
        days: int,
        interests: Optional[str] = None,
        budget: Optional[str] = None,
        weather: Optional[list] = None,
        places_data: Optional[pd.DataFrame] = None,
    ) -> Dict[str, Any]:
        """
        Generate an itinerary using the LLM chain.

        Args:
            days: Number of days for the itinerary
            interests: User's interests
            budget: Budget level
            weather: Weather forecast data
            places_data: DataFrame containing places information

        Returns:
            Dictionary containing the generated itinerary
        """
        # Prepare context
        # context = self._prepare_context(
        #     days=days, interests=interests, budget=budget, weather=weather,
        #     places_data=places_data
        # )
        # Generate prompt
        # prompt = ITINERARY_PROMPT_TEMPLATE.format(**context)
        # TODO: Use the prompt to call the LLM in production

        # For now, return a placeholder itinerary
        # In production, this would call the LLM
        itinerary = self._generate_placeholder_itinerary(days, interests, budget)

        return itinerary

    def _prepare_context(
        self,
        days: int,
        interests: Optional[str],
        budget: Optional[str],
        weather: Optional[list],
        places_data: Optional[pd.DataFrame],
    ) -> Dict[str, Any]:
        """Prepare context for the prompt template."""
        places_list = ""
        if places_data is not None and not places_data.empty:
            places_list = "\n".join(
                [
                    f"- {row.get('name', 'Unknown')}: {row.get('description', '')}"
                    for _, row in places_data.head(10).iterrows()
                ]
            )

        weather_info = ""
        if weather:
            weather_info = "\n".join(
                [
                    f"Day {i+1}: {w.get('condition', 'Unknown')}, "
                    f"{w.get('temperature_high', 'N/A')}°C"
                    for i, w in enumerate(weather)
                ]
            )

        return {
            "days": days,
            "interests": interests or "general sightseeing",
            "budget": budget or "medium",
            "places": places_list,
            "weather": weather_info,
        }

    def _generate_placeholder_itinerary(
        self, days: int, interests: Optional[str], budget: Optional[str]
    ) -> Dict[str, Any]:
        """Generate a placeholder itinerary for testing."""
        itinerary = {"days": days, "interests": interests, "budget": budget, "daily_plans": []}

        for day in range(1, days + 1):
            itinerary["daily_plans"].append(
                {
                    "day": day,
                    "activities": [
                        {
                            "time": "09:00 AM",
                            "place": f"Place {day}-1",
                            "description": "Sample activity description",
                        },
                        {
                            "time": "02:00 PM",
                            "place": f"Place {day}-2",
                            "description": "Sample activity description",
                        },
                    ],
                }
            )

        return itinerary
