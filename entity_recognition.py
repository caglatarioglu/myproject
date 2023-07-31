from pydantic import BaseModel
from typing import List

class Entity(BaseModel):
    text: str
    entity_type: str

class EntityRecognitionModel:
    def recognize_entities(self, text: str) -> List[Entity]:

        pass

