from django.core.management.base import BaseCommand
from ...models import USP_prescription_classification
import csv

class Command(BaseCommand):
    name = 'import_USP_prescription_classification'

    help = 'Import USP prescription classification  data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='django_usp_drug_classification.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = USP_prescription_classification(
                    usp_category=row['usp_category'],
                    usp_class=row['usp_class'],
                    usp_drug=row['usp_drug'],
                    generic_name=row['generic_name'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication Details data imported successfully.'))
