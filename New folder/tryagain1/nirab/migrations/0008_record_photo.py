# Generated by Django 4.2.2 on 2023-07-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nirab', '0007_record_mail_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]