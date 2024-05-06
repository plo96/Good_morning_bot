# import httpx
import requests as req

from src.project.config import settings


GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"


class GptWorker:

    def __init__(
            self,
            url: str,
            token: str,
            identification: str,
            content_type: str = None
    ):
        self._url = url
        self._headers = {"Authorization": token}
        self._model_uri = f"gpt://{identification}/yandexgpt-lite"
        if content_type:
            self._headers["Content-Type"] = content_type

    def get_good_morning(
            self,
            sex: str,
            name: str,
    ) -> str:
        prompt = {
            "modelUri": self._model_uri,
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "500"
            },
            "messages": [
                {
                    "role": "user",
                    "text": f"Сгенерируй одно приятное и интересное пожелание доброго утра для пользователя, пол - {sex}, имя - {name}."
                },
            ]
        }

        print(self._headers)

        response = req.post(GPT_URL, headers=self._headers, json=prompt)
        print(response.json())
        result = response.json()['result']['alternatives'][0]['message']['text']
        return result

    # async def get_good_morning(self) -> str:
    #     res = await httpx.post(url=self._url, headers=self._headers)
    #     return res.json().__str__()


gpt_worker = GptWorker(
    url=GPT_URL,
    token=f"Api-Key {settings.gpt_token}",
    identification=settings.gpt_identification,
    content_type="application/json",
)

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Api-Key {YANDEX_GPT_API_KEY}"
# }


print(gpt_worker.get_good_morning(sex='женского', name='Айдана'))
