import httpx

from src.project.config import settings
from src.outer_apis_workers.base_worker import BaseWorker

WEATHER_URL = "Some_LLM_URL"


class LLMWorker(BaseWorker):
	
	async def get_weather(self) -> dict:
		res = await httpx.post(url=self._url, headers=self._headers)
		return res.json()
	

weather_worker = LLMWorker(
	url=WEATHER_URL,
	token=settings.weather_token,
)
