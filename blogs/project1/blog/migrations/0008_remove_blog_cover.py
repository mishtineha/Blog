# Generated by Django 3.2.dev20200701050043 on 2020-11-02 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='cover',
        ),
    ]