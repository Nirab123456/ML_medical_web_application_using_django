from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Presciption_drug_class,SELECTED_QUESTION_ANSWER,Medication
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION_BETA():

    def __init__(self, request):
        self.request = request


    def get_presciption_classification(self):
        x=self.calculate_drug_class_match()
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

        return merged_groups
        

    def calculate_drug_class_match(self):
        print("calculate_drug_class_match() function started")
        drug_class_groups_list = self.get_drug_class_classification()
        all_list = []
        all_matching_list = []

        if drug_class_groups_list is not None:
            for drug_class_group in drug_class_groups_list:
                name = drug_class_group['name']
                headings = drug_class_group['heading'].split(',')
                specific_class = drug_class_group['specific_class'].split(',')

                # Combine nested list
                combined_list = [name, headings, specific_class]
                all_list.append(combined_list)

        # Now, let's check for matches between each pair of lists in all_list
        for i in range(len(all_list)):
            name1, headings1, specific_class1 = all_list[i]
            for j in range(i + 1, len(all_list)):
                name2, headings2, specific_class2 = all_list[j]

                # Check for matches between headings and specific_class for the current pair of lists
                heading_matches = set(headings1) & set(headings2)
                specific_class_matches = set(specific_class1) & set(specific_class2)

                # If there are matches, add them to the all_matching_list
                if heading_matches or specific_class_matches:
                    all_matching_list.append({
                        'name1': name1,
                        'name2': name2,
                        'heading_matches': list(heading_matches),
                        'specific_class_matches': list(specific_class_matches)
                    })

        print("calculate_drug_class_match() function completed")
        print(f'all_matching_list: {all_matching_list}')
        return all_matching_list














        # drug_sets = [self.create_class_set(drug['heading']) for drug in drug_class_groups_list]
        # print(f'drug_sets: {drug_sets}')
        # matching_indices = {}
        # for i, drug_set in enumerate(drug_sets):
        #     matching_indices[i] = []
        #     for j, other_set in enumerate(drug_sets):
        #         if i != j and sorted(drug_set) == sorted(other_set):
        #             matching_indices[i].append(j)

        # # Collect the matching dictionaries and their matches
        # matched_data = []
        # for i, matches in matching_indices.items():
        #     if matches:
        #         matched_data.append({
        #             'original': drug_class_groups_list[i],
        #             'matches': [drug_class_groups_list[j] for j in matches]
        #         })

        # print("calculate_drug_class_match() function completed")
        # return matched_data


    def get_side_effect_classification(self):
        pass


    def get_contraindication_classification(self):
        pass