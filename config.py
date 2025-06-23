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
        "o1-pro": "openai/o1-pro",  
        "gpt-4.5-preview": "openai/gpt-4.5-preview",  
        "claude-opus-4": "anthropic/claude-opus-4",  
        "deepseek-r1-0528": "deepseek/deepseek-r1-0528",
        "gemini-2.5-pro-preview": "google/gemini-2.5-pro-preview",
        "qwen3-235b-a22b": "qwen/qwen3-235b-a22b"  
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