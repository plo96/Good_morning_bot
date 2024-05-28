"""
    Взаимодействие с API gpt.
"""
__all__ = (
    "gpt_worker",
)

from .yandex_gpt_worker import yandex_gpt_worker as gpt_worker
