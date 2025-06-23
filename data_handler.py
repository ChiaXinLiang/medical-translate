"""Handles data input/output operations."""
import csv
import os
from typing import Dict, List
from datetime import datetime
from config import Config


class DataHandler:
    """Manages CSV file operations for translation data."""
    
    @staticmethod
    def read_input_file(input_file: str) -> List[Dict]:
        """
        Read and validate input CSV file.
        
        Args:
            input_file: Path to the input CSV file
            
        Returns:
            List of dictionaries containing row data
            
        Raises:
            FileNotFoundError: If input file doesn't exist
        """
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
            
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    @staticmethod
    def prepare_translation_row(row: Dict, idx: int) -> Dict:
        """
        Prepare a row for translation with all necessary fields.
        
        Args:
            row: Original row data
            idx: Row index
            
        Returns:
            Dictionary with prepared translation fields
        """
        question_text = row.get('harmful_medical_request', '') or row.get('question', '')
        
        return {
            'id': row.get('id', idx + 1),
            'category': row.get('category', ''),
            'original_question': question_text,
            'o1-pro_japanese': '',
            'gpt-4.5-preview_japanese': '',
            'claude-opus-4_japanese': '',
            'deepseek-r1-0528_japanese': '',
            'gemini-2.5-pro-preview_japanese': '',
            'qwen3-235b-a22b_japanese': ''
        }
    
    @staticmethod
    def save_translations(translations: List[Dict], output_file: str):
        """
        Save translations to CSV file.
        
        Args:
            translations: List of translation dictionaries
            output_file: Path to output CSV file
        """
        if not translations:
            return
            
        fieldnames = [
            'id',
            'category',
            'original_question',
            'o1-pro_japanese',
            'gpt-4.5-preview_japanese',
            'claude-opus-4_japanese',
            'deepseek-r1-0528_japanese',
            'gemini-2.5-pro-preview_japanese',
            'qwen3-235b-a22b_japanese'
        ]
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(translations)
    
    @staticmethod
    def generate_output_filename() -> str:
        """Generate timestamped output filename."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return f"{Config.OUTPUT_FILE_PREFIX}_{timestamp}.csv"