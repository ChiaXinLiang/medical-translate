#!/usr/bin/env python3
"""
Simple launcher for Medical Safety Japanese Translation

This is a convenience script to run the translation with default settings.
For more options, use main.py instead.
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from translation_service import TranslationService
from data_handler import DataHandler


def main():
    """Run translation with default settings."""
    print("🔄 Medical Safety Japanese Translation")
    print("=" * 50)
    
    # Set up default paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "med_safety_sample_300.csv")
    output_file = os.path.join(base_dir, DataHandler.generate_output_filename())
    
    # Quick validation
    try:
        Config.validate()
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("\n💡 Create a .env file with:")
        print("OPENROUTER_API_KEY=your-api-key-here")
        return
    
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        print("\n💡 Available CSV files:")
        for f in sorted(os.listdir(base_dir)):
            if f.endswith('.csv'):
                print(f"   - {f}")
        return
    
    # Show what we're doing
    print(f"📁 Input:  {os.path.basename(input_file)}")
    print(f"📁 Output: {os.path.basename(output_file)}")
    print(f"🤖 Models: {', '.join(Config.MODELS.keys())}")
    print(f"🌐 Language: Japanese")
    
    # Quick start or detailed confirmation
    print("\n🚀 Ready to translate 300 medical safety questions")
    response = input("Continue? (y/n): ").lower()
    
    if response not in ['y', 'yes']:
        print("❌ Translation cancelled.")
        return
    
    try:
        # Run translation
        print("\n" + "=" * 50)
        service = TranslationService()
        service.translate_dataset(input_file, output_file)
        
        print(f"\n✅ Translation completed!")
        print(f"📄 Results saved to: {os.path.basename(output_file)}")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Translation interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 For detailed error information, use main.py instead")


if __name__ == "__main__":
    main()