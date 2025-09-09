from pydantic import BaseModel
from enum import Enum
from pydantic import Field, field_validator
import re

class QuestionType(Enum):
    LOCATE = 'LOCATE'
    ABOUT = 'ABOUT'
    MEANING = 'MEANING'

class Query(BaseModel):
    searchItem: str = Field(description="A single word, no spaces or punctuation", pattern=r'^[\w]+$', example="apple")
    questionType: QuestionType = Field(default=QuestionType.ABOUT)
    