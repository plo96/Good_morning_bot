import httpx

from src.project.config import settings
from src.outer_apis_workers.base_worker import BaseWorker

LLM_URL = "Some_LLM_URL"


class LLMWorker(BaseWorker):
	
	async def get_good_morning(self) -> str:
		res = await httpx.post(url=self._url, headers=self._headers)
		return res.json().__str__()
	

llm_worker = LLMWorker(
	url=LLM_URL,
	token=settings.llm_token,
)
