import unittest
import bisect

"""
write down thoughts
"""

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s"
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info("Logger Setup Finished")
def submit():
    try:
        import dummy
        return True
    except (ImportError,ModuleNotFoundError) as err:
        logger.exception('Error importing module : {}'.format(err))
        return False


class TestException(unittest.TestCase):
    def test1(self):
        assert submit()==False, "Fail to import"


if __name__ == '__main__':
    unittest.main()
