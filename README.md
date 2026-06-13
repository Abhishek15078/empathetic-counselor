
# Empathetic Counselor

An AI-powered emotional support system that combines emotion detection, emotion-aware prompting, memory, and contextual conversation management to generate empathetic responses.

---

## Project Objective

The goal of this project is to build an emotionally intelligent conversational assistant capable of:

* Detecting user emotions from text
* Estimating emotional intensity
* Identifying concerning emotional states
* Generating empathetic responses conditioned on detected emotions
* Maintaining conversational memory
* Providing emotionally aware contextual interactions

---

## Technology Stack

### Backend

* Python
* FastAPI
* Hugging Face Transformers
* Groq API
* PyTest
* Python Dataclasses
* Enums

### Frontend

* React
* Vite

---

## Project Architecture

User Message

↓

Emotion Analysis Service

↓

Emotion Result

* Emotion Label
* Confidence Score
* Intensity
* Concerning Flag
* Timestamp

↓

Prompt Builder

↓

Emotion Context Injection

↓

LLM (Llama 3.3 70B via Groq)

↓

Empathetic Response

---

## Completed Phases

### Phase 0 — Project Setup

Completed

Features:

* Project structure creation
* Virtual environment setup
* Dependency management
* Backend/frontend separation

---

### Phase 1 — Emotion Classification

Completed

Features:

* Hugging Face emotion model integration
* Emotion detection service
* Unit testing
* Confidence score extraction

Model:

j-hartmann/emotion-english-distilroberta-base

---

### Phase 2 — Emotion Analysis Service

Completed

Features:

* EmotionLabel Enum
* IntensityLevel Enum
* EmotionResult Dataclass
* Concerning emotion detection
* Intensity mapping
* Structured emotion output

---

### Phase 3 — Empathetic Response Generation

Completed

Features:

* Groq LLM integration
* Prompt engineering
* Emotion-conditioned prompting
* Response formatter
* System prompts
* Prompt experiment notebook

Experiment:

The same user message was evaluated under anxiety, sadness, and neutral emotional contexts. Different responses were generated for each emotion, demonstrating successful emotion-conditioned prompting.

---

## Testing

Run:

pytest -v

Expected:

20+ tests passing

---

## Future Phases

* Phase 4 — Memory Layer
* Phase 5 — Safety Layer
* Phase 6 — Conversation Manager
* Phase 7 — Context Builder
* Phase 8 — Full System Integration

---

## Author

Abhishek Kumar Singh
