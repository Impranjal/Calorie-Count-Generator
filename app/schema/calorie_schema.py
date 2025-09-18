from pydantic import BaseModel,Field,validator
from typing import Optional

class CalorieRequest(BaseModel):
    dish_name:str = Field(...,min_length=1)
    servings:int 
    
    @validator("servings")
    def servings_greater_than_one(cls,v):
        if v <=0:
            raise ValueError("Servings must be a positive integer")
        return v
    
class CalorieResponse(BaseModel):
    dish_name:str
    servings:int
    calories_per_servings: int
    total_servings: int =Field(...,min_length=1)
    source: str = "USDA FoodData Capital"

    
