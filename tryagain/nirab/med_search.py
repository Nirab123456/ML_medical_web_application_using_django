from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MedicineForm
from . models import Medication,MedicationDetails
from django.http import JsonResponse








class TOTAL_MEDICINE_SEARCH:
    def __init__(self, request):
        self.request = request

    def med_search(self):
        request = self.request
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():

                name = form.cleaned_data['name']
                if name != None:
                    name = name.lower()
                    # matching_medications = Medication.objects.filter(name__icontains=name)
                    matching_medications = Medication.objects.filter(name=name)
                    strengths = matching_medications.values_list('strength', flat=True)
                    strengths = set(strengths)
                    # Convert the result to a list
                    strengths = list(strengths)
                    dosage_forms = matching_medications.values_list('dosage_form', flat=True)
                    dosage_forms = set(dosage_forms)
                    # Convert the result to a list
                    dosage_forms = list(dosage_forms)
                    return render(request, 'trial.html', {'medication_form': form, 'medications': matching_medications,
                                                                'strengths': strengths, 'name_of_medication': name, 'dosage_forms': dosage_forms})

        else:
            form = MedicineForm()
        return render(request, 'trial.html', {'medication_form': form})

    def med_search_generic(self):
        request = self.request
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():

                generic_name = form.cleaned_data['generic_name']

                if generic_name != None :
                    generic_name = form.cleaned_data['generic_name']
                    generic_name = generic_name.lower()
                    matching_medications = Medication.objects.filter(generic_name__icontains=generic_name)
                    strengths = matching_medications.values_list('strength', flat=True)
                    strengths = set(strengths)
                    # Convert the result to a list
                    strengths = list(strengths)
                    dosage_forms = matching_medications.values_list('dosage_form', flat=True)
                    dosage_forms = set(dosage_forms)
                    # Convert the result to a list
                    dosage_forms = list(dosage_forms)
                return render(request, 'trial.html', {'medication_form': form, 'medications': matching_medications,
                                                            'strengths': strengths, 'generic_name': generic_name, 'dosage_forms': dosage_forms})
        else:
            form = MedicineForm()
        return render(request, 'trial.html', {'medication_form': form})



    def get_medication_details(self):
        request = self.request
        selected_strength = request.GET.get('strength')
        print(selected_strength)
        name = request.GET.get('name')
        name = name.lower()
        dosage_form = request.GET.get('dosage_form')
        generic_name = Medication.objects.filter(name=name,strength=selected_strength,dosage_form=dosage_form).first()
        generic_strength_name = Medication.objects.filter(name=name,strength=selected_strength).first()
        generic_dosage_name = Medication.objects.filter(name=name,dosage_form=dosage_form).first()
        if generic_name != None:
            generic_name=generic_name.generic_name
            medications = Medication.objects.filter(strength=selected_strength, generic_name=generic_name, dosage_form=dosage_form)
            if medications.exists():
                medication_details = []
                for medication in medications:
                    details = {
                        'name': medication.name.strip().capitalize(),
                        'strength': medication.strength.strip().capitalize(),
                        'dosage_form': medication.dosage_form.strip().capitalize(),
                        'generic_name': medication.generic_name.strip().capitalize(),
                        'manufacturer': medication.manufacturer.strip().capitalize(),
                        'price': str(medication.price).strip(),
                        'price_analysis': str(medication.price_analysis).strip(),
                        # add any other fields you want to include
                    }
                    medication_details.append(details)
                
                self.medication_details = medication_details

                return JsonResponse(medication_details, safe=False)
            else:
                return JsonResponse({'error': 'Medication not found'}, status=404)
            
        elif generic_strength_name and generic_dosage_name != None:
            full_med_details=[]
            generic_name = generic_strength_name.generic_name
            medications = Medication.objects.filter(strength=selected_strength, generic_name=generic_name)
            if medications.exists():
                for medication in medications:
                    details = {
                        'name': medication.name.strip().capitalize(),
                        'strength': medication.strength.strip().capitalize(),
                        'dosage_form': medication.dosage_form.strip().capitalize(),
                        'generic_name': medication.generic_name.strip().capitalize(),
                        'manufacturer': medication.manufacturer.strip().capitalize(),
                        'price': str(medication.price).strip(),
                        'price_analysis': str(medication.price_analysis).strip(),
                        # add any other fields you want to include
                    }
                    full_med_details.append(details)
                
            generic_name = generic_dosage_name.generic_name
            medications = Medication.objects.filter(dosage_form=dosage_form, generic_name=generic_name)
            if medications.exists():
                for medication in medications:
                    details = {
                        'name': medication.name.strip().capitalize(),
                        'strength': medication.strength.strip().capitalize(),
                        'dosage_form': medication.dosage_form.strip().capitalize(),
                        'generic_name': medication.generic_name.strip().capitalize(),
                        'manufacturer': medication.manufacturer.strip().capitalize(),
                        'price': str(medication.price).strip(),
                        'price_analysis': str(medication.price_analysis).strip(),
                        # add any other fields you want to include
                    }
                    full_med_details.append(details)
                

            return JsonResponse(full_med_details, safe=False)
        


        elif generic_strength_name != None:
            generic_name = generic_strength_name.generic_name
            medications = Medication.objects.filter(strength=selected_strength, generic_name=generic_name)
            if medications.exists():
                medication_details = []
                for medication in medications:
                    details = {
                        'name': medication.name.strip().capitalize(),
                        'strength': medication.strength.strip().capitalize(),
                        'dosage_form': medication.dosage_form.strip().capitalize(),
                        'generic_name': medication.generic_name.strip().capitalize(),
                        'manufacturer': medication.manufacturer.strip().capitalize(),
                        'price': str(medication.price).strip(),
                        'price_analysis': str(medication.price_analysis).strip(),
                        # add any other fields you want to include
                    }
                    medication_details.append(details)
                
                self.medication_details = medication_details

                return JsonResponse(medication_details, safe=False)
        elif generic_dosage_name != None:
            generic_name = generic_dosage_name.generic_name
            medications = Medication.objects.filter(dosage_form=dosage_form, generic_name=generic_name)
            if medications.exists():
                medication_details = []
                for medication in medications:
                    details = {
                        'name': medication.name.strip().capitalize(),
                        'strength': medication.strength.strip().capitalize(),
                        'dosage_form': medication.dosage_form.strip().capitalize(),
                        'generic_name': medication.generic_name.strip().capitalize(),
                        'manufacturer': medication.manufacturer.strip().capitalize(),
                        'price': str(medication.price).strip(),
                        'price_analysis': str(medication.price_analysis).strip(),
                        # add any other fields you want to include
                    }
                    medication_details.append(details)
                
                self.medication_details = medication_details

                return JsonResponse(medication_details, safe=False)




    def get_generic_medication_details(self):
        request = self.request
        selected_strength = request.GET.get('strength')
        print(selected_strength)
        generic_name = request.GET.get('generic_name')
        generic_name = generic_name.lower()
        dosage_form = request.GET.get('dosage_form')
        target_medications = Medication.objects.filter(strength=selected_strength, generic_name__icontains=generic_name, dosage_form=dosage_form)
        strength_medication = Medication.objects.filter(strength=selected_strength, generic_name__icontains=generic_name)
        dosage_medication = Medication.objects.filter(dosage_form=dosage_form, generic_name__icontains=generic_name)
        if target_medications.exists():
            medication_details = []
            for medication in target_medications:
                details = {
                    'name': medication.name.strip().capitalize(),
                    'strength': medication.strength.strip().capitalize(),
                    'dosage_form': medication.dosage_form.strip().capitalize(),
                    'generic_name': medication.generic_name.strip().capitalize(),
                    'manufacturer': medication.manufacturer.strip().capitalize(),
                    'price': str(medication.price).strip(),
                    'price_analysis': str(medication.price_analysis).strip(),
                    # add any other fields you want to include
                }
                medication_details.append(details)

            return JsonResponse(medication_details, safe=False)
        elif strength_medication.exists() and dosage_medication.exists():
            medication_details = []
            for medication in strength_medication:
                details = {
                    'name': medication.name.strip().capitalize(),
                    'strength': medication.strength.strip().capitalize(),
                    'dosage_form': medication.dosage_form.strip().capitalize(),
                    'generic_name': medication.generic_name.strip().capitalize(),
                    'manufacturer': medication.manufacturer.strip().capitalize(),
                    'price': str(medication.price).strip(),
                    'price_analysis': str(medication.price_analysis).strip(),
                    # add any other fields you want to include
                }
                medication_details.append(details)
            for medication in dosage_medication:
                details = {
                    'name': medication.name.strip().capitalize(),
                    'strength': medication.strength.strip().capitalize(),
                    'dosage_form': medication.dosage_form.strip().capitalize(),
                    'generic_name': medication.generic_name.strip().capitalize(),
                    'manufacturer': medication.manufacturer.strip().capitalize(),
                    'price': str(medication.price).strip(),
                    'price_analysis': str(medication.price_analysis).strip(),
                    # add any other fields you want to include
                }
                medication_details.append(details)

            return JsonResponse(medication_details, safe=False)
        elif strength_medication.exists():
            medication_details = []
            for medication in strength_medication:
                details = {
                    'name': medication.name.strip().capitalize(),
                    'strength': medication.strength.strip().capitalize(),
                    'dosage_form': medication.dosage_form.strip().capitalize(),
                    'generic_name': medication.generic_name.strip().capitalize(),
                    'manufacturer': medication.manufacturer.strip().capitalize(),
                    'price': str(medication.price).strip(),
                    'price_analysis': str(medication.price_analysis).strip(),
                    # add any other fields you want to include
                }
                medication_details.append(details)

            return JsonResponse(medication_details, safe=False)
        elif dosage_medication.exists():
            medication_details = []
            for medication in dosage_medication:
                details = {
                    'name': medication.name.strip().capitalize(),
                    'strength': medication.strength.strip().capitalize(),
                    'dosage_form': medication.dosage_form.strip().capitalize(),
                    'generic_name': medication.generic_name.strip().capitalize(),
                    'manufacturer': medication.manufacturer.strip().capitalize(),
                    'price': str(medication.price).strip(),
                    'price_analysis': str(medication.price_analysis).strip(),
                    # add any other fields you want to include
                }
                medication_details.append(details)

            return JsonResponse(medication_details, safe=False)
        else:
            return JsonResponse({'message': 'No medication found'}, status=404)            


    def medicine_details(self):
        request = self.request
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                name = name.lower()
                return render(request, 'search_med_details.html', {'medication_form': form, 'name_of_medication': name})
        else:
            form = MedicineForm()
        return render(request, 'search_med_details.html', {'medication_form': form})

    def medicine_details_generic(self):
        request = self.request
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():
                generic_name = form.cleaned_data['generic_name']
                generic_name = generic_name.lower()
                return render(request, 'search_med_details_generic.html', {'medication_form': form, 'generic_name': generic_name})
        else:
            form = MedicineForm()
        return render(request, 'search_med_details_generic.html', {'medication_form': form})

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


    def get_medicine_details_generic(self):
        request = self.request
        generic_name = request.GET.get('generic_name')
        generic_name = generic_name.lower()
        if generic_name:
            details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name)
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
