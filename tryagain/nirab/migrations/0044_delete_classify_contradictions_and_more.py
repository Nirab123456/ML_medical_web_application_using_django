# Generated by Django 4.2.2 on 2023-08-08 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nirab', '0043_presciption_drug_class'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classify_CONTRADICTIONS',
        ),
        migrations.DeleteModel(
            name='Classify_Drug_Class',
        ),
        migrations.DeleteModel(
            name='Classify_Side_Effect',
        ),
    ]
