# Generated by Django 3.2.dev20200701050043 on 2020-11-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default=None, null=True, upload_to='files/'),
        ),
    ]
