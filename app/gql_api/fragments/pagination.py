""" Contains a reusable pagination function applicable to GraphQL queries """
from typing import List, TypeVar
import strawberry

# pylint: disable=invalid-name
# NOTE: (alopez) TypeVar must be assigned to a variable named "GenericType"Pylance
GenericType = TypeVar("GenericType")


@strawberry.type
class PaginationWindow(List[GenericType]):
    items: List[GenericType] = strawberry.field(
        description="The list of items in this pagination window."
    )


def get_pagination_window(
        dataset: List[GenericType],
        limit: int,
        total: int,
        offset: int = 0) -> PaginationWindow:
    """
    Get one pagination window on the given dataset for the given limit
    and offset, ordered by the given attribute and filtered using the
    given filters
    """

    if limit <= 0 or limit > 10:
        raise Exception(f'limit ({limit}) must be between 0-10')

    if offset != 0 and not 0 <= offset < total:
        raise Exception(f'offset ({offset}) is out of range '
                        f'(0-{total - 1})')

    items = dataset[offset:offset + limit]

    return PaginationWindow(items=items)
