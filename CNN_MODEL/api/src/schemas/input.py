from pydantic import BaseModel
class ImageInput(BaseModel):
    base64_image: str
