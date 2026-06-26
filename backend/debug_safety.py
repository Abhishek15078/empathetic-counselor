# debug_safety.py

from app.services.safety import SafetyService

service = SafetyService()

message = "I feel very sad today"

result = service.screen(message)

print("Message:", message)
print("Crisis:", result.is_crisis)
print("Reason:", result.reason)