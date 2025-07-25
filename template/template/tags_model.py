# template/tags_model.py

import openai
import os
import json
from typing import List

# Make sure to set this in your environment before running
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined tags to detect
TAGS = [
    "emotion_score", "growth", "family", "gratitude",
    "stress", "goals", "health", "relationships", "confidence", "conflict"
]

# Instruction to the model
SYSTEM_PROMPT = """
You are an intelligent assistant that extracts meaningful **tags** from human conversation transcripts. 
From the transcript provided, return relevant tags ONLY from this predefined list:

["emotion_score", "growth", "family", "gratitude", "stress", "goals", "health", "relationships", "confidence", "conflict"]

Respond ONLY with JSON in the format: {"tags": ["tag1", "tag2", ...]}.
If no tags apply, return: {"tags": []}
"""

def extract_tags(transcript: str, model="gpt-3.5-turbo") -> List[str]:
    """
    Extracts tags from a transcript using OpenAI ChatCompletion API.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": transcript}
            ],
            temperature=0
        )
        output = response.choices[0].message["content"]
        parsed = json.loads(output)
        return parsed.get("tags", [])
    except Exception as e:
        print("Error during tag extraction:", e)
        return []
