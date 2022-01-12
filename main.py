from fastapi import FastAPI
from pydantic import BaseModel

from transformers import pipeline



class Sentence (BaseModel):
        sentence: str


unmasker = pipeline('fill-mask', model='bert-base-uncased')

app = FastAPI()

@app.post("/get_suggestions")
async def root(request: Sentence):
        """String with * required"""
        q = request.sentence
        if q.count("*") != 1:
                return {"status":"error", "details":"Masked symbol * found more than once" }
        try:
                q = q.replace("*", "[MASK]")
                result = unmasker(q)
                return result
        except Exception as e:
                return {"status":"error", "details":e.args }
