# Generated by Django 4.2.2 on 2023-07-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nirab', '0029_classify_side_effect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classify_side_effect',
            name='group',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='classify_side_effect',
            name='indication',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='classify_side_effect',
            name='side_effect',
            field=models.TextField(max_length=1000),
        ),
    ]
