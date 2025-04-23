from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass, field

@dataclass
class CreateApple(BaseModel):
    colour:Optional[str]=field(metadata={"examples": ["Red","Blue","Orange"],"name": "Colour", "type": "Element"})
    origin:Optional[str]=field(metadata={"examples": ["Bahrain","United Stated of America"],"name": "Origin", "type": "Element"})

class AppleResponse(BaseModel):
    colour:Optional[str]=field(metadata={"examples": ["Red","Blue","Orange"],"name": "Colour", "type": "Element"})
    origin:Optional[str]=field(metadata={"examples": ["Bahrain","United Stated of America"],"name": "Origin", "type": "Element"})