"""
	Настройка логгера для данного приложения.
"""
from asyncio import create_task
import logging
from logging.handlers import RotatingFileHandler
import os

from aiogram import Bot

from src.project.config import settings


class BotMessageHandler(logging.Handler):
	"""Кастомный хендлер для отправки уведомлений администратору в Telegram."""
	def __init__(self, bot: Bot):
		super().__init__()
		self.bot = bot
	
	def emit(self, record):
		try:
			msg = self.format(record)
			create_task(self.bot.send_message(settings.admin_id, msg))
		except Exception:
			self.handleError(record)


def init_logger(name: str, bot: Bot) -> None:
	"""
	Инициализация и настройка логгера: задание уровней перехвата и форматов для всех хендлеров.
	bm_handler - кастомный хендлер для отправки особо важных уведомлений в Telegram.
	fh - хендлер для записи в файл логов текущей сессии (обновляется при перезапуске приложения).
	rfh - хендлер для записи в серию файлов общих логов (обновляется при превышении размера файлов).
	:param name: Имя логгера.
	:param bot: Бот, с которого будут отправляться уведомления.
	:return: None
	"""
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	FORMAT = '[%(levelname)s]_(%(asctime)s)_%(name)s:%(lineno)s - %(message)s'
	DATEFMT = '%d/%m/%Y %I:%M:%S'
	
	if settings.admin_id:
		bm_handler = BotMessageHandler(bot=bot)
		bm_handler.setLevel(logging.WARNING)
		logger.addHandler(bm_handler)
	
	if "logs" not in os.listdir(settings.home_dir):
		os.chdir(settings.home_dir)
		os.mkdir("logs")
		os.chdir(os.path.dirname(os.path.abspath(__file__)))
		print(os.curdir)
	
	fh = logging.FileHandler(filename=f"{settings.home_dir}\\logs\\current_logs.log", mode='w')
	fh.setFormatter(logging.Formatter(fmt=FORMAT, datefmt=DATEFMT))
	fh.setLevel(logging.DEBUG)
	logger.addHandler(fh)
	
	rfh = RotatingFileHandler(
		filename=f"{settings.home_dir}\\logs\\logs.log",
		mode='a',
		maxBytes=5 * 1024 * 1024,
		backupCount=5
	)
	rfh.setFormatter(logging.Formatter(fmt=FORMAT, datefmt=DATEFMT))
	rfh.setLevel(logging.INFO)
	logger.addHandler(rfh)
	
	logger.debug('logger was initialized.')
