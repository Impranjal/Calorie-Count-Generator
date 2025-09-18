from fastapi import APIRouter, Depends, HTTPException,Request
from app.services.calories_calculator import CalorieCalcultor
from app.schema.calorie_schema import CalorieRequest,CalorieResponse
from app.services.rate_limiter import limiter
from app.exceptions import DishNotFoundException,ServiceUnavailableException

router = APIRouter(
     tags=["Calories"]
)

@router.post("/get-calories",response_model=CalorieResponse)
@limiter.limit("15/minute")
async def get_calories(request: Request,req:CalorieRequest ):
    dish_name = req.dish_name
    servings = req.servings or 1
    calc = CalorieCalcultor()
    try:
            result = await calc.process(req.dish_name, req.servings)
            if not result:
                raise DishNotFoundException(req.dish_name)
            return result
    except DishNotFoundException:
        raise
    except Exception:
        raise ServiceUnavailableException()