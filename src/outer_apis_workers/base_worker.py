
class BaseWorker:
	def __init__(self, url: str, token: str):
		self._url = url
		self._headers = {"Authorization": token}
