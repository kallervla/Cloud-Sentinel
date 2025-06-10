"""Emotion detection module using IBM Watson NLU."""
# pylint: disable=too-few-public-methods
import os
from typing import Dict

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

class WatsonEmotionDetector:
    """Detect emotions in text using IBM Watson Natural Language Understanding."""

    def __init__(self, api_key: str | None = None, url: str | None = None) -> None:
        self.api_key = api_key or os.getenv("WATSON_NLU_API_KEY")
        self.url = url or os.getenv("WATSON_NLU_URL")
        self.service = None
        if self.api_key and self.url:
            authenticator = IAMAuthenticator(self.api_key)
            self.service = NaturalLanguageUnderstandingV1(
                version="2022-04-07", authenticator=authenticator
            )
            self.service.set_service_url(self.url)

    def detect(self, text: str) -> Dict[str, float | str]:
        """Return the dominant emotion and score for the given text."""
        if not text or not text.strip():
            raise ValueError("Input text must not be empty")

        if self.service:
            response = self.service.analyze(
                text=text,
                features=Features(emotion=EmotionOptions()),
            ).get_result()
            emotions = response["emotion"]["document"]["emotion"]
            emotion, score = max(emotions.items(), key=lambda pair: pair[1])
            return {"emotion": emotion, "score": score}

        # Fallback simple heuristic
        lowered = text.lower()
        if "happy" in lowered or "joy" in lowered:
            return {"emotion": "joy", "score": 1.0}
        if "sad" in lowered:
            return {"emotion": "sadness", "score": 1.0}
        if "angry" in lowered or "anger" in lowered:
            return {"emotion": "anger", "score": 1.0}
        return {"emotion": "neutral", "score": 1.0}
