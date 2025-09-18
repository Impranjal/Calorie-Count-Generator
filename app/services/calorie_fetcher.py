import httpx
from app.config_loader import settings
from app.exceptions import DishNotFoundException
class CalorieFetcher:
    def __init__(self, api_key:str=settings.API_KEY, http_timeout:int=10):
        if not api_key: 
            raise RuntimeError("API Credentials missing")
        self._api_key = api_key
        self.timeout = http_timeout
        
    async def fetch_calorie(self,dish_name:str,page_size:int=None):
        url = settings.API_URL
        params = {
            "query":dish_name,
            "api_key":self._api_key,
            "pageSize": page_size or 1
        }
        async with httpx.AsyncClient() as client:
                res = await client.get(url, params=params)
                data= res.json().get("foods", [])
        if not data:
            raise DishNotFoundException(dish_name)
        return data
        
        