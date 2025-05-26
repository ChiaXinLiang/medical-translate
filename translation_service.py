"""High-level service for managing the translation process."""
from typing import List, Dict
from config import Config
from translator import MedicalTranslator
from data_handler import DataHandler


class TranslationService:
    """Orchestrates the translation process."""
    
    def __init__(self):
        """Initialize the translation service."""
        self.translator = MedicalTranslator()
        self.data_handler = DataHandler()
    
    def translate_dataset(self, input_file: str, output_file: str):
        """
        Translate an entire dataset using all configured models.
        
        Args:
            input_file: Path to input CSV file
            output_file: Path to output CSV file
        """
        # Read input data
        rows = self.data_handler.read_input_file(input_file)
        total_rows = len(rows)
        
        print(f"Starting translation of {total_rows} questions to Japanese...")
        print(f"Using models: {', '.join(Config.MODELS.keys())}")
        
        translations = []
        
        for idx, row in enumerate(rows):
            print(f"\nProcessing row {idx + 1}/{total_rows}")
            
            # Prepare base row
            translated_row = self.data_handler.prepare_translation_row(row, idx)
            question_text = translated_row['original_question']
            
            # Skip empty questions
            if not question_text.strip():
                print(f"  Skipping empty question at row {idx + 1}")
                translations.append(translated_row)
                continue
            
            # Translate with all models
            model_translations = self.translator.translate_with_all_models(question_text)
            translated_row.update(model_translations)
            
            translations.append(translated_row)
            
            # Save progress periodically
            if (idx + 1) % Config.SAVE_INTERVAL == 0:
                self.data_handler.save_translations(translations, output_file)
                print(f"  Progress saved: {idx + 1}/{total_rows} rows completed")
        
        # Final save
        self.data_handler.save_translations(translations, output_file)
        print(f"\nTranslation completed!")
        print(f"Results saved to: {output_file}")
        
        # Print summary statistics
        self._print_summary(translations)
    
    def _print_summary(self, translations: List[Dict]):
        """Print summary statistics of the translation process."""
        total = len(translations)
        successful = {}
        
        for model_key in ['gpt-4o_japanese', 'claude-sonnet-4_japanese', 
                         'claude-opus-4_japanese', 'qwen3-235b_japanese']:
            successful[model_key] = sum(
                1 for t in translations 
                if t.get(model_key) and t[model_key] != "[Translation Failed]"
            )
        
        print("\n" + "=" * 50)
        print("Translation Summary:")
        print(f"Total rows: {total}")
        for model_key, count in successful.items():
            model_name = model_key.replace('_japanese', '')
            print(f"{model_name}: {count}/{total} successful ({count/total*100:.1f}%)")