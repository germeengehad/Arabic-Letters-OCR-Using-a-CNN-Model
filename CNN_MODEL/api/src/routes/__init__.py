from fastapi import APIRouter
from .api import modelRouter

router = APIRouter()

router.include_router(modelRouter)
