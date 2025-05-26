# Medical Safety Benchmark Japanese Translation

A comprehensive tool for translating medical safety benchmark questions from English to Japanese using multiple state-of-the-art language models through the OpenRouter API.

## 🎯 Overview

This project translates the [med-safety-bench](https://github.com/AI4LIFE-GROUP/med-safety-bench) dataset questions into Japanese using multiple AI models for comparison and research purposes. The questions are designed to test AI systems' ability to recognize and refuse unethical medical requests.

## 🏗️ Project Structure

```
medical-translate/
├── main.py                     # Full-featured CLI with arguments
├── run_translation.py          # Simple one-command launcher
├── translate_to_japanese.py    # Standard translation script
├── config.py                   # Configuration settings
├── translator.py               # Core translation logic
├── data_handler.py             # CSV file operations
├── translation_service.py      # High-level translation orchestration
├── prompts.py                  # Translation prompt templates
├── sample_med_safety_data.py   # Script to create sample dataset
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .gitignore                  # Git ignore patterns
└── README.md                   # This file
```

## ✨ Features

- **Multiple AI Models**: Compare translations from GPT-4o, Claude Sonnet-4, Claude Opus-4, and Gemini 2.5 Pro
- **Consistent Prompting**: All models use the same prompt for fair comparison
- **Progress Tracking**: Automatic progress saving every 10 rows
- **Error Handling**: Robust error handling with retry mechanisms
- **Summary Statistics**: Translation success rates per model
- **Multiple Interfaces**: Choose from simple launcher, standard script, or full CLI
- **Clean Output**: Automatic cleanup of markdown formatting and explanations

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ChiaXinLiang/medical-translate.git
cd medical-translate
```

### 2. Set Up Environment
```bash
# Create virtual environment
uv venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file:
```bash
echo "OPENROUTER_API_KEY=your-api-key-here" > .env
```

### 4. Download Dataset
```bash
git clone https://github.com/AI4LIFE-GROUP/med-safety-bench.git
python sample_med_safety_data.py
```

### 5. Run Translation

#### 🎯 **Super Simple** (Recommended):
```bash
python run_translation.py
```
- One-letter confirmation (y/n)
- Emoji indicators
- Auto-detects files

#### 📋 **Standard**:
```bash
python translate_to_japanese.py
```
- Standard interface
- Full confirmation

#### ⚙️ **Advanced CLI**:
```bash
# Basic usage
python main.py

# Custom files
python main.py -i custom_input.csv -o custom_output.csv

# Skip confirmation
python main.py -y

# Help
python main.py -h
```

## 🤖 Models Used

| Model | Provider | Version | Strengths |
|-------|----------|---------|-----------|
| GPT-4o | OpenAI | Latest | Most balanced, excellent for translations |
| Claude Sonnet-4 | Anthropic | Latest | Best reasoning and context handling |
| Claude Opus-4 | Anthropic | Latest | Most capable, complex reasoning |
| Gemini 2.5 Pro | Google | Preview | Large context window, multimodal |

## 📊 Output Format

The translation generates a CSV file with columns:
- `id`: Question number
- `category`: Medical category (1-9)
- `original_question`: English question
- `gpt-4o_japanese`: Japanese translation by GPT-4o
- `claude-sonnet-4_japanese`: Japanese translation by Claude Sonnet-4
- `claude-opus-4_japanese`: Japanese translation by Claude Opus-4
- `gemini-2.5-pro_japanese`: Japanese translation by Gemini 2.5 Pro

## 🏥 Medical Categories

The dataset includes 9 medical safety categories:
1. Professional misconduct and patient harm
2. Unethical medical procedures
3. Misleading medical information
4. Privacy violations
5. Dangerous medical advice
6. Experimental procedures without consent
7. Substance abuse and illegal prescriptions
8. Medical fraud
9. Emergency care negligence

## ⚙️ Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)

### Customizable Settings (config.py)
- Model selection and API endpoints
- Translation parameters (temperature, max tokens)
- Rate limiting and timeout settings
- File paths and output formats

## 🔧 Advanced Usage

### Custom Models
Edit `config.py` to add or modify models:
```python
MODELS = {
    "custom-model": "provider/model-name",
    # ... other models
}
```

### Custom Prompts
Modify `prompts.py` to adjust translation instructions:
```python
MEDICAL_SAFETY_JAPANESE = """Your custom prompt here..."""
```

### Batch Processing
```python
from translation_service import TranslationService

service = TranslationService()
service.translate_dataset("input.csv", "output.csv")
```

## 📈 Performance

- **Rate Limiting**: 1-second delay between API calls
- **Progress Saving**: Every 10 rows to prevent data loss
- **Error Recovery**: Automatic retry mechanisms
- **Memory Efficient**: Streaming CSV processing

## 🛡️ Security

- API keys stored in `.env` file (not committed to git)
- Comprehensive `.gitignore` for sensitive files
- No API keys in code or logs
- Secure session management

## 🔍 Troubleshooting

### Common Issues

**API Key Not Found**
```bash
Configuration error: OPENROUTER_API_KEY not found
```
→ Create `.env` file with your API key

**Input File Missing**
```bash
Input file not found: med_safety_sample_300.csv
```
→ Run `python sample_med_safety_data.py` first

**Translation Failures**
- Check API key validity
- Verify model availability on OpenRouter
- Check network connection

### Debugging
For detailed error information, use:
```bash
python main.py  # Shows full stack traces
```

## 📝 Dependencies

- `requests>=2.31.0` - HTTP requests
- `pandas>=2.0.0` - Data manipulation (optional)
- `python-dotenv>=1.0.0` - Environment variable loading

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project uses the med-safety-bench dataset. Please refer to the original repository for licensing information.

## 🙏 Acknowledgments

- [AI4LIFE-GROUP/med-safety-bench](https://github.com/AI4LIFE-GROUP/med-safety-bench) for the dataset
- [OpenRouter](https://openrouter.ai/) for API access to multiple models
- Contributors and maintainers

## 📞 Support

- **Issues**: Report bugs via [GitHub Issues](https://github.com/ChiaXinLiang/medical-translate/issues)
- **Discussions**: Ask questions in [GitHub Discussions](https://github.com/ChiaXinLiang/medical-translate/discussions)
- **Email**: Contact the maintainers for urgent issues

---

Made with ❤️ for medical AI safety research