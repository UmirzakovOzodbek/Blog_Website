from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    poster = models.ImageField("Poster", upload_to="post/", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
