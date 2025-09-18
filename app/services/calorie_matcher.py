from rapidfuzz import process, fuzz

class CalorieMatcher:
    def best_match(self, query: str, foods: list, threshold: int = 60):
        if not foods:
            return None, 0
        query = query.lower().strip()
        food_names = [food.get("description", "").lower().strip() for food in foods]
        match, score, idx = process.extractOne(query, food_names, scorer=fuzz.WRatio)

        if score < threshold:
            return None, 0
        return foods[idx], score
