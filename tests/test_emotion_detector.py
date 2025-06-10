import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from emotion_detection.detector import WatsonEmotionDetector
import pytest


def test_detect_joy():
    detector = WatsonEmotionDetector()
    result = detector.detect("I am very happy today!")
    assert result["emotion"] == "joy"


def test_invalid_input():
    detector = WatsonEmotionDetector()
    with pytest.raises(ValueError):
        detector.detect("")
