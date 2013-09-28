from django.test import TestCase

from photos.models import *

class TagTestCase(TestCase):

    def test_can_create(self):
        tag = Tag.objects.create(name="TestTag")
        self.assertTrue(isinstance(tag, Tag))

    def test_can_query(self):
        for name in ["Tag1", "Tag2"]:
            Tag.objects.create(name=name)
        self.assertIsNotNone(Tag.objects.all())
