from fastapi import APIRouter
from app.models.entity_recognition import Entity, EntityRecognitionModel

router = APIRouter()

@router.post("/recognize", response_model=List[Entity])
async def recognize_entities(text: str):
    model = EntityRecognitionModel()
    entities = model.recognize_entities(text)
    return entities
