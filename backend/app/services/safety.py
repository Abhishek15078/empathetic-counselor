import re

from pathlib import Path

from app.core.crisis_keywords import (
    CRISIS_KEYWORDS,
    CRISIS_PATTERNS
)

from app.models.safety import (
    SafetyResult
)

from app.services.llm import (
    LLMCaller
)


class SafetyService:
    """
    Handles crisis detection before
    the message reaches the AI pipeline.
    """

    def __init__(self):
        """
        Load keywords, patterns,
        and LLM service once.
        """

        self.keywords = CRISIS_KEYWORDS

        self.patterns = CRISIS_PATTERNS

        self.llm = LLMCaller()

    def keyword_check(
        self,
        text: str
    ) -> bool:
        """
        Stage 1:
        Exact keyword matching.
        """

        text = text.lower()

        for keyword in self.keywords:

            if keyword in text:

                return True

        return False

    def regex_check(
        self,
        text: str
    ) -> bool:
        """
        Stage 1:
        Regex matching.
        """

        for pattern in self.patterns:

            if re.search(
                pattern,
                text,
                re.IGNORECASE
            ):

                return True

        return False

    def stage_one_detection(
        self,
        text: str
    ) -> bool:
        """
        Keyword +
        Regex detection.
        """

        if self.keyword_check(text):

            return True

        if self.regex_check(text):

            return True

        return False

    def stage_two_detection(
        self,
        text: str
    ) -> bool:
        """
        Semantic crisis detection
        using a separate LLM call.
        """

        return self.llm.classify_crisis(
            text
        )

    def load_safe_response(
        self
    ) -> str:
        """
        Loads reviewed crisis response.
        """

        path = (
            Path(__file__)
            .parent.parent
            / "prompts"
            / "safety_response.txt"
        )

        return path.read_text(
            encoding="utf-8"
        )

    def get_safe_response(
        self
    ) -> str:
        """
        Returns crisis response.
        """

        return self.load_safe_response()

    def screen(
        self,
        text: str
    ) -> SafetyResult:
        """
        Main public method.

        Every user message
        passes through here.
        """

        # -------------------
        # Stage 1
        # -------------------

        if self.stage_one_detection(
            text
        ):

            return SafetyResult(
                is_crisis=True,
                reason="keyword_or_regex"
            )

        # -------------------
        # Stage 2
        # -------------------

        if self.stage_two_detection(
            text
        ):

            return SafetyResult(
                is_crisis=True,
                reason="semantic_detection"
            )

        # -------------------
        # Safe
        # -------------------

        return SafetyResult(
            is_crisis=False,
            reason="safe"
        )