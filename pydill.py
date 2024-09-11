
# საშინაო დავალება - შექმენით სტუდენტის ობიექტი სახელი, 
# გვარი, დაბადების წელი და ქულა. შექმენით ამ კლასის სამი 
# სხვადასხვა ობიექტი. დაწერეთ ფუნქცია რომელიც არგუმენტად 
# მიიღებს ობიექტს. ჯერ სცდის JSON-თ ჩაწერას თუ პროცესი 
# წარუმატებელი აღმოჩნდა, სცდის pickle-ით ჩაწერას, თუ 
# ფიქლიც წარუმატებელი აღმოჩნდა შემდეგ სცდის Dill-ით 
# ჩაწერას. თუ ვერცერთით ვერ ხდება ჩაწერა დააბრუნოს პასუხი 
# რომ ვერცერთ მეთოდი ვერ ასერიალიზებს გადაცემულ ობიექტს


import json
import pickle
import dill

class Student:
    def __init__(self, first_name, last_name, birth_year, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.grade = grade
        self.some_lambda = lambda x: x * 2  


student1 = Student("Mariam", "Bendeliani", 1991, 98)
student2 = Student("John", "Doe", 2000, 100)
student3 = Student("Jane", "Smith", 2000, 90)

students = [student1, student2, student3]


def serialize_object(obj):
#json serialization
    try:
        json_data = json.dumps([student.__dict__ for student in obj])
        print("Serialized successfully using JSON.")
        return json_data
    except (TypeError, OverflowError) as e:
        print(f"JSON Serialization Error: {e}")

    # pickle serialization
    try:
        with open('students.pkl', 'wb') as file:
            pickle.dump(obj, file)
        print("Serialized successfully using Pickle.")
        return None
    except (pickle.PicklingError, TypeError, Exception) as e:
        print(f"Pickle Serialization Error: {e}")

    #dill serialization
    try:
        with open('students_dill.pkl', 'wb') as file:
            dill.dump(obj, file)
        print("Serialized successfully using Dill.")
        return None
    except (dill.PicklingError, TypeError, Exception) as e:
        print(f"Dill Serialization Error: {e}")

  
    return "Serialization failed using all methods."


# Test serialization
result = serialize_object(students)
if result:
    print(result)
