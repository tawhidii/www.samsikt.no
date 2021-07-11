from django.db import models


class HeroSlider(models.Model):
    sub_title = models.CharField(max_length=150, help_text='Give hero subtitle')
    main_title = models.CharField(max_length=150, help_text='Giver hero main title')
    background_image = models.ImageField(upload_to='uploads/hero', help_text='Upload background image')
    left_animated_image = models.ImageField(upload_to='uploads/hero', help_text='Upload hero left image')
    right_animated_image = models.ImageField(upload_to='uploads/hero', help_text='Upload hero right image')

    class Meta:
        verbose_name_plural = 'Home Hero Slider Settings'

    def __str__(self):
        return f'{self.sub_title} - {self.main_title}'
