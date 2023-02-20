from django.db import models
import uuid

class Post(models.Model):
    # user_id =
    post_status = models.CharField(max_length=25, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=250, null=True)
    mood = models.CharField(max_length=25, null=True)
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['-created']
