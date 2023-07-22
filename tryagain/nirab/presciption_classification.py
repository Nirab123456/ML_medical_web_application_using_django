from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication,Classify_Drug_Class
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION():

    def __init__(self, request):
        self.request = request

    def get_presciption_classification(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names
        generic_name_list = []
        drug_class_list = []
        drug_class_details_list = []
        new_name_list = []

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            print(f'Name: {name}')
            new_name_list.append(name)
            generic_name_object = Medication.objects.filter(name=name).first()
            print(f'Generic Name OBJECT: {generic_name_object}')
            if generic_name_object is not None:
                generic_name = generic_name_object.generic_name
                print(f'Generic Name: {generic_name}')
                generic_name_list.append(generic_name)
                drug_class_object = MedicationDetails.objects.filter(generic_name=generic_name).first()
                print(f'Drug Class Object: {drug_class_object}')
                if drug_class_object:
                    drug_class = drug_class_object.drug_class
                    drug_class_list.append(drug_class)
                    drug_class_details = Classify_Drug_Class.objects.filter(drug_class=drug_class)
                    if drug_class_details:
                        for drug_class_detail in drug_class_details:
                            details = {
                                'name': name,
                                'group': drug_class_detail.group,
                                'indication': drug_class_detail.indication,
                                'drug_class': drug_class_detail.drug_class,
                                'score': str(drug_class_detail.score),
                            }
                            drug_class_details_list.append(details)
            else:
                continue

        if drug_class_details_list:
            return JsonResponse(drug_class_details_list, safe=False)
        else:
            return JsonResponse([], safe=False)
        