from django.core.management.base import BaseCommand
from ...models import Classify_Drug_Class
import csv

class Command(BaseCommand):
    name = 'side_effects'

    help = 'Import drug class data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='side_effects.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = Classify_Drug_Class(
                    group=row['group'],
                    indication=row['indication'],
                    score=row['Score'],
                    drug_class=row['drug_class'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
