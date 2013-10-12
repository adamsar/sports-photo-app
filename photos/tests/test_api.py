from django.test import TestCase

from photos.api.core import ImageApi
from photos.api import requests, helper, keys
from photos.util.images import read_image

class APITestCase(TestCase):

    def setUp(self):
        self.api = ImageApi()

    def test_can_list(self):
        params = {
            "limit": 5,
            "mode": "phrase",
            "keywords": "NFL,cheerleader"
        }
        results = self.api.make_request(params=params).list()
        self.assertEquals(len(results), 5)

        
    def test_image_links(self):
        """
        Test the preview image functionality for a photo
        """
        result = self.api.make_request(
            requests.photo_reel(["NFL"], limit=1)
                                ).one()
        
        def expect_size(image, width, height):
            test = min(width, height)
            test2 = max(*image.size)
            self.assertEqual(test, test2)

        sizes = [(100, 20), (20, 100)]
        for size in sizes:
            img = read_image(
                helper.get_preview_url(result.get(keys.ID), size[0], size[1])
                )
            expect_size(img, size[0], size[1])        

