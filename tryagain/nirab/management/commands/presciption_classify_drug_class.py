from django.core.management.base import BaseCommand
from ...models import Presciption_drug_class
import csv

class Command(BaseCommand):
    name = 'presciption_classify_drug_class'

    help = 'Import drug class data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='drug_class.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = Presciption_drug_class(
                    generic_name=row['generic_name'],
                    drug_class=row['cases'],
                    heading=row['head'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
