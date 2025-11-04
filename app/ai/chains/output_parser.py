"""
Output parser for structured itinerary data from LLM responses.
"""
from typing import Dict, Any, List
import re
import json


class ItineraryOutputParser:
    def parse(self, llm_output: str) -> Dict[str, Any]:
        """
        Parse LLM output into structured itinerary format.
        
        Args:
            llm_output: Raw text output from the LLM
        
        Returns:
            Structured dictionary containing the itinerary
        """
        try:
            # Try to parse as JSON first
            if llm_output.strip().startswith('{'):
                return json.loads(llm_output)
        except json.JSONDecodeError:
            pass
        
        # Parse text-based output
        return self._parse_text_output(llm_output)
    
    def _parse_text_output(self, text: str) -> Dict[str, Any]:
        """Parse text-based itinerary output."""
        itinerary = {
            "daily_plans": []
        }
        
        # Split by days
        day_pattern = r"Day (\d+)"
        days = re.split(day_pattern, text)
        
        for i in range(1, len(days), 2):
            if i + 1 < len(days):
                day_num = int(days[i])
                day_content = days[i + 1]
                
                activities = self._extract_activities(day_content)
                
                itinerary["daily_plans"].append({
                    "day": day_num,
                    "activities": activities
                })
        
        return itinerary
    
    def _extract_activities(self, day_content: str) -> List[Dict[str, Any]]:
        """Extract activities from a day's content."""
        activities = []
        
        # Look for time patterns like "9:00 AM", "2:30 PM", etc.
        time_pattern = r"(\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?)"
        lines = day_content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            time_match = re.search(time_pattern, line)
            if time_match:
                time = time_match.group(1)
                description = line.replace(time, '').strip(' :-–—')
                
                activities.append({
                    "time": time,
                    "description": description
                })
        
        return activities
    
    def validate(self, parsed_output: Dict[str, Any]) -> bool:
        """
        Validate the parsed itinerary structure.
        
        Args:
            parsed_output: Parsed itinerary dictionary
        
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(parsed_output, dict):
            return False
        
        if "daily_plans" not in parsed_output:
            return False
        
        if not isinstance(parsed_output["daily_plans"], list):
            return False
        
        for day_plan in parsed_output["daily_plans"]:
            if not isinstance(day_plan, dict):
                return False
            if "day" not in day_plan or "activities" not in day_plan:
                return False
        
        return True
