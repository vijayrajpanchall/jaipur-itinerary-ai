"""
Prompt templates for itinerary generation.
"""

ITINERARY_PROMPT_TEMPLATE = """
You are an expert travel guide for Jaipur, Rajasthan, India. Create a personalized \
{days}-day itinerary based on the following preferences:

User Interests: {interests}
Budget Level: {budget}

Available Places in Jaipur:
{places}

Weather Forecast:
{weather}

Please generate a detailed day-by-day itinerary that includes:
1. Recommended places to visit each day
2. Best times to visit each location
3. Estimated time needed at each place
4. Travel time between locations
5. Meal recommendations
6. Budget-friendly tips if applicable
7. Weather-appropriate activities

Format the itinerary clearly with day numbers and time slots.
"""

PLACE_RECOMMENDATION_PROMPT = """
Based on the user's interest in {interest}, recommend the best places to visit in Jaipur.
Consider the following factors:
- Relevance to the interest
- Time of year and weather
- Accessibility
- Budget constraints: {budget}

Available places:
{places}

Provide your top recommendations with reasons.
"""

OPTIMIZATION_PROMPT = """
Optimize the following itinerary to minimize travel time and maximize enjoyment:

Current Itinerary:
{current_itinerary}

Weather Conditions:
{weather}

Suggest improvements considering:
1. Geographical proximity of places
2. Opening/closing times
3. Weather conditions
4. Peak tourist hours
5. Logical flow of activities

Provide an optimized version.
"""
