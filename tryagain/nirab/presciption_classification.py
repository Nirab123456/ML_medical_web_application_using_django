from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import MedicationDetails,Medication,Classify_Drug_Class,Classify_Side_Effect,Classify_CONTRADICTIONS
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION():

    def __init__(self, request):
        self.request = request

    def get_presciption_classification(self):
        drug_class_groups = self.get_drug_class_classification()
        side_effect_groups = self.get_side_effect_classification()
        contraindication_groups = self.get_contraindication_classification()
        all_groups = []

        for drug_group in drug_class_groups:
            name = drug_group['name']
            merged_group = drug_group.copy()

            if side_effect_groups:
                for side_effect_group in side_effect_groups:
                    if side_effect_group['name'] == name:
                        print('i am here')
                        merged_group['side_effect_group'] = side_effect_group['group']
                        merged_group['side_effect_indication'] = side_effect_group['indication']
                        merged_group['side_effect_score'] = side_effect_group['score']
                    else:
                        continue

            if contraindication_groups:
                for contraindication_group in contraindication_groups:
                    if contraindication_group['name'] == name:
                        print('i am here')
                        merged_group['contraindication_group'] = contraindication_group['group']
                        merged_group['contraindication_indication'] = contraindication_group['indication']
                        merged_group['contraindication_result'] = contraindication_group['contraindication_result']
                        merged_group['contraindication_score'] = contraindication_group['score']
                    else:
                        continue


            all_groups.append(merged_group)
        print(f'all_groups: {all_groups}')
        
        # for drug_group in drug_class_groups:
        #     name = drug_group['name']
        #     merged_group = drug_group.copy()

        #     if side_effect_groups:
        #         for side_effect_group in side_effect_groups:
        #             if side_effect_group['name'] == name:
        #                 print('i am here')
        #                 merged_group['side_effect_group'] = side_effect_group['group']
        #                 merged_group['side_effect_indication'] = side_effect_group['indication']
        #                 merged_group['side_effect_score'] = side_effect_group['score']
        #             else:
        #                 continue


        #     all_groups.append(merged_group)
        # print(f'all_groups: {all_groups}')

        if all_groups:
            return JsonResponse(all_groups, safe=False)
        else:
            return JsonResponse({}, safe=False)

    def get_drug_class_classification(self):
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
                                # 'drug_class': drug_class_detail.drug_class,
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

        if all_groups:
            # Concatenate the inner dictionaries' 'group', 'indication', and 'score' fields while maintaining the order
            for i in range(len(all_groups)):
                combined_group = ','.join(d['group'] for d in all_groups[i])
                combined_indication = ','.join(d['indication'] for d in all_groups[i])
                combined_score = ','.join(d['score'] for d in all_groups[i])
                all_groups[i] = {
                    'name': all_groups[i][0]['name'],
                    'group': combined_group,
                    'indication': combined_indication,
                    # 'drug_class': all_groups[i][0]['drug_class'],
                    'score': combined_score,
                }
            return all_groups
        else:
            return []
            
    def get_side_effect_classification(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names
        side_effect_details_list = []
        grouped_by_name = {}
        grouped_list = []
        all_groups = []

        for name in names_list:
            name = name.lower().strip()  # Use strip() to remove leading/trailing spaces
            generic_name_object = Medication.objects.filter(name=name).first()
            if generic_name_object is not None:
                generic_name = generic_name_object.generic_name
                side_effect_details = Classify_Side_Effect.objects.filter(generic_name=generic_name)
                if side_effect_details:
                    for side_effect_detail in side_effect_details:
                        details = {
                            'name': name,
                            'group': side_effect_detail.group,
                            'indication': side_effect_detail.indication,
                            # 'side_effect': side_effect_detail.side_effect,
                            'score': str(side_effect_detail.score),
                        }
                        side_effect_details_list.append(details)
        # print(f'length of side_effect_details_list: {len(side_effect_details_list)}')

        if side_effect_details_list:
            for side_effect_detail in side_effect_details_list:
                name = side_effect_detail['name']
                # Check if the 'name' already exists in the grouped dictionary
                if name in grouped_by_name:
                    # If the 'name' already exists, append the current dictionary to the list
                    grouped_by_name[name].append(side_effect_detail)
                else:
                    # If the 'name' is not yet in the grouped dictionary, create a new list with the current dictionary
                    grouped_by_name[name] = [side_effect_detail]

        # print(f'grouped_by_name: {grouped_by_name}')
        


        if grouped_by_name:
            all_groups = list(grouped_by_name.values())

        if all_groups:
            # Concatenate the inner dictionaries' 'group', 'indication', and 'score' fields while maintaining the order
            for i in range(len(all_groups)):
                combined_group = ','.join(d['group'] for d in all_groups[i])
                combined_indication = ','.join(d['indication'] for d in all_groups[i])
                combined_score = ','.join(d['score'] for d in all_groups[i])
                all_groups[i] = {
                    'name': all_groups[i][0]['name'],
                    'group': combined_group,
                    'indication': combined_indication,
                    # 'side_effect': all_groups[i][0]['side_effect'],
                    'score': combined_score,
                }

            return all_groups
        else:
            return []




    def get_contraindication_classification(self):
        request = self.request
        names = request.GET.get('name', '')  # Get the comma-separated names as a single string
        names_list = names.split(',')  # Split the string into a list of names
        contraindication_details_list = []
        grouped_by_name = {}
        grouped_list = []
        all_groups = []

        for name in names_list:
            name = name.lower().strip()
            generic_name_object = Medication.objects.filter(name=name).first()
            if generic_name_object is not None:
                generic_name = generic_name_object.generic_name
                contraindication_details = Classify_CONTRADICTIONS.objects.filter(generic_name=generic_name)
                if contraindication_details:
                    for contraindication_detail in contraindication_details:
                        details = {
                            'name': name,
                            'group': contraindication_detail.group,
                            'indication': contraindication_detail.indication,
                            # 'contraindication': contraindication_detail.contraindication,
                            'contraindication_result': contraindication_detail.contraindication_result,
                            'score': str(contraindication_detail.score),
                        }
                        contraindication_details_list.append(details)
        # print(f'length of contraindication_details_list: {len(contraindication_details_list)}')

        if contraindication_details_list:
            for contraindication_detail in contraindication_details_list:
                name = contraindication_detail['name']
                # Check if the 'name' already exists in the grouped dictionary
                if name in grouped_by_name:
                    # If the 'name' already exists, append the current dictionary to the list
                    grouped_by_name[name].append(contraindication_detail)
                else:
                    # If the 'name' is not yet in the grouped dictionary, create a new list with the current dictionary
                    grouped_by_name[name] = [contraindication_detail]

        # print(f'grouped_by_name: {grouped_by_name}')

        if grouped_by_name:
            all_groups = list(grouped_by_name.values())

        if all_groups:
            # Concatenate the inner dictionaries' 'group', 'indication', and 'score' fields while maintaining the order
            for i in range(len(all_groups)):
                combined_group = ','.join(d['group'] for d in all_groups[i])
                combined_indication = ','.join(d['indication'] for d in all_groups[i])
                combined_score = ','.join(d['score'] for d in all_groups[i])
                all_groups[i] = {
                    'name': all_groups[i][0]['name'],
                    'group': combined_group,
                    'indication': combined_indication,
                    # 'contraindication': all_groups[i][0]['contraindication'],
                    'contraindication_result': all_groups[i][0]['contraindication_result'],
                    'score': combined_score,
                }

            return all_groups
        else:
            return []



        # return side_effect_details_list  # Move the return statement outside the loop
