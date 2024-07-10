from django.db import models
from django.conf import settings

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        if self.is_anonymous:
            return "%i::%s by Anonymous" % (self.id, self.title)
        else:
            return "%i::%s by %s" % (self.id, self.title, self.author)