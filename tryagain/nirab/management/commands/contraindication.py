from django.core.management.base import BaseCommand
from ...models import Classify_CONTRADICTIONS
import csv

class Command(BaseCommand):
    name = 'contradiction'

    help = 'Import drug class data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='contraindication.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = Classify_CONTRADICTIONS(
                    generic_name=row['generic_name'],
                    group=row['group'],
                    indication=row['indication'],
                    score=row['score'],
                    contraindication=row['contraindications_description'],
                    contraindication_result=row['contraindication_result'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
