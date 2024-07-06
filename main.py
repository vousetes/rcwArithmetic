from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()
# Allow oreigins

origins =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Number( BaseModel):
    num1 : float
    num2 : float

@app.post('/prod')
async def welcome(num: Number):
    a= num.num1

    b= num.num2

    print(f"{a} X {b}={int(a*b)}")
    return {f"Request confirmation:Product is {a*b}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8801)

