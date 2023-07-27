from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication,Classify_Drug_Class,Classify_Side_Effect,Classify_CONTRADICTIONS,med_Ques_Ans
from django.http import JsonResponse
from transformers import pipeline




class MEDICINE_CHAT():

    def __init__(self, request):
        self.request = request


    def get_medicine_details(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names
        question = request.GET.get('question')
        question = question.lower()
        print(f'type(question): {question}')
        if question == 'null' :
            self.selected_question = request.GET.get('selected_question')
            print(f'self.selected_question: {self.selected_question}')
        else:
            topic = request.GET.get('topic')
            answer_list = []

            for name in names_list:
                name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
                generic_name_object = Medication.objects.filter(name=name).first()
                if generic_name_object is not None:
                    generic_name = generic_name_object.generic_name
                    if generic_name:
                        question = question.replace(name, generic_name)
                        details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name)

                        if details_of_medicine.exists():
                            topic_field_map = {
                                'indication_description': 'indication_description',
                                'therapeutic_class_description': 'therapeutic_class_description',
                                'pharmacology_description': 'pharmacology_description',
                                'dosage_description': 'dosage_description',
                                'interaction_description': 'interaction_description',
                                'contraindications_description': 'contraindications_description',
                                'side_effects_description': 'side_effects_description',
                            }

                            topic_field = topic_field_map.get(topic)

                            if topic_field:
                                field_value = details_of_medicine.values_list(topic_field, flat=True).first()

                                if field_value:
                                    replay = self.init_chat_model(topic=field_value, question=question)
                                    answer = replay['answer']
                                    answer = answer.replace(generic_name, name)
                                    response_data = {'answer': answer, 'name': name, 'generic_name': generic_name}
                                    print(f'response_data: {response_data}')



                                    med_question_answer = med_Ques_Ans.objects.create(
                                        name=name,
                                        generic_name=generic_name,
                                        question=question,
                                        answer=answer,
                                        corrected_answer=answer  # You can modify this field as needed
                                    )




                                    answer_list.append(response_data)
            
            if answer_list:
                print(f'answer_list: {answer_list}')
                return JsonResponse(answer_list, status=200,safe=False)
            
            return JsonResponse({'error': 'Medication details not found'}, status=404)
        

    def get_selected_question(self):
        question =self.selected_question
        print(f'question: {question}')

    



    def init_chat_model(self,topic,question):
        tqa = pipeline(task="question-answering",model='deepset/bert-large-uncased-whole-word-masking-squad2',device=0)
        data = tqa(question=question,context=topic)
        return data
    











    # def get_medicine_details(self):
    #     request = self.request
    #     name = request.GET.get('name')
    #     name = name.lower()
    #     print(f'name: {name}')
    #     question = request.GET.get('question')
    #     question = question.lower()
    #     print(f'question: {question}')
    #     generic_name = Medication.objects.filter(name=name).first()
    #     topic = request.GET.get('topic')
    #     if generic_name:
    #         question = question.replace(name, generic_name.generic_name)
    #         details_of_medicine = MedicationDetails.objects.filter(generic_name=generic_name.generic_name)

    #         if details_of_medicine.exists():
    #             topic_field_map = {
    #                 'indication_description': 'indication_description',
    #                 'dosage_description': 'dosage_description',
    #                 'interaction_description': 'interaction_description',
    #                 'contraindications_description': 'contraindications_description',
    #                 'side_effects_description': 'side_effects_description',
    #             }

    #             topic_field = topic_field_map.get(topic)

    #             if topic_field:
    #                 field_value = details_of_medicine.values_list(topic_field, flat=True).first()

    #                 if field_value:
    #                     replay = self.init_chat_model(topic=field_value, question=question)
    #                     answer = replay['answer']
    #                     answer = answer.replace(generic_name.generic_name, name)
    #                     response_data = {'answer': answer}
    #                     med_question_answer = med_Ques_Ans.objects.create(
    #                         name=name,
    #                         generic_name=generic_name.generic_name,
    #                         question=question,
    #                         answer=answer,
    #                         corrected_answer=answer  # You can modify this field as needed
    #                     )
    #                     return JsonResponse(response_data, status=200)

    #             return JsonResponse({'error': 'Medication details not found for the given topic'}, status=404)

    #         return JsonResponse({'error': 'Medication details not found'}, status=404)

    #     return JsonResponse({'error': 'Medication not found'}, status=404)



