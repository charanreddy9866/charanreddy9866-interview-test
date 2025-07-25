# template/test_tags_model.py

import pytest
from tags_model import extract_tags

def test_extract_tags_with_mock(monkeypatch):
    """
    Test the extract_tags function using a mocked OpenAI response.
    """
    def mock_chat_completion_create(*args, **kwargs):
        class MockChoice:
            message = {"content": '{"tags": ["growth", "confidence"]}'}
        return type("obj", (object,), {"choices": [MockChoice()]})

    import openai
    monkeypatch.setattr(openai.ChatCompletion, "create", mock_chat_completion_create)

    transcript = "I finally spoke up in the team meeting and shared a new idea. It felt empowering."
    tags = extract_tags(transcript)
    assert "growth" in tags
    assert "confidence" in tags

def test_extract_tags_with_empty_tags(monkeypatch):
    """
    Ensure that empty responses are handled correctly.
    """
    def mock_chat_completion_create(*args, **kwargs):
        class MockChoice:
            message = {"content": '{"tags": []}'}
        return type("obj", (object,), {"choices": [MockChoice()]})

    import openai
    monkeypatch.setattr(openai.ChatCompletion, "create", mock_chat_completion_create)

    transcript = "Random sentence with no relevant content."
    tags = extract_tags(transcript)
    assert tags == []
