# Generated by Django 3.1.1 on 2020-10-14 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categorey',
        ),
    ]
