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
        drug_class_details_list = []
        grouped_by_name = {}
        grouped_list = []
        all_groups = []

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            generic_name_object = Medication.objects.filter(name=name).first()
            if generic_name_object is not None:
                generic_name = generic_name_object.generic_name
                drug_class_object = MedicationDetails.objects.filter(generic_name=generic_name).first()
                if drug_class_object:
                    drug_class = drug_class_object.drug_class
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
            print(f'all_groups: {all_groups}')

        if all_groups:
            # Concatenate the inner dictionaries' 'group', 'indication', and 'score' fields
            for i in range(len(all_groups)):
                combined_group = ','.join(set(d['group'] for d in all_groups[i]))
                combined_indication = ','.join(set(d['indication'] for d in all_groups[i]))
                combined_score = ','.join(set(d['score'] for d in all_groups[i]))
                all_groups[i] = {
                    'name': all_groups[i][0]['name'],
                    'group': combined_group,
                    'indication': combined_indication,
                    'drug_class': all_groups[i][0]['drug_class'],
                    'score': combined_score,
                }
            print(f'all_groups 2: {all_groups}')


            return JsonResponse(all_groups, safe=False)
        else:
            return JsonResponse({}, safe=False)
