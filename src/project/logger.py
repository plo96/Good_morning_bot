from logging import getLogger, Logger, StreamHandler, Formatter, INFO


def init_logger(name: str) -> Logger:
	"""Инициализатор корневого логера"""
	logger = getLogger(name)
	logger.setLevel(INFO)
	
	FORMAT = '[%(levelname)s]_(%(asctime)s)_%(name)s:%(lineno)s - %(message)s'
	DATEFMT = '%d/%m/%Y %I:%M:%S'
	
	sh = StreamHandler()
	sh.setFormatter(Formatter(fmt=FORMAT, datefmt=DATEFMT))
	sh.setLevel(INFO)
	logger.addHandler(sh)
	
	return logger
