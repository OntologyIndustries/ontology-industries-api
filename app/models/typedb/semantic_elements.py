from enum import StrEnum

from pydantic import BaseModel, Field


class ValueType(StrEnum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"


class Property(BaseModel):
    name: str
    value_type: ValueType


class Object(BaseModel):
    name: str
    properties: list[Property]


class Link(BaseModel):
    name: str
    from_objects: list[str] = Field(
        default_factory=list,
        description="List of names of 'from' objects",
    )
    to_objects: list[str] = Field(
        default_factory=list,
        description="List of names of 'to' objects",
    )
