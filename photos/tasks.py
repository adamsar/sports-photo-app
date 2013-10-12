"""
Celery tasks for the app, mostly relating to the ingestion of
photo data
"""

from photos.ingestion.images import can_ingest, consume_image
from photos.cnsts import search
from photos.api import requests

from photos.api.core import ImageApi
from celery import task
from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
  

import logging
log = logging.getLogger(__name__)

@periodic_task(run_every=crontab(hour="*", minute="30", day_of_week="*"))  
def check_for_new():
    """Checks the api for images"""
    keywords = [(team, keyword) for team in search.TEAMS['nfl'] for keyword in search.TERMS]
    for terms in keywords:
        check_terms.delay(terms)

@task
def check_terms(terms):
    """
    Given an iterable of terms it will search the api, and ingest any new content
    """
    log.debug("Checking for {}".format(str(terms)))
    api = ImageApi()
    images = api.make_request(params=requests.photo_reel(terms, limit=25)).list()
    map(do_ingest.delay, filter(lambda image: can_ingest(image), images.items))

@task
def do_ingest(image):
    log.debug("Ingesting {}".format(str(image)))
    consume_image(image)
    
    
def resize_and_save(raw_image_data):
    pass
