from fastapi import HTTPException, status

class DishNotFoundException(HTTPException):
    def __init__(self, dish_name: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish not found: '{dish_name}'."
        )

class ServiceUnavailableException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Calorie service temporarily unavailable."
        )
