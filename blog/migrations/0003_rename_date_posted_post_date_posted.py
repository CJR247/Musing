# Generated by Django 5.1.1 on 2024-09-29 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_date_created_post_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Date_posted',
            new_name='date_posted',
        ),
    ]
