from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Presciption_drug_class,SELECTED_QUESTION_ANSWER,Medication
from django.http import JsonResponse

class PRESCIPTION_CLASSIFICATION_BETA():

    def __init__(self, request):
        self.request = request



    def get_presciption_classification(self):
        drug_class_groups,all_mach_groups,all_mach_groups_2,all_matching_uniques=self.re_match_between_matches()
        # print(f'drug_class_groups: {drug_class_groups}')
        # print(f'all_mach_groups: {all_mach_groups}')
        # print(f'all_mach_groups_2: {all_mach_groups_2}')
        # print(f'all_matching_uniques: {all_matching_uniques}')
        response_data = {}

        if drug_class_groups is not None:
            response_data['drug_class_groups'] = drug_class_groups

        if all_mach_groups is not None:
            response_data['all_mach_groups'] = all_mach_groups

        if all_mach_groups_2 is not None:
            response_data['all_mach_groups_2'] = all_mach_groups_2

        if all_matching_uniques is not None:
            response_data['all_matching_uniques'] = all_matching_uniques

        if response_data:
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({'error': 'No data found'}, status=404)

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
        drug_class_groups_list = self.get_drug_class_classification()
        all_list = []
        all_matching_list = []
        all_combined_list = []

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


        name=[]
        headings=[]
        specific_class=[]
        #get the unique heading_matches ,specific_class_matches
        for all_matching in all_matching_list:
            name1 = all_matching['name1']
            name2 = all_matching['name2']
            heading_matches = all_matching['heading_matches']
            specific_class_matches = all_matching['specific_class_matches']
            name.append(name1)
            name.append(name2)
            headings.append(heading_matches)
            specific_class.append(specific_class_matches)


        name=list(set(name))


        headings = [tuple(sublist) for sublist in headings]
        headings=list(set(headings))
        headings = [item[0] for item in headings]



        specific_class = [tuple(sublist) for sublist in specific_class]
        specific_class=list(set(specific_class))
        specific_class = [item[0] for item in specific_class if item]



        all_combined_list.append(name)
        all_combined_list.append(headings)
        all_combined_list.append(specific_class)







        return all_matching_list,drug_class_groups_list,all_combined_list
    





    def re_match_between_matches(self):
        all_matching_list,drug_class_groups_list,all_combined_list = self.calculate_drug_class_match()
        all_list = []
        all_matching_list2 = []

        if all_matching_list is not None:
            for all_matching in all_matching_list:
                name1 = all_matching['name1']
                name2 = all_matching['name2']
                heading_matches = all_matching['heading_matches']
                specific_class_matches = all_matching['specific_class_matches']

                # Combine nested list
                combined_list = [name1, name2, heading_matches, specific_class_matches]
                all_list.append(combined_list)

        # Now, let's check for matches between each pair of lists in all_list
        for i in range(len(all_list)):
            name1, name2, heading_matches1, specific_class_matches1 = all_list[i]
            for j in range(i + 1, len(all_list)):
                name3, name4, heading_matches2, specific_class_matches2 = all_list[j]

                # Check for matches between headings and specific_class for the current pair of lists
                heading_matches = set(heading_matches1) & set(heading_matches2)
                specific_class_matches = set(specific_class_matches1) & set(specific_class_matches2)

                # If there are matches, add them to the all_matching_list
                if heading_matches or specific_class_matches:
                    if name1 == name3 or name1 == name4 or name2 == name3 or name2 == name4:
                        all_matching_list2.append({
                            'name1': name1,
                            'name2': name2,
                            'heading_matches': list(heading_matches),
                            'specific_class_matches': list(specific_class_matches)
                        })
                        # print(f'1st all_matching_list2: {all_matching_list2}')

                    else:
                        all_matching_list2.append({
                            'name1': name1,
                            'name2': name2,
                            'name3': name3,
                            'name4': name4,
                            'heading_matches': list(heading_matches),
                            'specific_class_matches': list(specific_class_matches)
                        })
                        # print(f'2nd all_matching_list2: {all_matching_list2}')
        #remove duplicates
        all_matching_list2 = [i for n, i in enumerate(all_matching_list2) if i not in all_matching_list2[n + 1:]]
        return drug_class_groups_list,all_matching_list,all_matching_list2,all_combined_list
                            


    def get_side_effect_classification(self):
        pass


    def get_contraindication_classification(self):
        pass