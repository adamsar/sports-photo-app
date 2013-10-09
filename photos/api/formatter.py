"""
Formatters for parsing returns from the api
"""
import itertools

def no_formatting(value):
    return value

def flatten(collection):
    return itertools.chain.from_iterable(collection)

