import os
import click
from .command_runner import CommandRunner


class CommandGroup(click.Group):
    def invoke(self, ctx: click.Context):
        org = os.getenv("ORG")
        bucket = os.getenv("BUCKET")
        influx_token = os.getenv("INFLUX_TOKEN")
        influx_url = os.getenv("INFLUX_URL")

        # needs to be called obj for the decorator to be able to find the instance
        ctx.obj = CommandRunner(org, bucket, influx_token, influx_url)
        super(CommandGroup, self).invoke(ctx)

