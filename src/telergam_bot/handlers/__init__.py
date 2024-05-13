__all__ = (
	"router",
)

from aiogram import Router

from .config_handler import router as config_router
from .main_menu_handler import router as main_menu_router
from .delete_handler import router as delete_router

router = Router()

router.include_routers(main_menu_router, delete_router, config_router)
