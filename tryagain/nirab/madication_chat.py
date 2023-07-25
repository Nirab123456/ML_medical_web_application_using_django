from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication,Classify_Drug_Class,Classify_Side_Effect,Classify_CONTRADICTIONS
from django.http import JsonResponse




class MEDICINE_CHAT():

    def __init__(self, request):
        self.request = request


    def get_medicine_details(self):
        request = self.request
        name = request.GET.get('name')
        name = name.lower()
        generic_name = Medication.objects.filter(name=name).first()
        if generic_name:
            details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name.generic_name)
            if details_of_medicine.exists():
                details_list = []
                for detail in details_of_medicine:
                    details = {
                        'generic_name': detail.generic_name,
                        'drug_class': detail.drug_class,
                        'indication': detail.indication,
                        'indication_description': detail.indication_description,
                        'therapeutic_class_description': detail.therapeutic_class_description,
                        'pharmacology_description': detail.pharmacology_description,
                        'dosage_description': detail.dosage_description,
                        'interaction_description': detail.interaction_description,
                        'contraindications_description': detail.contraindications_description,
                        'side_effects_description': detail.side_effects_description,
                    }
                    details_list.append(details)
                return JsonResponse(details_list, safe=False)
            else:
                return JsonResponse({'error': 'Medication details not found'}, status=404)
        else:
            return JsonResponse({'error': 'Medication not found'}, status=404)
        