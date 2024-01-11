import os

from influx_cli.influx.influx_client import InfluxClient
from influx_cli.metadata_store import MetadataStore
from influx_cli.models import PredicateRequest


class CommandRunner:
    def __init__(
        self,
        org: str,
        bucket: str,
        influx_token: str,
        influx_url: str
    ):
        self.influx_client = InfluxClient(org, bucket, influx_token, influx_url)

        tags = self.influx_client.tags()
        fields = self.influx_client.fields()

        self.store = MetadataStore(tags, fields)

    def delete(
        self,
        predicates: list[PredicateRequest],
        start_timestamp: int,
        end_timestamp: int
    ):
        print(predicates)
