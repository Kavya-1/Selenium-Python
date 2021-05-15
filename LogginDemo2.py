import logging

logging.basicConfig(filename="test1.log",
                    format='%(asctime)s: %(levelname)s : %(message)s',
                    datefmt='%d/%m/%y %I:%M:%S %p'
                   )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is a debug log")
logger.error("This is a error log")
logger.info("This is a info log")
logger.warning("This is a warning log")
logger.critical("This is a critical log")