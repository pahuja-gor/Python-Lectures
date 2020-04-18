#Name: Jamie
#Age: 28
#Salary: 22500
#Occupation: Student
#Name: Jill
#Age: 30
#Salary: 80000
#Occupation: Professor

#Name,Age,Salary,Occupation
#Jamie,28,22500,Student
#Jill,30,80000,Professor

import csv
import json

def create_person_csv(csv_data):
    person = {}
    person["name"] = csv_data[0]
    person["age"] = int(csv_data[1])
    person["salary"] = int(csv_data[2])
    person["occupation"] = csv_data[3]
    return person

list_of_csv_people = []
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    counter = 0
    for row in csv_reader:
        #print(row)
        if counter != 0:
            list_of_csv_people.append(create_person_csv(row))
        counter += 1
# print(list_of_csv_people)

# with open("data.json", "w") as output_file:
#     json.dump(list_of_csv_people, output_file)

with open("data.json") as json_file:
    list_of_json_people = json.load(json_file)

# def create_person(person_data):
#     person = {}
#     person["name"] = person_data[0].split(":")[1].strip()
#     person["age"] = int(person_data[1].split(":")[1].strip())
#     person["salary"] = int(person_data[2].split(":")[1].strip())
#     person["occupation"] = person_data[1].split(":")[1].strip()
#
# list_of_people = []
#
# with open("data.txt") as my_data_file:
#     counter = 0
#     person = []
#     for line in my_data_file:
#         person.append(line)
#         counter += 1
#         if counter == 4:
#             list_of_people.append(create_person(person))
#             counter = 0
#             person = []