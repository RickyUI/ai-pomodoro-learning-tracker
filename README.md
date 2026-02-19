# AI Pomodoro Learning Tracker API

## Overview

AI Pomodoro Learning Tracker is a FastAPI backend application that allows users to log study sessions, generate AI-powered summaries, analyze weekly progress, and retrieve learning statistics.

This project is designed as a clean MVP demonstrating:

* RESTful API design with FastAPI
* SQLite database integration
* Layered architecture (routers, services, CRUD)
* AI integration as an internal service
* Basic analytics and time-based filtering

No authentication is included in this version.

---

## Features

### Study Sessions

* Create study sessions
* Retrieve all sessions
* Retrieve a session by ID
* Automatically generate AI summary per session

### Weekly Review

* Generate AI-powered weekly learning analysis
* Detect patterns
* Provide recommendations

### Statistics

* Total sessions
* Total minutes studied
* Average session duration
* Most frequent topic

---

## Tech Stack

* Python 3.10+
* FastAPI
* SQLite3
* SQLAlchemy
* Pydantic
* OpenAI (or compatible LLM provider)
* Uvicorn

Optional:

* Streamlit (frontend integration)

---

## Project Structure

```
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── routers/
│   ├── sessions.py
│   ├── review.py
│   └── stats.py
│
├── services/
│   └── ai_service.py
│
└── crud/
    └── session_crud.py
```

### Architecture Principles

* Routers: Handle HTTP layer only
* CRUD layer: Database operations
* Services: Business logic and AI integration
* Models: SQLAlchemy database models
* Schemas: Pydantic validation models

AI logic is implemented as an internal service and never exposed as a direct HTTP endpoint.

---

## Database Schema

### Table: study_sessions

| Field            | Type     | Description          |
| ---------------- | -------- | -------------------- |
| id               | Integer  | Primary Key          |
| topic            | String   | Study topic          |
| duration_minutes | Integer  | Duration in minutes  |
| notes            | Text     | User notes           |
| ai_summary       | Text     | AI-generated summary |
| created_at       | DateTime | Timestamp            |

---

## API Endpoints

### Sessions

#### POST /sessions

Create a new study session.

Request body:

```
{
  "topic": "FastAPI",
  "duration_minutes": 25,
  "notes": "Studied dependency injection and routers."
}
```

Behavior:

* Stores session in database
* Calls AI service
* Generates summary
* Updates session with AI summary
* Returns complete session

---

#### GET /sessions

Retrieve all study sessions.

---

#### GET /sessions/{id}

Retrieve a single study session by ID.

---

### Weekly Review

#### POST /weekly-review

Generates AI analysis for sessions created within the last 7 days.

Response example:

```
{
  "weekly_summary": "...",
  "patterns": "...",
  "recommendations": "..."
}
```

The weekly review is not stored in the database (MVP scope).

---

### Statistics

#### GET /stats

Returns computed statistics:

```
{
  "total_sessions": 12,
  "total_minutes": 320,
  "average_duration": 26.6,
  "most_frequent_topic": "FastAPI"
}
```

Statistics are calculated dynamically using stored session data.

---

## AI Integration

AI functionality is implemented in:

```
services/ai_service.py
```

Two core functions:

* generate_session_summary(...)
* generate_weekly_review(...)

The AI service is called internally by routers after database operations.

There are no public AI endpoints.

---

## Installation

### 1. Clone repository

```
git clone https://github.com/yourusername/ai-pomodoro-tracker.git
cd ai-pomodoro-tracker
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run Application

```
uvicorn app.main:app --reload
```

API documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## Development Roadmap

* Add authentication (JWT)
* Add user model
* Store weekly reviews
* Add advanced analytics
* Add dashboard frontend
* Deploy with Docker

---

## Learning Goals Demonstrated

* REST API design
* Clean architecture separation
* SQLite relational modeling
* Date filtering and time logic
* AI service abstraction
* Basic analytics computation

---

## License

MIT License