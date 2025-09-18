from rapidfuzz import fuzz, process

class CalorieMatcher:
    def best_match(self, query: str, foods: list, threshold: int = 60):
        food_names = [food.get("description", "") for food in foods]
        match, score, idx = process.extractOne(query, food_names, scorer=fuzz.WRatio)
        if score < threshold:
            return None, None
        return foods[idx], score
