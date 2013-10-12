"""
Image based ingestion tasks
"""
from django.core.exceptions import ObjectDoesNotExist
from photos.api import keys, formatter
from photos.models import AppImage, Tag

def make_tags(image):
    """
    Makes a list of tags based on an image"
    """
    keywords = image.get(keys.KEYWORDS, formatter=formatter.flatten_and_merge)
    return [Tag.objects.get_or_create(
        name=value, category=key.upper()
        )[0] for key, value in keywords.iteritems()]


def consume_image(image):
    """
    Takes a photos.api.results.ImageResult and
    stores it in the database
    """
    img, successful = AppImage.objects.get_or_create(
        id=image.get(keys.ID),
        title=image.get(keys.HEADLINE),
        caption=image.get(keys.CAPTION),
        created_on=image.get(keys.UPLOAD_DATE, formatter.parse_date)
        )
    img.tags.add(*make_tags(image))
    return img
    

def can_ingest(image):
    """
    Checks to see if the image is in the DB and is henceforth
    safe to ingest
    """
    try:
        AppImage.objects.get(id=image.get(keys.ID))
        return False
    except ObjectDoesNotExist:
        return True
