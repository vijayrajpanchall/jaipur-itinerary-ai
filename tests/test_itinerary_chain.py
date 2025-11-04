"""
Tests for the itinerary chain functionality.
"""
import pytest
import pandas as pd
from app.ai.chains.itinerary_chain import ItineraryChain
from app.ai.chains.output_parser import ItineraryOutputParser


@pytest.fixture
def itinerary_chain():
    """Fixture to create an ItineraryChain instance."""
    return ItineraryChain()


@pytest.fixture
def output_parser():
    """Fixture to create an ItineraryOutputParser instance."""
    return ItineraryOutputParser()


@pytest.fixture
def sample_places_data():
    """Fixture to create sample places data."""
    return pd.DataFrame([
        {
            "name": "Amber Fort",
            "description": "A magnificent hilltop fortress",
            "category": "Historical Monument"
        },
        {
            "name": "Hawa Mahal",
            "description": "The iconic Palace of Winds",
            "category": "Historical Monument"
        },
        {
            "name": "City Palace",
            "description": "A grand palace complex",
            "category": "Palace"
        }
    ])


@pytest.mark.asyncio
async def test_generate_itinerary_basic(itinerary_chain):
    """Test basic itinerary generation."""
    result = await itinerary_chain.generate(
        days=3,
        interests="history, culture",
        budget="medium"
    )
    
    assert result is not None
    assert "daily_plans" in result
    assert len(result["daily_plans"]) == 3
    assert result["days"] == 3


@pytest.mark.asyncio
async def test_generate_itinerary_with_places(itinerary_chain, sample_places_data):
    """Test itinerary generation with places data."""
    result = await itinerary_chain.generate(
        days=2,
        interests="architecture",
        budget="high",
        places_data=sample_places_data
    )
    
    assert result is not None
    assert "daily_plans" in result
    assert len(result["daily_plans"]) == 2


@pytest.mark.asyncio
async def test_generate_itinerary_with_weather(itinerary_chain):
    """Test itinerary generation with weather data."""
    weather = [
        {"date": "2024-01-01", "condition": "Sunny", "temperature_high": 25},
        {"date": "2024-01-02", "condition": "Cloudy", "temperature_high": 22}
    ]
    
    result = await itinerary_chain.generate(
        days=2,
        interests="outdoor activities",
        weather=weather
    )
    
    assert result is not None
    assert "daily_plans" in result


def test_output_parser_json(output_parser):
    """Test parsing JSON output."""
    json_output = '{"daily_plans": [{"day": 1, "activities": []}]}'
    result = output_parser.parse(json_output)
    
    assert result is not None
    assert "daily_plans" in result


def test_output_parser_text(output_parser):
    """Test parsing text output."""
    text_output = """
    Day 1
    9:00 AM - Visit Amber Fort
    2:00 PM - Explore City Palace
    
    Day 2
    10:00 AM - See Hawa Mahal
    3:00 PM - Visit Jantar Mantar
    """
    
    result = output_parser.parse(text_output)
    
    assert result is not None
    assert "daily_plans" in result
    assert len(result["daily_plans"]) >= 1


def test_output_parser_validation(output_parser):
    """Test validation of parsed output."""
    valid_output = {
        "daily_plans": [
            {"day": 1, "activities": []},
            {"day": 2, "activities": []}
        ]
    }
    
    assert output_parser.validate(valid_output) is True
    
    invalid_output = {"days": 3}
    assert output_parser.validate(invalid_output) is False


def test_prepare_context(itinerary_chain, sample_places_data):
    """Test context preparation for prompts."""
    context = itinerary_chain._prepare_context(
        days=3,
        interests="history",
        budget="medium",
        weather=None,
        places_data=sample_places_data
    )
    
    assert "days" in context
    assert context["days"] == 3
    assert "interests" in context
    assert "budget" in context
    assert "places" in context


@pytest.mark.asyncio
async def test_generate_itinerary_edge_cases(itinerary_chain):
    """Test itinerary generation with edge cases."""
    # Test with 1 day
    result = await itinerary_chain.generate(days=1)
    assert result is not None
    assert len(result["daily_plans"]) == 1
    
    # Test with no interests
    result = await itinerary_chain.generate(days=2, interests=None)
    assert result is not None
    
    # Test with no budget
    result = await itinerary_chain.generate(days=2, budget=None)
    assert result is not None
