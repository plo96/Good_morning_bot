from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

HOME_DIR = Path(__file__).parent.parent.parent.absolute()


@dataclass
class Settings:
	bot_token: str
	weather_token: str
	gpt_token: str
	gpt_identification: str
	home_dir: Path
	db_echo: bool
	admin_id: int
	max_number_of_users: int
	redis_url: str = 'redis://localhost:6379/0'
	
	def __post_init__(self):
		self.db_url_sqlite_async: str = f"sqlite+aiosqlite:///{HOME_DIR}/src/database/db_sqlite/db.sqlite3"
		self.db_url_sqlite_sync: str = f"sqlite:///{HOME_DIR}/src/database/db_sqlite/db.sqlite3"
		self.db_url_sqlite_async_test: str = f"sqlite+aiosqlite:///{HOME_DIR}/src/database/db_sqlite/test_db.sqlite3"
		

settings = Settings(
	bot_token=os.getenv("BOT_TOKEN"),
	weather_token=os.getenv("OPENWEATHERMAP_API_KEY"),
	gpt_identification=os.getenv("YANDEX_GPT_IDENTIFICATION"),
	gpt_token=os.getenv("YANDEX_GPT_API_KEY"),
	home_dir=HOME_DIR,
	db_echo=False,
	admin_id=int(os.getenv('ADMIN_ID')),
	max_number_of_users=int(os.getenv('MAX_NUMBER_OF_USERS')),
)
