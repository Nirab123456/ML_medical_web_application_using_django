from django.core.management.base import BaseCommand
from ...models import Classify_Side_Effect
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
                medication = Classify_Side_Effect(
                    generic_name=row['generic_name'],
                    group=row['group'],
                    indication=row['indication'],
                    score=row['Score'],
                    side_effect=row['side_effects'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
