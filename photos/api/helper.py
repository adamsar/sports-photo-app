"""
Quick helper functions for the api
"""

PREVIEW_URL = "http://thumb.usatodaysportsimages.com/image/thumb/{}-{}nw/{}.jpg"

def get_preview_url(_id, width, height):
    """
    Leverages the API to get a preview url for the given image id,
    width, and height
    """
    return PREVIEW_URL.format(str(width), str(height), str(_id))
