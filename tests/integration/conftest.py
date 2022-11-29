import pytest
import os

CONNECTION_TIMEOUT = 1
READ_TIMEOUT = 5

class Config:
    def __init__(self):
        target_host = os.getenv("TARGET_HOST", "127.0.0.1")
        target_port = os.getenv("TARGET_PORT", 5000)
        self.base_url = f'http://{target_host}:{target_port}/'
        self.TIMEOUT = (CONNECTION_TIMEOUT, READ_TIMEOUT)

@pytest.fixture
def config():
    return Config()
