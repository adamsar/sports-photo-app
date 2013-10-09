from django.test import TestCase

from photos.models import *

class TagTestCase(TestCase):

    def test_can_create(self):
        tag = Tag.objects.create(name="TestTag")
        self.assertTrue(isinstance(tag, Tag))

    def test_can_query(self):
        to_create = ["Tag1", "Tag2"]
        for name in to_create:
            Tag.objects.create(name=name)
        tags = Tag.objects.all()
        self.assertIsNotNone(tags)
        self.assertEqual(sorted([t.name for t in tags]), to_create)
