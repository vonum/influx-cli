from dataclasses import dataclass


# field request doesn't need value defined -> _field="price_btc"
# tag requests need value -> chain="ethereum" AND "asset"="ether"

# NO OR FOR PREDICATES
# FIELDS NEED TO GO 1 by 1
# FIELDS WILL DELETE ALL DATA
# DELETE FIELDS ONLY WHEN DEPRECATING METRICS
# DELETE BY TAGS OTHERWISE


# DIFFERENT PREDICATES FOR EACH OPERATION

@dataclass
class PredicateRequest:
    type:             str # field or tag
    key:              str
    is_key_pattern:   bool
    value:            str | None

    @classmethod
    def create_predicate_requests(
        cls,
        predicates: list[tuple[str, str, bool, str]]
    ):
        return [cls(*predicate) for predicate in predicates]

@dataclass
class Predicate:
    type: str
    key: str
    value: str | None
