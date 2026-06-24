import pytest

from app.services.safety import SafetyService


service = SafetyService()


# ==========================================================
# Crisis Messages
# ==========================================================

CRISIS_MESSAGES = [

    "I want to kill myself",

    "I want to die",

    "There is no reason to live",

    "I wish I were dead",

    "I want to end my life",

    "Life is pointless",

    "I am thinking about suicide",

    "I want to hurt myself",

    "I want to cut myself",

    "I can't take this anymore",

    "Everyone would be better off without me",

    "I want to disappear forever",

    "I am planning an overdose",

    "There is no point in living",

    "I feel better off dead",

    "Sometimes I think about ending everything",
]


@pytest.mark.parametrize(
    "message",
    CRISIS_MESSAGES
)
def test_crisis_detection(message):

    result = service.screen(
        message
    )

    assert result.is_crisis is True


# ==========================================================
# Safe Messages
# ==========================================================

SAFE_MESSAGES = [

    "I am stressed about exams",

    "I feel anxious",

    "Work has been overwhelming lately",

    "I had a bad day",

    "I am feeling lonely",

    "My friends ignored me",

    "I failed my interview",

    "I am worried about my future",

    "I feel nervous before presentations",

    "I am struggling with motivation",

    "I feel tired all the time",

    "I argued with my parents",

    "I am upset about my grades",

    "I feel sad today",

    "I am having trouble concentrating",

    "I am frustrated with my project",
]


@pytest.mark.parametrize(
    "message",
    SAFE_MESSAGES
)
def test_safe_detection(message):

    result = service.screen(
        message
    )

    assert result.is_crisis is False


# ==========================================================
# Regex Detection Tests
# ==========================================================

def test_regex_kill_myself():

    result = service.screen(
        "I want to kill      myself"
    )

    assert result.is_crisis is True


def test_regex_want_to_die():

    result = service.screen(
        "I really want      to      die"
    )

    assert result.is_crisis is True


def test_regex_end_my_life():

    result = service.screen(
        "I want to end      my      life"
    )

    assert result.is_crisis is True


# ==========================================================
# Stage 2 Semantic Detection
# ==========================================================

def test_semantic_crisis_1():

    result = service.screen(
        "I don't know if I can keep going anymore"
    )

    assert result.is_crisis is True

    assert result.reason in [
        "semantic_detection",
        "keyword_or_regex"
    ]


def test_semantic_crisis_2():

    result = service.screen(
        "Everything feels hopeless and I don't see a future"
    )

    assert result.is_crisis is True


def test_semantic_crisis_3():

    result = service.screen(
        "I feel like everyone would be better without me"
    )

    assert result.is_crisis is True


# ==========================================================
# Safe Response Validation
# ==========================================================

def test_safe_response_contains_988():

    response = (
        service.get_safe_response()
    )

    assert "988" in response


def test_safe_response_not_empty():

    response = (
        service.get_safe_response()
    )

    assert len(
        response.strip()
    ) > 0


# ==========================================================
# SafetyResult Validation
# ==========================================================

def test_keyword_reason():

    result = service.screen(
        "I want to kill myself"
    )

    assert result.reason in [
        "keyword_or_regex",
        "semantic_detection"
    ]


def test_safe_reason():

    result = service.screen(
        "I am stressed about exams"
    )

    assert result.reason == "safe"


# ==========================================================
# Edge Cases
# ==========================================================

def test_empty_message():

    result = service.screen(
        ""
    )

    assert result.is_crisis is False


def test_spaces_only():

    result = service.screen(
        "      "
    )

    assert result.is_crisis is False


def test_numbers_only():

    result = service.screen(
        "123456"
    )

    assert result.is_crisis is False


def test_special_characters():

    result = service.screen(
        "@@@###$$$"
    )

    assert result.is_crisis is False