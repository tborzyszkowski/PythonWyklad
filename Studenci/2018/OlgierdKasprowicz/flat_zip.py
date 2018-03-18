#!/usr/bin/env python3

from itertools import chain
from functools import reduce
from operator import concat

def flat_zip(lists):
    """
    Zips lists into a single list, not list of tuples
    """

    zipped_lists = zip(*lists)
    return chain.from_iterable(zipped_lists)
    
def flat_zip_academic(lists):
    """
    Zips lists into a single list, not list of tuples

    This uses more academic method of flattening a list of lists
    """

    zipped_lists = zip(*lists)
    return reduce(concat, zipped_lists)

if __name__ == "__main__":
    print("Fast:")
    lists = [[1,3,5], [2,4,6]]
    print(lists)
    print(list(flat_zip(lists)))

    print()

    print("Academic:")
    lists = [[1,3,5], [2,4,6]]
    print(lists)
    print(list(flat_zip_academic(lists)))
