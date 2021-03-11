from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Horesy API',
    version='0.0.1',
    description='services and endpoints for Horesy',
    redoc_url='/'
)

# setup the origins
origins = ["http://localhost","http://localhost:3000","http://127.0.0.1", ]

# add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def hello():
    return {"message": "Hello there!"}

@app.post("/hello")
async def test():
    pass