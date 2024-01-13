from datetime import datetime
from influx.influx_client import InfluxClient


class DBCleaner(InfluxClient):
    def reset_db(self):
        dt = datetime.now()
        start = "1970-01-01T00:00:00Z"
        stop = dt.strftime('%Y-%m-%dT%H:%M:%SZ')

        self._delete_api().delete(
            start,
            stop,
            "",
            bucket=self.bucket,
            org=self.org
        )
