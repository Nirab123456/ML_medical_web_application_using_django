from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Presciption_drug_class,SELECTED_QUESTION_ANSWER,Medication
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION_BETA():

    def __init__(self, request):
        self.request = request


    def get_presciption_classification(self):
        pass

    def get_drug_class_classification(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        print(f'names: {names}')
        names_list = names.split(',')  # Split the string into a list of names
        print(f'names_list: {names_list}')
        drug_class_details_list = []
        grouped_by_name = {}
        grouped_list = []
        all_groups = []

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            generic_name_object = Medication.objects.filter(name=name).first()
            if generic_name_object is not None:
                    generic_name = generic_name_object.generic_name
                    print(f'generic_name: {generic_name}')
                    drug_class_details = Presciption_drug_class.objects.filter(generic_name=generic_name)
                    print(f'drug_class_details: {drug_class_details}')
            
    def get_side_effect_classification(self):
        pass


    def get_contraindication_classification(self):
        pass