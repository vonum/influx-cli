import os
import pytest
from tests.db_cleaner import DBCleaner


@pytest.fixture
def reset_influx():
    org = os.getenv("ORG")
    bucket = os.getenv("BUCKET")
    token = os.getenv("INFLUX_TOKEN")
    url = os.getenv("INFLUX_URL")

    client = DBCleaner(org, bucket, token, url)
    client.reset_db()
    print("\nCleared influxdb")
    yield None
