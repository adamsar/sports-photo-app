from django.db import models
import uuid

def UuidField(primary_key=False):
    """
    Denotes a CharField that is a Uuid field in the database.
    primary_key - this key is the primary key in the table it is present in.
    """

    options = {
        "primary_key": primary_key,
        "default": lambda: str(uuid.uuid4()),
        "max_length": 36
    }
    return models.CharField(**options)
    

#Basic way of associating information in the database
class Tag(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128, blank=True)
    associated_id = UuidField()    

    def __str__(self):
        return "Tag({}) with associated Id {}".format(self.name,
                                                      self.associated_id)

        
#Any image that has been ingested and is associable with a tag
class Image(models.Model):
    
    id = UuidField(primary_key=True)
    title = models.CharField(max_length=128)
    caption = models.CharField(max_length=4096, blank=True)
    tags = models.ManyToManyField(Tag, related_name="images")

    def __str__(self):
        return "Image({})".format(self.title)
