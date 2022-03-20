# Assignment week 11 - Files
# From: https://byui-cse.github.io/cse110-course/lesson11/prove.html
# By: Felipe dos Santos Belisário

from itertools import count




with open('./life-expectancy.csv') as life_expectancy:
    for line in life_expectancy:
        line = line.strip()
        country, acronym, year, countries_data = line.split(",")
      


    expectancy_value = countries_data[3]
    print(f"The max life expectancy was {max(expectancy_value)}")
    print(f"The min life expectancy was {min(expectancy_value)}")