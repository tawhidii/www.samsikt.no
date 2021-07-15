from django.db import models


class AboutUs(models.Model):
    about_us_banner = models.ImageField(upload_to='uploads/about_us')
    about_title = models.CharField(max_length=300)
    about_description = models.TextField()
    about_image = models.ImageField(upload_to='uploads/about_us')
    video_thumbnail = models.ImageField(upload_to='uploads/about_us')
    video_url = models.URLField()
    phone_no = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'About Us page content'

    def __str__(self):
        return self.about_title
