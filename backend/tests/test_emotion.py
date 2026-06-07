import pytest

from app.services.emotion import EmotionClassifier
from app.models.emotion import (
    EmotionLabel,
    EmotionResult
)


@pytest.fixture(scope="session")
def classifier():
    """
    Load model only once.
    """
    return EmotionClassifier()


def test_joy(classifier):
    result = classifier.classify(
        "I had a wonderful day"
    )

    assert isinstance(
        result,
        EmotionResult
    )

    assert result.label == EmotionLabel.JOY
    assert result.score > 0.5


def test_fear(classifier):
    result = classifier.classify(
        "I am so anxious about my exams"
    )

    assert result.label in [
        EmotionLabel.FEAR,
        EmotionLabel.SADNESS
    ]

    assert result.score > 0.5


def test_empty_string(classifier):
    result = classifier.classify("")

    assert result.label == EmotionLabel.NEUTRAL
    assert result.score == 0.0


def test_spaces_only(classifier):
    result = classifier.classify("     ")

    assert result.label == EmotionLabel.NEUTRAL


def test_sadness(classifier):
    result = classifier.classify(
        "I feel deeply sad today"
    )

    assert result.label == EmotionLabel.SADNESS


def test_anger(classifier):
    result = classifier.classify(
        "I am furious and angry"
    )

    assert result.label == EmotionLabel.ANGER


def test_surprise(classifier):
    result = classifier.classify(
        "I cannot believe this happened"
    )

    assert result.label in [
        EmotionLabel.SURPRISE,
        EmotionLabel.JOY
    ]


def test_score_range(classifier):
    result = classifier.classify(
        "I feel sad"
    )

    assert 0.0 <= result.score <= 1.0


def test_numbers(classifier):
    result = classifier.classify(
        "123456789"
    )

    assert result.label is not None
    assert result.score >= 0.0


def test_special_characters(classifier):
    result = classifier.classify(
        "!@#$%^&*()"
    )

    assert result.label is not None
    assert result.score >= 0.0


def test_emoji_input(classifier):
    result = classifier.classify(
        "😊😊😊"
    )

    assert result.label is not None
    assert result.score >= 0.0


def test_newline_input(classifier):
    result = classifier.classify(
        "Hello\nWorld"
    )

    assert result.label is not None
    assert result.score >= 0.0


def test_mixed_emotions(classifier):
    result = classifier.classify(
        "I am happy but nervous"
    )

    assert result.score > 0.0


def test_long_input(classifier):
    text = "anxiety " * 10000

    result = classifier.classify(text)

    assert result.label is not None
    assert result.score >= 0.0


def test_large_paragraph(classifier):
    text = """
    I have been feeling stressed about my exams.
    At the same time I am hopeful about my future.
    Sometimes I feel nervous and overwhelmed.
    """

    result = classifier.classify(text)

    assert result.label is not None
    assert result.score >= 0.0