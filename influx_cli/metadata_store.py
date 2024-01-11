from .models import PredicateRequest, Predicate


FIELD = "field"
TAG = "tag"

class MetadataStore:
    def __init__(self, tags: list[str], fields: list[str]):
        self.tags = tags
        self.fields = fields

    def create_tag_predicates(self, request: PredicateRequest) -> list[Predicate]:
        pass

    def create_field_predicates(self, request: PredicateRequest) -> list[Predicate]:
        if request.is_key_pattern:
            predicates = [
                Predicate(FIELD, field, None) for field in self.fields
                if request.key in field
            ]
            return predicates
        else:
            if request.key in self.fields:
                return [Predicate(FIELD, request.key, None)]
