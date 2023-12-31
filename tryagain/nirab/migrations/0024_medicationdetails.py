# Generated by Django 4.2.2 on 2023-07-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nirab', '0023_medication_price_analysis_alter_medication_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_name', models.CharField(max_length=500)),
                ('drug_class', models.CharField(max_length=500)),
                ('indication', models.CharField(max_length=500)),
                ('indication_description', models.CharField(max_length=500)),
                ('therapeutic_class_description', models.CharField(max_length=500)),
                ('pharmacology_description', models.CharField(max_length=500)),
                ('dosage_description', models.CharField(max_length=500)),
                ('interaction_description', models.CharField(max_length=500)),
                ('contraindications_description', models.CharField(max_length=500)),
                ('side_effects_description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
