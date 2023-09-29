from pydantic import BaseModel, Field


class AbstractSiteLoadState(BaseModel):
    current_load: float = Field(ge=0.00)


class AbstractSiteLoad(BaseModel):
    name: str = Field(min_length=3, max_length=30, frozen=True)
    max_load: float = Field(ge=0.00, frozen=True)
    current_state: AbstractSiteLoadState
