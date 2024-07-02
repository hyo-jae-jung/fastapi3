from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/submit/")
async def submit_form(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
