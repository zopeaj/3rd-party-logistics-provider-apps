from enum import Enum
from pydantic import BaseModel, Field


class Contract_Type(str, Enum):
    on_demand = "on_demand"
    monthly = "monthly"

class ContractType(BaseModel):
    contractType: Contract_Type = Field(..., alias="Contract Type")

