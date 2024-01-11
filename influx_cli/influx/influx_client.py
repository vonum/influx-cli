import influxdb_client
from influxdb_client import InfluxDBClient
from influxdb_client import WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.flux_table import FluxTable

from .queries import tags_in_measurement, fields_in_measurement


MEASUREMENT = "horus"

class InfluxClient:
    def __init__(self, org: str, bucket: str, token: str, url: str):
        self.measurement = MEASUREMENT
        self.org = org
        self.bucket = bucket
        self.url = url
        self.client = InfluxDBClient(self.url, token=token, org=org, timeout=3000000)

    def tags(self) -> list[str]:
        query = tags_in_measurement(self.bucket, self.measurement)
        tables = self._run_query(query)
        return self._extract_keys(tables[0])

    def fields(self) -> list[str]:
        query = fields_in_measurement(self.bucket, self.measurement)
        tables = self._run_query(query)
        return self._extract_keys(tables[0])

    def close(self):
        self.client.close()

    def _extract_keys(self, table: FluxTable):
        return [
            r.get_value()
            for r in table.records
            if not r.get_value().startswith("_")
        ]

    def _run_query(self, query: str):
        query_api = self._query_api()
        return query_api.query(query, org=self.org)

    def _query_api(self):
        return self.client.query_api()

    def _delete_api(self):
        return self.client.delete_api()
