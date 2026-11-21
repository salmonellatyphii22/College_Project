from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    category: str
    response: str