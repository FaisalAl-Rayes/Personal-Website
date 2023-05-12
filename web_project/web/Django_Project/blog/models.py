from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog_images")
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The representation of the blog."""

        return self.title
