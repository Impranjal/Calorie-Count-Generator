from app.services.calorie_fetcher import CalorieFetcher
from app.services.calorie_matcher import  CalorieMatcher
class CalorieCalcultor:
    def __init__(self):
        self.fetcher = CalorieFetcher()
        self.matcher = CalorieMatcher()

    async def process(self, dish_name: str, servings: int):
        foods = await self.fetcher.fetch(dish_name)
        if not foods:
            return None

        best_food, score = self.matcher.best_match(dish_name, foods)
        if not best_food:
            return None

        calories = self._extract_calories(best_food)
        return {
            "dish_name": best_food.get("description"),
            "servings": servings,
            "calories_per_serving": calories,
            "total_calories": calories * servings,
            "match_score": score,
            "source": "USDA FoodData Central",
        }

    def _extract_calories(self, food: dict) -> float:
        for nutrient in food.get("foodNutrients", []):
            name = nutrient.get("nutrientName", "").lower()
            if "energy" in name and "kcal" in name:
                return nutrient.get("value", 0)
        return 0
