from dataclasses import dataclass
import os
from pathlib import Path

HOME_DIR = Path(__file__).parent.parent.parent.absolute()


@dataclass
class Settings:
	bot_token: str
	weather_token: str
	llm_token: str
	home_dir: Path
	db_echo: bool
	
	def __post_init__(self):
		self.db_url_sqlite_async: str = f"sqlite+aiosqlite:///{HOME_DIR}/src/database/db_sqlite/db.sqlite3"
		self.db_url_sqlite_sync: str = f"sqlite:///{HOME_DIR}/src/database/db_sqlite/db.sqlite3"
		self.db_url_sqlite_async_test: str = f"sqlite+aiosqlite:///{HOME_DIR}/src/database/db_sqlite/test_db.sqlite3"
		

settings = Settings(
	bot_token=os.getenv("BOT_TOKEN"),
	weather_token=os.getenv("WEATHER_TOKEN"),
	llm_token=os.getenv("LLM_TOKEN"),
	home_dir=HOME_DIR,
	db_echo=False,
)
