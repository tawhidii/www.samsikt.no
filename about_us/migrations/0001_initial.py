# Generated by Django 3.0 on 2021-07-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_banner', models.ImageField(help_text='Insert about us banner', upload_to='uploads/about_us')),
                ('about_title', models.CharField(max_length=300)),
                ('about_description', models.TextField()),
                ('about_image', models.ImageField(upload_to='uploads/about_us')),
                ('video_thumbnail', models.ImageField(upload_to='uploads/about_us')),
                ('video_url', models.URLField()),
                ('phone_no', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'About Us page content',
            },
        ),
        migrations.CreateModel(
            name='TeamBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams_banner', models.ImageField(help_text='Insert Team banner', upload_to='uploads/about_us')),
            ],
            options={
                'verbose_name_plural': 'Team Upper banner section',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter team member name', max_length=100)),
                ('team_image', models.ImageField(upload_to='uploads/teams')),
                ('designation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Team Section',
            },
        ),
    ]
