from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application

app = FastAPI()

django_app = get_wsgi_application()

app.mount("/django", WSGIMiddleware(django_app))

@app.get("/api")
async def read_main():
    return {"message": "Hello World"}
