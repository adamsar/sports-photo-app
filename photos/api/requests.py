"""
Common api requests for reuse
"""

from functools import partial

KEYWORDS = "keywords"
MODE = "mode"
LIMIT = "limit"
PHRASE = "phrase"

def photo_reel(keywords, limit=10):
    return {
        KEYWORDS: ",".join(keywords),
        MODE: PHRASE,
        LIMIT: limit
        }

def cheerleaders(keywords=[]):
    return partial(photo_reel, ["cheerleader"] + keywords)
