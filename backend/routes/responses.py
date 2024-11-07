from typing import Any, TypeVar, Literal, Mapping, Generic
from pydantic import BaseModel
from utils.errors import Error
from utils.json import OrJSONResponse

T = TypeVar("T")

def create_response(
    content: Mapping[str, Any],
    status_code: int,
) -> OrJSONResponse:
    response = OrJSONResponse(content=content, status_code=status_code)
    return response

class Success(BaseModel, Generic[T]):
    status: Literal["success"]
    data: T
    
class Failure(BaseModel):
    status: Literal["failure"]
    error: Error
    message: str
    
def format_success(data: Any) -> dict[str, Any]:
    return {"status": "success", "data": data}

def success(
    data: Any,
    status_code: int = 200,
) -> Any:
    content = format_success(data)
    return create_response(content, status_code) 

def format_failure(error: Error, message: str) -> dict[str, Any]:
    return {"status": "failure", "error": error, "message": message}

def failure(
    error: Error,
    message: str,
    status_code: int = 400,
) -> Any:
    content = format_failure(error, message)
    return create_response(content, status_code)