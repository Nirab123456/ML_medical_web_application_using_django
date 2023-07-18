from django.core.management.base import BaseCommand
from ...models import Medication
import csv

class Command(BaseCommand):
    name = 'import_medication'

    help = 'Import medication data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='django.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = Medication(
                    name=row['name'],
                    dosage_form=row['dosage_form'],
                    generic_name=row['generic_name'],
                    strength=row['strength'],
                    manufacturer=row['manufacturer'],
                    price=row['price'],
                    price_analysis=row['price_analysis'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
