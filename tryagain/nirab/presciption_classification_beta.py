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
                    if drug_class_details is not None:
                        for drug_class_detail in drug_class_details:
                            if drug_class_detail.heading == drug_class_detail.drug_class:
                                details = {
                                    'name': name,
                                    'heading': drug_class_detail.heading,
                                }
                                drug_class_details_list.append(details)
                            else:
                                details = {
                                    'name': name,
                                    'heading': drug_class_detail.heading,
                                    'specific_class': drug_class_detail.drug_class,
                                }
                                drug_class_details_list.append(details)
        print(f'drug_class_details_list: {drug_class_details_list}')
        if drug_class_details_list:
            for drug_class_detail in drug_class_details_list:
                name = drug_class_detail['name']
                # Check if the 'name' already exists in the grouped dictionary
                if name in grouped_by_name:
                    # If the 'name' already exists, append the current dictionary to the list
                    grouped_by_name[name].append(drug_class_detail)
                else:
                    # If the 'name' is not yet in the grouped dictionary, create a new list with the current dictionary
                    grouped_by_name[name] = [drug_class_detail]
        
        if grouped_by_name:
            all_groups = list(grouped_by_name.values())
                            
        if all_groups:
            # Concatenate the inner dictionaries' 'heading' and 'specific_class' fields while maintaining the order
            for i in range(len(all_groups)):
                combined_heading = ','.join([d['heading'] for d in all_groups[i]])
                specific_class_list = [d.get('specific_class', '') for d in all_groups[i]]  # Get the value or empty string if key is missing
                combined_specific_class = ','.join(specific_class_list)
                if combined_specific_class:
                    all_groups[i] = {
                        'name': all_groups[i][0]['name'],
                        'heading': combined_heading,
                        'specific_class': combined_specific_class,
                    }
                else:
                    all_groups[i] = {
                        'name': all_groups[i][0]['name'],
                        'heading': combined_heading,
                    }
        print(f'all_groups: {all_groups}')
        return all_groups

            
    def get_side_effect_classification(self):
        pass


    def get_contraindication_classification(self):
        pass