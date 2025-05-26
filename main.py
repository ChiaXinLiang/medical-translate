"""Main entry point for the medical translation application."""
import os
import sys
import argparse
from pathlib import Path
from config import Config
from data_handler import DataHandler
from translation_service import TranslationService


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Translate medical safety questions to Japanese using multiple AI models"
    )
    
    parser.add_argument(
        "-i", "--input",
        type=str,
        default=Config.DEFAULT_INPUT_FILE,
        help="Input CSV file path (default: med_safety_sample_300.csv)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output CSV file path (default: auto-generated with timestamp)"
    )
    
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Skip confirmation prompt"
    )
    
    return parser.parse_args()


def main():
    """Main entry point for the translation tool."""
    args = parse_arguments()
    
    # Set up file paths
    base_dir = Path(__file__).parent
    input_file = base_dir / args.input
    output_file = args.output or DataHandler.generate_output_filename()
    
    if not args.output:
        output_file = base_dir / output_file
    
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
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        # Confirm before starting (unless -y flag is used)
        if not args.yes:
            response = input("\nReady to start translation? This will make API calls. (yes/no): ")
            if response.lower() != 'yes':
                print("Translation cancelled.")
                return
        
        # Create translation service and run
        service = TranslationService()
        service.translate_dataset(str(input_file), str(output_file))
        
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("\nAvailable files in current directory:")
        for f in sorted(base_dir.glob("*.csv")):
            print(f"  - {f.name}")
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