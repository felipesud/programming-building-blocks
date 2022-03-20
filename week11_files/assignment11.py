# Assignment week 11 - Files
# From: https://byui-cse.github.io/cse110-course/lesson11/prove.html
# By: Felipe dos Santos Belisário

countries_list = []
acronyms_list = []
years_list = []
countries_data = []



with open('./life-expectancy.csv') as life_expectancy:
    for line in life_expectancy:
        line = line.strip()
        country, acronym, year, expectancy = line.split(",")
        countries_list.append(country)
        acronyms_list.append(acronym)
        years_list.append(year)
        countries_data.append(expectancy)
        print(expectancy)

  

highest = max(countries_data)
lowest = min(countries_data)
print(f"The min life expectancy was: {lowest}")
print(f"The max life expectancy was: {highest}")
