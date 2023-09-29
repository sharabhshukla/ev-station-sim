from pydantic import BaseModel, Field


class AbstractGeneratorState(BaseModel):
    power: float = Field(ge=0.00)
    fuel_state: float = Field(ge=0.00, le=1.00)


class AbstractGenerator(BaseModel):
    name: str = Field(min_length=3, max_length=30, frozen=True)
    efficiency: float = Field(ge=0.00, le=1.00)
    input_cost_per_unit_fuel: float = Field(ge=0.00)
    fuel_capacity_units: float = Field(ge=0.00)
    current_state: AbstractGeneratorState
