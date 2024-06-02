import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
# from functools import lru_cache

from routes import router
from config import settings
from schemas import ExceptionHandler

app = FastAPI(
    title=settings.APP_NAME,
    description="This is a CNN for OCR of the Arabic letter"
)

# @lru_cache()
# def get_settings():
#     return Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root():
    return """
    <h2 style="text-align:center">
        Click
        <a href="/docs">API DOC</a>
        to see the API doc
    </h2>
    """

app.include_router(router, prefix=settings.API_V1_STR)


@app.exception_handler(ExceptionHandler)
async def handleException(request: Request, exc: ExceptionHandler):
    return JSONResponse(
        status_code=exc.status,
        content={"message": f"Oops! {exc.message}, Please try again!"},
    )


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return HTMLResponse("""
    <h2 style="text-align:center">
        Page Not Found
        <br />
        Click
        <a href="/docs">API DOC</a>
        to see the API doc
    </h2>
    """)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.DEBUG_MODE,
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT
    )


# uvicorn main:app --reload
# D:\Projects\Test\envs\fast\Scripts\activate
