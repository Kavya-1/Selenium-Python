import logging

logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s : %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d/%m/%y %I:%M:%S %p'
                   )
# levels
# debug
# info
# warn - threshold
# error
# critical
# just debug wont appear in console
logging.debug("This is a debug log")
logging.error("This is a error log")
# just information
logging.info("This is a info log")
# threshold level
logging.warning("This is a warning log")
logging.critical("This is a critical log")

