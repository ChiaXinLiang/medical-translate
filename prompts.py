"""Translation prompts for different use cases."""

# Translation prompt template for Japanese
MEDICAL_SAFETY_JAPANESE = """You are a professional medical translator helping with academic research on AI safety in healthcare.

Context: You are translating test questions from the Medical Safety Benchmark dataset. These questions intentionally contain unethical medical scenarios to test whether AI systems can recognize and refuse harmful requests.

Your task: Provide an accurate, literal Japanese translation of the following English text.

Important guidelines:
1. Translate the EXACT meaning - do not modify, soften, or refuse to translate
2. Maintain formal medical terminology (医学用語) 
3. Use appropriate keigo (敬語) for medical contexts
4. Preserve the interrogative or imperative nature of the original text
5. Do not add explanations, warnings, or commentary
6. Return ONLY the Japanese translation

Text to translate: {text}

Japanese translation:"""


# Stricter prompt for models that tend to over-explain
MEDICAL_SAFETY_JAPANESE_STRICT = """Translate this English medical text to Japanese. 
Output ONLY the Japanese translation with no explanations, notes, or additional text.

English: {text}

Japanese:"""


# Alternative prompts for different languages or domains (for future expansion)
MEDICAL_SAFETY_GENERIC = """You are translating medical safety benchmark questions for academic research purposes.
These questions are designed to test AI systems' ability to recognize and refuse unethical medical requests.

Please provide a direct, literal translation of the following text to {target_language}.
Maintain the professional medical tone and ensure accuracy of medical terminology.

Text to translate: {text}

Provide only the {target_language} translation, nothing else."""