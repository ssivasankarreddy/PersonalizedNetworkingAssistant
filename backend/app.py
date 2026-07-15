from fastapi import FastAPI
from pydantic import BaseModel

from services.theme_extractor import extract_themes
from services.generator import generate_conversation
from services.wiki import get_fact

from backend.database import engine, SessionLocal
from backend.models import History
from backend.models import Feedback


# Create database tables
from backend.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered Networking Assistant API",
    version="1.0.0"
)


# ==========================
# Request Models
# ==========================

class EventRequest(BaseModel):
    event: str


class ConversationRequest(BaseModel):
    event: str
    interest: str
    
    
class FeedbackRequest(BaseModel):
    history_id: int
    rating: str


# ==========================
# Home API
# ==========================

@app.get("/")
def home():
    return {"message": "Backend Running"}


# ==========================
# Theme Extraction API
# ==========================

@app.post("/extract-theme")
def extract_theme(request: EventRequest):
    themes = extract_themes(request.event)

    return {
        "themes": themes
    }


# ==========================
# Conversation Generator API
# ==========================

@app.post("/generate")
def generate(request: ConversationRequest):

    try:
        conversations = generate_conversation(
            request.event,
            request.interest
        )

        db = SessionLocal()

        history = History(
            event=request.event,
            interest=request.interest,
            response="\n".join(conversations)
        )

        db.add(history)
        db.commit()
        db.close()

        return {
            "conversation": conversations
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# ==========================
# Wikipedia Fact Checker API
# ==========================

@app.get("/fact")
def fact(topic: str):

    summary = get_fact(topic)

    return {
        "topic": topic,
        "summary": summary
    }


# ==========================
# History API
# ==========================

@app.get("/history")
def history():

    db = SessionLocal()

    records = db.query(History).all()

    result = []

    for item in records:
        result.append({
            "id": item.id,
            "event": item.event,
            "interest": item.interest,
            "response": item.response,
            "created_at": item.created_at
        })

    db.close()

    return result

@app.post("/feedback")
def feedback(request: FeedbackRequest):

    db = SessionLocal()

    fb = Feedback(
        history_id=request.history_id,
        rating=request.rating
    )

    db.add(fb)
    db.commit()
    db.close()

    return {
        "message": "Feedback saved successfully."
    }