from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FormData(BaseModel):
    aadhaar: str
    owner_name: str
    declaration: bool

@app.post("/submit")
async def submit_form(data: FormData):
    print("Received:", data)
    return {"message": "Form received successfully"}
