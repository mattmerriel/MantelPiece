import logging

import src.mantelware.__main__ as mw
import src.mantelware.components.logging_config


logger = logging.getLogger('main')


if __name__ == "__main__":
    logger.debug("debug message: Application Started")
    logger.info("info message: Application Started")
    mw.cli()
