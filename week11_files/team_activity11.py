
  
# File: 11-Team_Activity.py
# Purpose: Team Activity Week 11 - Human Resources System
# Reference: https://byui-cse.github.io/cse110-course/lesson11/teach.html

with open("resources/hr_system.txt") as employees_list:
    for employee in employees_list:
        employee = employee.strip()
        name, id_number, job_title, salary = employee.split()
        
        #salary = (float(salary))
        salary = (float(salary)/24)
        
        if job_title.lower() == "engineer":
            salary += 1000
        
        #print(f"Name: {name}, Title: {job_title}")
        #print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")
        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")

