# Generated by Django 3.0 on 2021-07-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footersettings',
            options={'verbose_name_plural': 'Footer Settings'},
        ),
        migrations.AlterModelOptions(
            name='topbarsettings',
            options={'verbose_name_plural': 'Top Bar Settings'},
        ),
    ]