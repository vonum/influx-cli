def tags_in_measurement(bucket: str, measurement: str) -> str:
    return f"""
        import "influxdata/influxdb/schema"

        schema.measurementTagKeys(
            bucket: "{bucket}",
            measurement: "{measurement}",
        )
    """

def fields_in_measurement(bucket: str, measurement: str) -> str:
    return f"""
        import "influxdata/influxdb/schema"

        schema.measurementFieldKeys(
            bucket: "{bucket}",
            measurement: "{measurement}",
        )
    """
