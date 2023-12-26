from django.db import models

class Post(models.Model):

    post_name = models.CharField(max_length=255)
    post_text = models.CharField(max_length=10000)
    post_time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_name}: {self.post_time_in}: {self.post_text[:20]}'

