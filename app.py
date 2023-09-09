import os
import re
import json
from typing import Dict
import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

api_key = "VwwUreJVM4NTOMtxk3rjP0MLUp0nYDBh"

class TrafficUpdate(object):
    def __init__(self, ApiKey) -> None:
        pass

    def fetch_traffic_data(self):
        pass


@app.get('/')
async def get_traffic_data(request: Request):
    return templates.TemplateResponse("traffic.html", {"request": request, "api_key": api_key})