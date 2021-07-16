from django.db import models


class AboutUs(models.Model):
    about_us_banner = models.ImageField(upload_to='uploads/about_us', help_text='Insert about us banner')
    about_title = models.CharField(max_length=300, help_text='')
    about_description = models.TextField()
    about_image = models.ImageField(upload_to='uploads/about_us')
    video_thumbnail = models.ImageField(upload_to='uploads/about_us')
    video_url = models.URLField()
    phone_no = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'About Us page content'

    def __str__(self):
        return self.about_title


class Teams(models.Model):
    name = models.CharField(max_length=100, help_text='Enter team member name')
    team_image = models.ImageField(upload_to='uploads/teams')
    designation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Team Section'


class TeamBanner(models.Model):
    teams_banner = models.ImageField(upload_to='uploads/about_us', help_text='Insert Team banner')

    class Meta:
        verbose_name_plural = 'Team Upper banner section'

    def __str__(self):
        return str(self.teams_banner)
    @property
    def get_banner(self):
        return self.teams_banner.url
