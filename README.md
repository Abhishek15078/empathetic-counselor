# 🧠 Empathetic Counselor

An AI-powered empathetic counseling assistant built with **FastAPI**,
**React**, **Groq LLM**, **Hugging Face Transformers**, **ChromaDB**,
**SQLite**, and **Docker**.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![React](https://img.shields.io/badge/React-19-61DAFB)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![License](https://img.shields.io/badge/License-MIT-yellow)

------------------------------------------------------------------------

# Overview

Empathetic Counselor is a full-stack Generative AI application that
provides emotionally aware conversations. The assistant detects
emotions, maintains conversation history, retrieves supportive knowledge
using Retrieval-Augmented Generation (RAG), performs safety checks, and
generates empathetic responses using a Large Language Model.

## Key Features

-   Emotion Detection (Hugging Face Transformers)
-   Emotion Trajectory Tracking
-   Safety Detection
-   Conversation Memory
-   Retrieval-Augmented Generation (ChromaDB)
-   Groq LLM Response Generation
-   Session Summary
-   Emotion Timeline
-   Conversation Export
-   REST API (FastAPI)
-   Modern React Frontend
-   SQLite Persistence
-   Docker & Docker Compose

------------------------------------------------------------------------

# Architecture

``` text
React Frontend
      │
      ▼
 FastAPI Backend
      │
 ┌────┼─────────────┐
 │    │             │
 ▼    ▼             ▼
Safety Emotion   Memory
      │
      ▼
 Context Builder
      │
      ▼
   RAG Service
      │
      ▼
   ChromaDB
      │
      ▼
 Prompt Builder
      │
      ▼
   Groq LLM
      │
      ▼
 Assistant Response
      │
      ▼
 SQLite Database
```

# Tech Stack

## Backend

-   FastAPI
-   SQLAlchemy
-   SQLite
-   Uvicorn

## AI

-   Groq API
-   Hugging Face Transformers
-   Sentence Transformers
-   ChromaDB

## Frontend

-   React
-   Vite
-   Recharts

## DevOps

-   Docker
-   Docker Compose

# Project Structure

``` text
empathetic-counselor/
├── backend/
│   └── app/
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── repositories/
│       ├── services/
│       └── database.py
├── frontend/
│   └── src/
│       ├── components/
│       ├── hooks/
│       └── services/
├── docs/
├── docker-compose.yml
└── README.md
```

# Installation

## Clone

``` bash
git clone https://github.com/Abhishek15078/empathetic-counselor.git
cd empathetic-counselor
```

## Backend

``` bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend

``` bash
cd frontend
npm install
npm run dev
```

# Docker

``` bash
docker compose build
docker compose up
```

Frontend: `http://localhost:3000`

Backend: `http://localhost:8000`

Swagger: `http://localhost:8000/docs`

# Environment Variables

Backend:

``` env
GROQ_API_KEY=your_key
HF_TOKEN=your_token
```

Frontend:

``` env
VITE_API_BASE_URL=http://localhost:8000
```

# API Endpoints

  Method   Endpoint                     Description
  -------- ---------------------------- ----------------------
  POST     /api/session                 Create Session
  POST     /api/message                 Send Message
  GET      /api/messages/{id}           Conversation History
  GET      /api/session/{id}/summary    Session Summary
  GET      /api/session/{id}/timeline   Emotion Timeline
  GET      /api/session/{id}/export     Export Conversation

# Screenshots

Add screenshots under `docs/screenshots/`.

``` text
01_home.png
02_chat.png
03_emotion_timeline.png
04_summary.png
05_download.png
```

# Resume Highlights

-   Built a full-stack AI counseling assistant using FastAPI and React.
-   Implemented emotion detection using Hugging Face Transformers.
-   Integrated Groq LLM for empathetic response generation.
-   Developed Retrieval-Augmented Generation using ChromaDB.
-   Implemented conversation memory, safety layer, summaries, analytics,
    and export.
-   Containerized the application using Docker and Docker Compose.

# Future Improvements

-   User authentication
-   Voice conversations
-   Multilingual support
-   Cloud deployment
-   Long-term memory
-   Therapist dashboard

# License

MIT License

# Author

**Abhishek Kumar Singh**

