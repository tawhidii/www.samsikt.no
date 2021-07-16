from django.db import models
from django.utils import timezone


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    is_published = models.BooleanField(default=False, verbose_name="Is published?")
    published_at = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Published at")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', verbose_name="Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField(verbose_name="Text")
    thumbnail = models.ImageField(blank=True, upload_to='blogs/')
    blog_image = models.ImageField(blank=True, upload_to='blogs/')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
