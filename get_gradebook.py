# get_data.py
import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))
#print(dir(response))

print(response.status_code)
print(response.text)
print(type(response.text))

parsed_response = json.loads(response.text)
print(type(parsed_response))

gradebook = parsed_response["students"]
total_grade = 0
for stud in gradebook:
    total_grade += int(stud["finalGrade"])

max = 0
min = 100
for grades in gradebook:
    if int(grades["finalGrade"]) > max:
        max = float(grades["finalGrade"])
    if int(grades["finalGrade"]) < min:
        min = float(grades["finalGrade"])

print("The average grade was: " +str(total_grade/len(gradebook)))
print("The max grade was: " +str(max))
print("The min grade was: " +str(min))