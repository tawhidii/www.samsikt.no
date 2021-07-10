from django.db import models


class TopBarSettings(models.Model):
    """
    Model class  for Top Bar settings in Homepage
    """

    phone_number = models.CharField(max_length=20,help_text='Enter Phone number')
    email = models.EmailField(help_text='Enter Email')
    working_hours = models.CharField(max_length=120,help_text='Enter Working hour')

    def __str__(self):
        return f'Phone Number : {self.phone_number} - Email : {self.email}'


class FooterSettings(models.Model):
    footer_post_title = models.CharField(max_length=50,help_text='Give a title')
    footer_logo = models.ImageField(upload_to='uploads/site_settings',help_text='Upload Logo')
    footer_short_about = models.TextField(help_text='Provide footer description and social as markup ')
    footer_contact_details = models.TextField(help_text='Provide footer contact details as markup ')

    def __str__(self):
        return self.footer_post_title
