from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict
from datetime import datetime

from schemas import Contact, ContactResponse
from database import db, create_document, get_documents  # provided by environment

app = FastAPI(title="Portfolio API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root() -> Dict[str, Any]:
    return {"status": "ok", "service": "portfolio-api", "time": datetime.utcnow().isoformat()}

@app.get("/test")
async def test_db():
    # Verify db connectivity by listing collections
    try:
        collections = await db.list_collection_names()
        return {"ok": True, "collections": collections}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.post("/contact", response_model=ContactResponse)
async def create_contact(payload: Contact):
    try:
        doc = await create_document("contact", payload.dict())
        return ContactResponse(id=str(doc.inserted_id), status="received", message="Thanks for reaching out!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
