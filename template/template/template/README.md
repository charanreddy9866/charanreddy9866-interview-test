# Tag Extraction Module – Sentari AI

This module extracts relevant tags from transcribed text using OpenAI's Chat Completion API.

## Tags Detected
- emotion_score
- growth
- family
- gratitude
- stress
- goals
- health
- relationships
- confidence
- conflict

## Files
- `tags_model.py`: Core extraction logic
- `test_tags_model.py`: Unit tests using mock OpenAI response

## How to Run
1. Export your OpenAI key:
   ```bash
   export OPENAI_API_KEY=your-key-here
