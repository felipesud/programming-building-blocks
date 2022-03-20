# Assignment week 11 - Files
# From: https://byui-cse.github.io/cse110-course/lesson11/prove.html
# By: Felipe dos Santos Belisário

with open('./life-expectancy.csv') as life_expectancy:
    for line in life_expectancy:
        countries_data = line.split(",")
        print(countries_data)