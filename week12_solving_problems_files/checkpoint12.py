# Checkpoint Week 12 Solving Problems Using Files
# From: https://byui-cse.github.io/cse110-course/lesson12/checkpoint.html
# By: Felipe dos Santos Belisario



people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


youngest_age = 9999


youngest_name = ""


for line in people:

    items = line.split() 

  
    name = items[0]
    age = int(items[1])

    
    if age < youngest_age:
      
        youngest_age = age

        
        youngest_name = name


print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")