from app.models.emotion import (
    EmotionLabel,
    IntensityLevel
)

from app.services.emotion import (
    EmotionClassifier
)


def test_low_intensity():

    classifier = EmotionClassifier()

    assert (
        classifier._get_intensity(0.20)
        == IntensityLevel.LOW
    )


def test_medium_intensity():

    classifier = EmotionClassifier()

    assert (
        classifier._get_intensity(0.50)
        == IntensityLevel.MEDIUM
    )


def test_high_intensity():

    classifier = EmotionClassifier()

    assert (
        classifier._get_intensity(0.90)
        == IntensityLevel.HIGH
    )


def test_concerning_sadness():

    classifier = EmotionClassifier()

    assert (
        classifier._is_concerning(
            EmotionLabel.SADNESS,
            0.90
        )
        is True
    )


def test_non_concerning_joy():

    classifier = EmotionClassifier()

    assert (
        classifier._is_concerning(
            EmotionLabel.JOY,
            0.99
        )
        is False
    )