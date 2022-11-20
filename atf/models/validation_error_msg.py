from typing import List, Dict, Union

from pydantic import BaseModel


class ValidationErrorMsg(BaseModel):
    detail: List[Dict[str, Union[List[Union[str, int]], str]]]
