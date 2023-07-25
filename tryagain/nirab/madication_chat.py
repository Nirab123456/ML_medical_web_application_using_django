from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication,Classify_Drug_Class,Classify_Side_Effect,Classify_CONTRADICTIONS
from django.http import JsonResponse
from transformers import pipeline




class MEDICINE_CHAT():

    def __init__(self, request):
        self.request = request


    def get_medicine_details(self):
        request = self.request
        name = request.GET.get('name')
        name = name.lower()
        question = request.GET.get('question')
        question = question.lower()
        print(f'question: {question}')
        generic_name = Medication.objects.filter(name=name).first()
        topic = request.GET.get('topic')
        print(topic)
        if generic_name:
            question = question.replace(name, generic_name.generic_name)
            print(f'modified question: {question}')
            details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name.generic_name)
            if details_of_medicine.exists():

                if topic == 'indication_description':
                    self.indication_description = details_of_medicine.values_list('indication_description', flat=True)

                    replay = self.init_chat_model(topic=self.indication_description[0],question=question)
                    answer = replay['answer']
                    print(f'answer: {answer}')
                    print(f'indication_replay: {replay}')
                    print(f'indication_description: {self.indication_description}')




        #         details_list = []
        #         for detail in details_of_medicine:
        #             details = {
        #                 'generic_name': detail.generic_name,
        #                 'drug_class': detail.drug_class,
        #                 'indication': detail.indication,
        #                 'indication_description': detail.indication_description,
        #                 'therapeutic_class_description': detail.therapeutic_class_description,
        #                 'pharmacology_description': detail.pharmacology_description,
        #                 'dosage_description': detail.dosage_description,
        #                 'interaction_description': detail.interaction_description,
        #                 'contraindications_description': detail.contraindications_description,
        #                 'side_effects_description': detail.side_effects_description,
        #             }
        #             details_list.append(details)
        #         return JsonResponse(details_list, safe=False)
        #     else:
        #         return JsonResponse({'error': 'Medication details not found'}, status=404)
        # else:
        #     return JsonResponse({'error': 'Medication not found'}, status=404)


    def init_chat_model(self,topic,question):
        tqa = pipeline(task="question-answering",model='deepset/bert-large-uncased-whole-word-masking-squad2',device=0)
        data = tqa(question=question,context=topic)
        return data
