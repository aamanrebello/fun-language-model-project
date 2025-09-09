from typing import Union, Any
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import app.prompts as prompts

app = FastAPI()

app.include_router(prompts.router, prefix='/v1')