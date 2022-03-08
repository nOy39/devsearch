from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(uuid=uuid.uuid4(), unique=True, primary_key=True,
                          editable=False, null=False)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

