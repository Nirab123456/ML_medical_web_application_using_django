from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Presciption_drug_class,SELECTED_QUESTION_ANSWER,Medication
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION_BETA():

    def __init__(self, request):
        self.request = request


    def get_presciption_classification(self):
        drug_class_groups = self.get_drug_class_classification()
        if drug_class_groups:
            return JsonResponse(drug_class_groups, safe=False)
        else:
            return JsonResponse({}, safe=False)

                
    def get_drug_class_classification(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names
        drug_class_details_list = []

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            generic_name_object = Medication.objects.filter(name=name).first()
            if generic_name_object is not None:
                generic_name = generic_name_object.generic_name
                drug_class_details = Presciption_drug_class.objects.filter(generic_name=generic_name).distinct()
                if drug_class_details is not None:
                    for drug_class_detail in drug_class_details:
                        details = {
                            'name': name,
                            'heading': drug_class_detail.heading,
                            'specific_class': drug_class_detail.drug_class,
                        }
                        drug_class_details_list.append(details)

        if drug_class_details_list:
            # Create a dictionary to group the drug class details by name
            grouped_by_name = {}
            for drug_class_detail in drug_class_details_list:
                name = drug_class_detail['name']
                if name in grouped_by_name:
                    # If the 'name' already exists, append the current dictionary to the list
                    grouped_by_name[name].append(drug_class_detail)
                else:
                    # If the 'name' is not yet in the grouped dictionary, create a new list with the current dictionary
                    grouped_by_name[name] = [drug_class_detail]

            all_groups = list(grouped_by_name.values())

            # Combine the dictionaries for each name
            merged_groups = []
            for group in all_groups:
                merged_group = {}
                merged_group['name'] = group[0]['name']
                merged_group['heading'] = ','.join([d['heading'] for d in group])
                merged_group['specific_class'] = ','.join([d['specific_class'] for d in group if d['specific_class']])
                merged_groups.append(merged_group)

        print(f'drug_class_list: {merged_groups}')
        return merged_groups
    

    def get_side_effect_classification(self):
        pass


    def get_contraindication_classification(self):
        pass