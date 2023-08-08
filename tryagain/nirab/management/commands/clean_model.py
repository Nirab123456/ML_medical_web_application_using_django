
# # Now you can import the models from the Django app
# from ...models import Classify_Side_Effect,Classify_CONTRADICTIONS,Classify_Drug_Class
# from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#     help = 'Clean data in the Classify_Side_Effect model.'

#     def handle(self, *args, **options):
#         # Get the manager of the model
#         model_manager = Classify_Side_Effect.objects
#         # Call the delete() method on the manager to delete all records
#         model_manager.all().delete()
#         self.stdout.write(self.style.SUCCESS('Data cleaned successfully!'))
