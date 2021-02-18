# D9 Excerise 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# D9 Excerise 2
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, num_of_visits, city):
#     new_entry = {}
#     new_entry["country"] = country
#     new_entry["visits"] = num_of_visits
#     new_entry["cities"] = city
#     travel_log.append({new_entry})
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# D9 Project Silent Auction
# from art import logo