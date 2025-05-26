"""Core translator class for handling API interactions."""
import time
import requests
from typing import Dict, List, Optional
from config import Config
from prompts import MEDICAL_SAFETY_JAPANESE


class MedicalTranslator:
    """Handles translation of medical texts using various AI models."""
    
    def __init__(self):
        """Initialize the translator with API configuration."""
        Config.validate()
        
        self.headers = {
            "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "Medical Safety Japanese Translation"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
    def translate_text(self, text: str, model_name: str) -> Optional[str]:
        """
        Translate text using specified model via OpenRouter API.
        
        Args:
            text: The text to translate
            model_name: The model to use for translation
            
        Returns:
            Translated text or None if translation failed
        """
        model_id = Config.MODELS.get(model_name)
        if not model_id:
            print(f"Unknown model: {model_name}")
            return None
        
        # Use the same prompt for all models for consistency
        prompt = MEDICAL_SAFETY_JAPANESE.format(text=text)
            
        payload = {
            "model": model_id,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": Config.TEMPERATURE,
            "max_tokens": Config.MAX_TOKENS
        }
        
        try:
            response = self.session.post(
                Config.OPENROUTER_API_URL,
                json=payload,
                timeout=Config.REQUEST_TIMEOUT
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content'].strip()
                
                # Clean up any responses that might have extra formatting
                # Remove any markdown formatting
                content = content.replace("```japanese", "").replace("```", "").replace("```ja", "")
                # If response has multiple lines, take only the first non-empty line
                lines = [line.strip() for line in content.split('\n') if line.strip()]
                if lines:
                    content = lines[0]
                
                return content
            else:
                print(f"API Error for {model_name}: {response.status_code} - {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            print(f"Timeout error for {model_name}")
            return None
        except Exception as e:
            print(f"Error translating with {model_name}: {str(e)}")
            return None
    
    def translate_with_all_models(self, text: str) -> Dict[str, str]:
        """
        Translate text with all configured models.
        
        Args:
            text: The text to translate
            
        Returns:
            Dictionary mapping model names to their translations
        """
        translations = {}
        
        for model_name in Config.MODELS.keys():
            print(f"  Translating with {model_name}...")
            translation = self.translate_text(text, model_name)
            translations[f'{model_name}_japanese'] = translation or "[Translation Failed]"
            
            # Rate limiting
            time.sleep(Config.RATE_LIMIT_DELAY)
            
        return translations