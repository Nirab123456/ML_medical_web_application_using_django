from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm , addrecord , VenueForm , EventForm , OCRImageForm,Mail_me_Form,profilepicForm,BlogForm,SocialMediaForm,ChangePasswordForm,MedicineForm
from . models import Record , Event , EventVenue , EventAttendee , RecordImage,Record_mail_me,Post,SocialMedia,Medication,MedicationDetails
from django.http import JsonResponse
from django.core.paginator import Paginator








class TOTAL_MEDICINE_SEARCH:
    def __init__(self, request):
        self.request = request

    def med_search(self):
        request = self.request
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                name = name.lower()
                matching_medications = Medication.objects.filter(name__icontains=name)
                strengths = Medication.objects.filter(name=name).values_list('strength', flat=True)
                strengths = set(strengths)
                # Convert the result to a list
                strengths = list(strengths)
                dosage_forms = Medication.objects.filter(name=name).values_list('dosage_form', flat=True)
                dosage_forms = set(dosage_forms)
                # Convert the result to a list
                dosage_forms = list(dosage_forms)
                return render(request, 'search.html', {'medication_form': form, 'medications': matching_medications,
                                                            'strengths': strengths, 'name_of_medication': name, 'dosage_forms': dosage_forms})
        else:
            form = MedicineForm()
        return render(request, 'search.html', {'medication_form': form})



    def get_medication_details(self):
        request = self.request
        selected_strength = request.GET.get('strength')
        name = request.GET.get('name')
        name = name.lower()
        dosage_form = request.GET.get('dosage_form')
        generic_name = Medication.objects.filter(name=name,strength=selected_strength).first().generic_name
        medications = Medication.objects.filter(strength=selected_strength, generic_name=generic_name, dosage_form=dosage_form)
        if medications.exists():
            medication_details = []
            for medication in medications:
                details = {
                    'name': medication.name.strip().capitalize(),
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
        



    # def send_page_object(self):
    #     request = self.request
    #     medication_details = self.medication_details
    #     print(f'len of medication details : {len(medication_details)}')
    #     print(f'medication details :{medication_details}')
    #     items_per_page =10
    #     paginator = Paginator(medication_details, items_per_page)
    #     page_number = self.request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     self.page_obj = page_obj
    #     print('my name is nirab')
    #     return render (request,'search_results.html',{'page_obj': page_obj})  

