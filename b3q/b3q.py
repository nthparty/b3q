"""Boto3 predicate-driven retrieval of AWS resources.

Boto3 utility library that supports parameter-driven and
predicate-driven retrieval of collections of AWS
resources.
"""

from __future__ import annotations
import doctest

def get(method, arguments=None, constraints=None, attribute=None):
    """
    Assemble all items in a paged response pattern from
    the supplied AWS API retrieval method.
    """
    arguments = {} if arguments is None else arguments
    constraints = {} if constraints is None else constraints
    attribute = 'items' if attribute is None else attribute
    position = {}
    while True:
        response = method(**arguments, **position)
        for item in response[attribute]:
            if all(item[k] == v for (k, v) in constraints.items()):
                yield item
        if not 'position' in response:
            break
        position = {'position': response['position']}

if __name__ == "__main__":
    doctest.testmod()
