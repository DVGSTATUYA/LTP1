
from pydantic import BaseModel

class RawCalcResponse(BaseModel):
    result: int
