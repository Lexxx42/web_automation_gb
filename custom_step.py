from allure_commons._allure import StepContext
from logger import Logger


def step(title: str, log_level: str = 'INFO') -> StepContext:
    log_method = getattr(Logger, log_level.lower(), Logger.info)

    log_method(title)

    return StepContext(title, {})
