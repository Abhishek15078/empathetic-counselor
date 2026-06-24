from dataclasses import dataclass


@dataclass
class SafetyResult:

    is_crisis: bool

    reason: str