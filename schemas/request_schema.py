from pydantic import BaseModel, Field
from typing import List

class Location(BaseModel):
    lat: float
    lng: float

class Job(BaseModel):
    id: int
    location: Location
    demand: int = Field(ge=0)
    service_time: int = Field(ge=0)

class Vehicle(BaseModel):
    id: int
    capacity: int = Field(gt=0)
    start_location: Location

class OptimizeRequest(BaseModel):
    jobs: List[Job]
    vehicles: List[Vehicle]
