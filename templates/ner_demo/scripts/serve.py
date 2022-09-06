from typing import List, Dict, Any
from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spacy
from spacy.tokens import Doc
import en_ner_demo

class Sentence(BaseModel):
    text: str

class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int

class Entities(BaseModel):
    entities: List[Entity]  

# Set up the FastAPI app and define the endpoints
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

nlp = en_ner_demo.load()

@app.get("/", summary="Health Check")
def health_check() -> List[str]:
    return "LIVE"


@app.post("/process/entities", summary="Process batches of text", response_model=Entities)
def process_entities(sentence: Sentence):
    ents = nlp(sentence.text).ents
    return {"entities":[{"text":ent.text, 
                         "label":ent.label_, 
                         "start":ent.start_char, 
                         "end":ent.end_char} for ent in ents]}
