from fastapi import FastAPI, Depends

app = FastAPI()

def depend(val:int) -> str:
    if val>10:
        return "a"
    else:
        return "b"

@app.get("/")
def start():
    return "Hello World"

@app.get("/{val}")
def start(val: str = Depends(depend)):
    return  {
        "message":"Hello World",
        "cnt":val
    }
