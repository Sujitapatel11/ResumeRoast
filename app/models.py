#This file will act as the "souce of truth" for what a job listing actually is.It will define the columns in the databse and the rules for the API.
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import field_validator, ConfigDict
from datetime import datetime
class AnalysisRequest(SQLModel):
    text: str
class Joblisting(SQLModel, table=True):
    #this forces pydantic to validate data even when we just assign values.
    #It prevents SQLModel from bypassing our rules for performance.
    model_config = ConfigDict(validate_assignment=True)
    id: int | None =  Field(default=None, primary_key=True)
    title: str
    description: str
    skills: str
    location: str
    salary_range: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    #VALIDATION LOFIC
    @field_validator("salary_range", mode="after")
    @classmethod
    def validate_salary(cls, value: str | None) -> str | None:
        """ Enforce that the salary range is in the format 'min-max' where min and max are integers."""
        if value is None:
            return None
        if value.strip().startswith("-"):
            raise ValueError("Salary cannot be negative. We pay people here.")
        return value