from aiogram import Router

from .config_handler import router as config_router

router = Router()

router.include_routers(config_router, )

