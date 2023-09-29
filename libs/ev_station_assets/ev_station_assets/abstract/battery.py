from pydantic import BaseModel, Field


class AbstractState(BaseModel):
    pass


class AbstractBatteryState(AbstractState):
    soc: float = Field(ge=0, le=1)
    current_power: float = Field(ge=0)

    def __new__(cls, *args, **kwargs):
        if cls is AbstractBatteryState:
            raise Exception("cannot instantiate a instance of abstract class")
        return super().__new__(cls)


class AbstractBattery(BaseModel):
    name: str = Field(max_length=30, min_length=3, frozen=True)
    nameplate_capacity: float = Field(ge=0, le=10000, frozen=True)
    capacity: float = Field(ge=0, le=10000)
    inverter_size: float = Field(ge=0, le=10000, frozen=True)
    current_state: AbstractBatteryState

    def __new__(cls, *args, **kwargs):
        if cls is AbstractBattery:
            raise Exception("Cannot instantiate an instance of abstract class")
        return super().__new__(cls)