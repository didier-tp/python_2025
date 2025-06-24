from basic import addition
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def test_addition():
    resAdd=addition(3,5)
    assert resAdd == 8
    logger.info("addition(3,5)=" + str(resAdd))
