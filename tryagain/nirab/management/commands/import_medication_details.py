from django.core.management.base import BaseCommand
from ...models import MedicationDetails
import csv

class Command(BaseCommand):
    name = 'import_medication_details'

    help = 'Import medication details data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='cleaned_generic_df_main.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = MedicationDetails(
                    generic_name=row['generic_name'],
                    drug_class=row['drug_class'],
                    indication=row['indication'],
                    indication_description=row['indication_description'],
                    therapeutic_class_description=row['therapeutic_class_description'],
                    pharmacology_description=row['pharmacology_description'],
                    dosage_description=row['dosage_description'],
                    interaction_description=row['interaction_description'],
                    contraindications_description=row['contraindications_description'],
                    side_effects_description=row['side_effects_description'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication Details data imported successfully.'))
