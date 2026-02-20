from .main import app, db_dependency
from fastapi import HTTPException

"""
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
"""


@app.post("/sessions", status_code="")
def create_study_session(db: db_dependency):
    pass