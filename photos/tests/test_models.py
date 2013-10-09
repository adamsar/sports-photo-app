from django.test import TransactionTestCase
from django.db import transaction

from photos.models import *

from datetime import datetime
from django.db import IntegrityError

class TagTestCase(TransactionTestCase):

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

class ImageTestCase(TransactionTestCase):

    def test_can_create(self):
        now = datetime.utcnow()        
        image = AppImage.objects.create(id="190321290",
                                    title="Something cool",
                                    caption="Something is really good",
                                    created_on=now)
        self.assertTrue(isinstance(image, AppImage))

        
    def test_fails_on_bad_params(self):
        now = datetime.utcnow()
        
        def check_and_rollback(**params):
            transaction.rollback()            
            self.assertRaises(IntegrityError, AppImage.objects.create,
                              **params)
            
        check_and_rollback(created_on=now)
