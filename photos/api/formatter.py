"""
Formatters for parsing returns from the api
"""
from datetime import datetime

#"2007-01-01 01:35:04"
API_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def no_formatting(value):
    return value

def flatten_and_merge(collection):
    """
    Visit each member of a series of lists until
    we reach the crunch bottom and fold all the entries
    into a result table. This is for cleaning up
    keywords
    """
    results = {}
    def visit(node):
        if isinstance(node, list):
            for n in node: visit(n)
        else:
            results.update(node)
    visit(collection)
    return results
        

def parse_date(date):
    """
    Formats a date from the API
    """    
    return datetime.strptime(date, API_DATE_FORMAT)

