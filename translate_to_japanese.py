#!/usr/bin/env python3
"""
Medical Safety Japanese Translation Tool

This script translates medical safety benchmark questions to Japanese
using multiple AI models for comparison.
"""

import sys
import os

# Add the current directory to Python path to import local modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from translation_service import TranslationService
from data_handler import DataHandler


def main():
    """Main entry point for the translation tool."""
    # Configuration
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "med_safety_sample_300.csv")
    output_file = DataHandler.generate_output_filename()
    output_file = os.path.join(base_dir, output_file)
    
    # Display configuration
    print("Medical Safety Japanese Translation Tool")
    print("=" * 50)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Target language: Japanese")
    print(f"Models: {', '.join(Config.MODELS.keys())}")
    print("=" * 50)
    
    try:
        # Validate configuration
        Config.validate()
        
        # Check input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        # Confirm before starting
        response = input("\nReady to start translation? This will make API calls. (yes/no): ")
        if response.lower() != 'yes':
            print("Translation cancelled.")
            return
        
        # Create translation service and run
        service = TranslationService()
        service.translate_dataset(input_file, output_file)
        
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("\nAvailable CSV files in current directory:")
        for f in sorted(os.listdir(base_dir)):
            if f.endswith('.csv'):
                print(f"  - {f}")
    except ValueError as e:
        print(f"\nConfiguration error: {e}")
        print("Please ensure OPENROUTER_API_KEY is set in your .env file")
        print("\nExample .env file:")
        print("OPENROUTER_API_KEY=your-api-key-here")
    except KeyboardInterrupt:
        print("\n\nTranslation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()