from pydantic import BaseModel
from datetime import datetime

#Demand a title for creating new todos
class TodoCreate(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime
    
    class config:
        from_attributes = True