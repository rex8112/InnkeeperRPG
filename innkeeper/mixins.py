class EqualityComparableMixin:
    id: int

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self.id == other.id

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


class HashableMixin(EqualityComparableMixin):
    def __hash__(self) -> int:
        return hash(self.id)