from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication
from django.http import JsonResponse
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

# pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple",device=0) # pass device=0 if using gpu


class PRESCIPTION_CLASSIFICATION():

    def __init__(self, request):
        self.request = request
        self.pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple",device=0) # pass device=0 if using gpu
        self.result_geoup_list=['Sign_symptom','Medication','Therapeutic_procedure','Disease_disorder']


    def get_presciption_classification(self):
        names = self.request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names

        print(f'all names: {names_list}')
        all_details = []  # List to store details of all medications

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            generic_name = Medication.objects.filter(name=name).first()

            if generic_name:
                details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name.generic_name)
                if details_of_medicine.exists():
                    for detail in details_of_medicine:
                        details = {
                            'name': name,
                            'generic_name': detail.generic_name,
                            'drug_class': detail.drug_class,
                            'indication': detail.indication,
                        }
                        all_details.append(details)
                        self.all_details = all_details
                        self.classify_presciption_drugs()



                        # duplicate_indices = self.compare_presciption_drugs()
                        # if duplicate_indices:
                        #     for i, j in duplicate_indices:
                        #         print(f"Duplicates found between dictionary {i} and dictionary {j}.")
                        #         print("Details for dictionary", i, ":", all_details[i])
                        #         print("Details for dictionary", j, ":", all_details[j])
                        #         print("Generic Name:", all_details[i]['generic_name'])
                        #         print("Drug Class:", all_details[i]['drug_class'])
                        #         print("Indication:", all_details[i]['indication'])
                        #         print()
            else:
                # If medication details not found, continue to the next name
                continue

        if all_details:
            return JsonResponse(all_details, safe=False)
        else:
            # If no medication details found for any name, return an empty list
            return JsonResponse([], safe=False)
        

    def compare_presciption_drugs(self):
        all_details = self.all_details
        duplicates = []
        for i in range(len(all_details)):
            for j in range(i+1, len(all_details)):
                if (all_details[i]['generic_name'] == all_details[j]['generic_name'] or
                    all_details[i]['drug_class'] == all_details[j]['drug_class'] or
                    all_details[i]['indication'] == all_details[j]['indication']):
                    duplicates.append((i, j))
        return duplicates
    
    def classify_presciption_drugs(self):
        all_details = self.all_details
        for detail in all_details:
            print(f'detail: {detail}')
            # Access the 'drug_class' value from the dictionary
            drug_class_string = detail['drug_class']

            print(f'drug_class_string: {drug_class_string}')
            results=self.pipe(drug_class_string)
            for result in results:
                if result['entity_group'] in self.result_geoup_list:
                    if len(result['word']) >= 4 and '#' not in result['word']:
                        print(f"Entity: {result['entity_group']}")
                        print(f"Score: {result['score']}")
                        print(f"Word: {result['word']}")
                        print()
