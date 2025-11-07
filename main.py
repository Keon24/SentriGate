from fastapi import FastAPI
import os
app = FastAPI()

@app.get('/')
def home_page():
    return{"message":"backend is now running"}


    