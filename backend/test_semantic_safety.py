from app.services.safety import (
    SafetyService
)

safety = SafetyService()

result = safety.screen(
    "I don't know if I can keep going anymore."
)

print(result)