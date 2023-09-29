from pydantic import BaseModel, Field


class AbstractChargerState(BaseModel):
    current_power: float = Field(ge=0, le=10000)


class AbstractCharger(BaseModel):
    name: str = Field(min_length=3, max_length=13, frozen=True)
    max_power: float = Field(ge=0, le=10000, frozen=True)
    max_power_to_car: float = Field(ge=0, le=10000)
    current_state: AbstractChargerState
