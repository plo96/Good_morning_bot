import aiohttp

from src.outer_apis_workers.multiply_triying import multiply_trying
from src.project.config import settings
from src.project.exceptions import GptApiException

GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


class GptWorker:

    def __init__(
            self,
            url: str,
            token: str,
            identification: str,
    ):
        self._url = url
        self._headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        self._model_uri = f"gpt://{identification}/yandexgpt-lite"
    
    @multiply_trying
    async def get_good_morning(
            self,
            sex: str,
            name: str,
    ) -> str:
        prompt = {
            "modelUri": self._model_uri,
            "completionOptions": {
                "stream": False,
                "temperature": 0.8,
                "maxTokens": "500"
            },
            "messages": [
                {
                    "role": "user",
                    "text": f"Сгенерируй одно приятное и интересное пожелание доброго утра для пользователя, пол - {sex}, имя - {name}."
                },
            ]
        }

        async with aiohttp.ClientSession() as client:
            async with client.post(
                    self._url,
                    headers=self._headers,
                    json=prompt,
                    timeout=5,
            ) as response:
                status_code = response.status
                if status_code != 200:
                    raise GptApiException
                result = (await response.json())['result']['alternatives'][0]['message']['text']
        return result


gpt_worker = GptWorker(
    url=GPT_URL,
    token=f"Api-Key {settings.gpt_token}",
    identification=settings.gpt_identification,
)
