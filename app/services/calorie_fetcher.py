import httpx
from app.config_loader import settings

class CalorieFetcher:
    def __init__(self, api_key:settings.API_KEY, http_timeout:int=10):
        if not api_key: 
            raise RuntimeError("API Credentials missing")
        self._api_key = api_key
        self.timeout = http_timeout
        
    async def fetch_calorie(self,dish_name:str,page_size:int=None):
        url = settings.API_URL
        params = {
            "query":dish_name,
            "api_key":self._api_key,
            "pagesize": page_size
        }
        async with httpx.AsyncClient() as client:
                res = await client.get(url, params=params)
                return res.json().get("foods", [])
        