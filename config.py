"""Configuration settings for the translation application."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration."""
    
    # API Settings
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
    
    # Model configurations - Using the latest flagship models (2025)
    MODELS = {
        "gpt-4o": "openai/gpt-4o",  # Latest GPT-4o model
        "claude-sonnet-4": "anthropic/claude-sonnet-4",  # Claude 3.5 Sonnet
        "claude-opus-4": "anthropic/claude-opus-4",  # Claude 3 Opus - most capable
        "gemini-2.5-pro": "google/gemini-2.5-pro-preview"  # Gemini 2.5 Pro - large context
    }
    
    # Translation settings
    TEMPERATURE = 0.3
    MAX_TOKENS = 1000
    RATE_LIMIT_DELAY = 1  # seconds between API calls
    SAVE_INTERVAL = 10  # rows between progress saves
    REQUEST_TIMEOUT = 30  # seconds
    
    # File settings
    DEFAULT_INPUT_FILE = "med_safety_sample_300.csv"
    OUTPUT_FILE_PREFIX = "japanese_translations"
    
    @classmethod
    def validate(cls):
        """Validate required configuration."""
        if not cls.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")