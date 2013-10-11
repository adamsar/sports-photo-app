"""
ingestion tests for the api
"""

from django.test import TransactionTestCase
from photos.api.core import ImageApi
from photos.tests import mocks
from photos.ingestion.images import consume_image

class IngestionTestCase(TransactionTestCase):

    def setUp(self):
        self.api = ImageApi()

    def test_list_ingest(self):
        mocks.fake_results(self.api, "api_list.json")
        for result in self.api.make_request().list():
            image = consume_image(result)
