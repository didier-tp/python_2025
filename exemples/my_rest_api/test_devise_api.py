from fastapi.testclient import TestClient
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/devise-api/v1/devises")
    assert response.status_code == 200
    logger.info("response.json()=" + str(response.json()))
    #assert response.json() == {....}