from django.core.management.base import BaseCommand
from ...models import SELECTED_QUESTION_ANSWER
import csv

class Command(BaseCommand):
    name = 'selected_question_answer'

    help = 'Import selected_question_answer data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='selected_question_answer.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                medication = SELECTED_QUESTION_ANSWER(
                    generic_name=row['generic_name'],
                    A_T_U_C=row['use_cases'],
                    A_S_E_C=row['side_effects'],
                    A_M_O_C=row['mechanism_of_action'],
                    W_T_A_D_C=row['drug_interactions'],
                    W_T_A_F_C=row['food_interactions'],
                    I_W_C_N_T_T_C=row['contraindications'],
                )
                medication.save()
        self.stdout.write(self.style.SUCCESS('Medication data imported successfully.'))
