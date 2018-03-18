#!/usr/bin/env python3

from itertools import chain

def flat_zip(lists):
    """
    Zips lists into a single list, not list of tuples
    """

    zipped_lists = zip(*lists)
    return chain.from_iterable(zipped_lists)
    

if __name__ == "__main__":
    lists = [[1,3,5], [2,4,6]]
    print(lists)
    print(list(flat_zip(lists)))
