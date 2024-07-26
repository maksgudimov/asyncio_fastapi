import uuid

from pydantic import BaseModel, field_validator


class Operations(BaseModel):
    x: int
    y: int
    operation: str

    @field_validator('operation')
    @classmethod
    def validate_operation(cls, value):
        check_values = ['+', '-', '*', '/']
        if value not in check_values:
            raise ValueError("Operation must be: + or - or * or /.")
        return value
