# Jaipur Itinerary AI

An intelligent travel planning application that generates personalized itineraries for Jaipur, Rajasthan using AI and LangChain.

## Features

- 🤖 AI-powered itinerary generation using LangChain
- 🗺️ Integration with maps for location details and routing
- 🌤️ Weather-aware recommendations
- 📍 Semantic search for places using embeddings
- 🏛️ Comprehensive database of Jaipur attractions
- 🎯 Personalized based on interests and budget

## Project Structure

```
jaipur-itinerary-ai/
├── app/
│   ├── main.py                          # FastAPI application entry point
│   ├── routes/
│   │   └── itinerary_routes.py         # API routes for itinerary generation
│   ├── services/
│   │   ├── itinerary_service.py        # Business logic for itinerary generation
│   │   ├── maps_service.py             # Maps and location services
│   │   └── weather_service.py          # Weather forecast services
│   ├── ai/
│   │   ├── chains/
│   │   │   ├── itinerary_chain.py      # LangChain for itinerary generation
│   │   │   ├── prompt_templates.py     # Prompt templates for LLM
│   │   │   └── output_parser.py        # Parser for LLM responses
│   │   ├── embeddings/
│   │   │   └── embed_places.py         # Generate embeddings for places
│   │   └── memory/                      # Conversation memory (future)
│   └── db/
│       ├── models.py                    # SQLAlchemy models
│       └── database.py                  # Database configuration
├── data/
│   ├── jaipur_places.csv               # Places data
│   └── embeddings/                      # Stored embeddings
├── tests/
│   └── test_itinerary_chain.py         # Tests for itinerary generation
├── .env                                 # Environment variables
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vijayrajpanchall/jaipur-itinerary-ai.git
   cd jaipur-itinerary-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env` file and update with your API keys
   - Add your OpenAI API key
   - Add your Google Maps API key (optional)
   - Add your Weather API key (optional)

5. **Initialize the database**
   ```bash
   python -c "from app.db.database import init_db; init_db()"
   ```

## Usage

### Running the API Server

```bash
python app/main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example API Request

```bash
curl -X POST "http://localhost:8000/api/itinerary/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "days": 3,
    "interests": "history, culture, food",
    "budget": "medium"
  }'
```

## Testing

Run tests using pytest:

```bash
pytest tests/
```

With coverage:

```bash
pytest --cov=app tests/
```

## Development

### Code Formatting

```bash
black app/ tests/
```

### Linting

```bash
flake8 app/ tests/
```

### Type Checking

```bash
mypy app/
```

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **LangChain**: Framework for developing LLM applications
- **OpenAI**: LLM for generating itineraries
- **SQLAlchemy**: SQL toolkit and ORM
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing for embeddings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please open an issue on GitHub.