from pydantic import BaseModel 
from typing import Any

class Item(BaseModel):
    item: str 
    status: str

class Todo(BaseModel):
    id: Any
    item: Item 

