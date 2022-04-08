
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


#    How many students are there?
print(f"1. there are {len(students)} students \n")

#    How many students prefer light coffee? For each type of coffee roast?
prefer_light = [s for s in students if s['coffee_preference']=='light']
print(f"2a. {len(prefer_light)} student prefer light coffee \n")
prefer_medium = [s for s in students if s['coffee_preference']=='medium']
prefer_dark = [s for s in students if s['coffee_preference']=='dark']
print(f"2b. {len(prefer_light)} student prefer light coffee, {len(prefer_medium)} prefer medium coffee, and {len(prefer_dark)} prefer dark coffee.\n")

#    How many types of each pet are there?
types_of_pets = ['cat', 'dog', 'horse']
print("3. ")

#    How many grades does each student have? Do they all have the same number of grades?
num_grades_per_student = [len(s['grades']) for s in students]
print(f"4a. The distribution of the number of grades is {num_grades_per_student}\n")
grade_set = set(num_grades_per_student)
same_num_grades = None
if len(grade_set)==1:
    same_num_grades=True
else:
    same_num_grades=False
print(f"4b. 'Every student has the same number of grades' is a {same_num_grades} statement\n")

#    What is each student's grade average?
get_avg = lambda nums: sum(nums)/len(nums)
student_avgs = [{'student':s['student'], 'avg':get_avg(s['grades'])} for s in students]
avg_msg = ""
for s in student_avgs:
    avg_msg += f"\t{s['student']} has an average of {s['avg']}.\n"
print(f"5. {avg_msg}")

#    How many pets does each student have?
student_pets = [{'student':s['student'], 'num_pets':len(s['pets'])} for s in students]
pet_msg = ""
for s in student_pets:
    pet_msg += f"\t{s['student']} has {s['num_pets']} pet(s).\n"
print(f"6. {pet_msg}")

#    How many students are in web development? data science?
data_science_students = [s for s in students if s['course']=='data science']
web_dev_students = [s for s in students if s['course']=='web development']
print(f"7. There are {len(web_dev_students)} web dev students and {len(data_science_students)} data science student\n")

#    What is the average number of pets for students in web development?
web_dev_pets = [len(s['pets']) for s in students if s['course']=='web development']
web_dev_avg_pets = sum(web_dev_pets)/len(web_dev_pets)
print(f"8. Web dev students have an average of {web_dev_avg_pets} pets.\n")

#    What is the average pet age for students in data science?
data_science_students = [s for s in students if s['course']=='data science']
ds_pets = []
for s in data_science_students:
    for p in s['pets']:
        ds_pets.append(p)
pet_ages = [p['age'] for p in ds_pets]
pet_avg_age = sum(pet_ages)/len(pet_ages)
print(f"9. The average age of the pets of data scientist is {pet_avg_age}")

#    What is most frequent coffee preference for data science students?
coffee_prefs = ['light', 'medium', 'dark']
ds_coffee_prefs_num = [
    len([s for s in students if s['coffee_preference']=='light' and s['course']=='data science']),
    len([s for s in students if s['coffee_preference']=='medium' and s['course']=='data science']),
    len([s for s in students if s['coffee_preference']=='dark' and s['course']=='data science'])
]
ds_coffee_pref_max = coffee_prefs[ds_coffee_prefs_num.index(max(ds_coffee_prefs_num))]
print(f"10. The most frequent coffee preference for DS students is {ds_coffee_pref_max}")

#    What is the least frequent coffee preference for web development students?
coffee_prefs = ['light', 'medium', 'dark']
wd_coffee_prefs_num = [
    len([s for s in students if s['coffee_preference']=='light' and s['course']=='web development']),
    len([s for s in students if s['coffee_preference']=='medium' and s['course']=='web development']),
    len([s for s in students if s['coffee_preference']=='dark' and s['course']=='web development'])
]
wd_coffee_pref_min = coffee_prefs[wd_coffee_prefs_num.index(min(wd_coffee_prefs_num))]
print(f"10. The least frequent coffee preference for Web Dev students is {wd_coffee_pref_min}")


#    What is the average grade for students with at least 2 pets?
students_with_two_pets = [s for s in students if len(s['pets'])>=2]
get_avg = lambda nums: sum(nums)/len(nums)
student_pets_avgs = [get_avg(s['grades']) for s in students_with_two_pets]
with_pets_avg = get_avg(student_pets_avgs)
print(f"11. The average grade of students with at least two pets is {with_pets_avg}.\n")

#    How many students have 3 pets?
students_with_three_pets = len([s for s in students if len(s['pets'])==3])
print(f"12. {students_with_three_pets} student(s) have three pets.")

#    What is the average grade for students with 0 pets?
students_with_no_pets = [s for s in students if len(s['pets'])==0]
get_avg = lambda nums: sum(nums)/len(nums)
student_no_pets_avgs = [get_avg(s['grades']) for s in students_with_no_pets]
with_no_pets_avg = get_avg(student_no_pets_avgs)
print(f"13. The average grade of students with at least two pets is {with_no_pets_avg}.\n")

#    What is the average grade for web development students? data science students?
wd_students = [s for s in students if s['course']=='web development']
get_avg = lambda nums: sum(nums)/len(nums)
wd_students_avgs = [get_avg(s['grades']) for s in wd_students]
wd_avg = get_avg(wd_students_avgs)
data_science_students = [s for s in students if s['course']=='data science']
get_avg = lambda nums: sum(nums)/len(nums)
ds_students_avgs = [get_avg(s['grades']) for s in data_science_students]
ds_avg = get_avg(ds_students_avgs)
print(f"13a. The average grade of web dev students is {wd_avg}.\n")
print(f"13b. The average grade of data science students is {ds_avg}.\n")

#    What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dark_coffee_drinkers = [s for s in students if s['coffee_preference']=='dark']
get_avg = lambda nums: sum(nums)/len(nums)
dark_coffee_avgs = [get_avg(s['grades']) for s in dark_coffee_drinkers]
dark_coffee_range = max(dark_coffee_avgs) - min(dark_coffee_avgs)
print(f"14. The range of grades for dark coffee drinkers is {dark_coffee_range}.\n")

#    What is the average number of pets for medium coffee drinkers?
#    What is the most common type of pet for web development students?
#    What is the average name length?
#    What is the highest pet age for light coffee drinkers?
