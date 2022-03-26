# Assignment week 11 - Files
# From: https://byui-cse.github.io/cse110-course/lesson11/prove.html
# By: Felipe dos Santos Belisário
import statistics

life = []
years_list = []
country_list = []
country_chosen = []
life_chosen = []
is_selected = False
largest = 0

user_year = int(input('\nPlease type a year: '))

with open('./life-expectancy.csv') as life_expectancy_file:
    next(life_expectancy_file)
    for line in life_expectancy_file:
        line = line.strip()
        country, code, year, life_expectancy = line.split(",")
        
        
        life.append(life_expectancy)
        years_list.append(year)
        country_list.append(country)

        


        # if int(year) == user_year:
        #     is_selected = True
        #     user_country, user_code, user_year, user_life = line.split(",")
        #     country_chosen.append(user_country)
        #     life_chosen.append(user_life)
        #     max_life = life_chosen.index(max(life_chosen))
        #     min_life = life_chosen.index(min(life_chosen))
           
        #     # mean = statistics.mean(life_chosen)
          
            
            
            
            
highest = life.index(max(life))
lowest = life.index(min(life))



print(f"The overall max life expectancy is: {life[highest]} from {country_list[highest]} in {years_list[highest]}")
print(f"The overall min life expectancy is: {life[lowest]} from {country_list[lowest]} in {years_list[lowest]}")
    
# if is_selected:    
   
#     print(f'\n For the year {user_year}: ')
#     # print(f'The average life expectancy across all countries was {mean}')
#     print(f'The max life expectancy was in {country_chosen[max_life]} with {life_chosen[max_life]} ')
#     print(f'The min life expectancy was in {country_chosen[min_life]} with {life_chosen[min_life]} ')

with open("./life-expectancy.csv") as user_life_file:
    next(life_expectancy_file)
    
    for line in user_life_file:
        line = line.strip()
        user_country, user_code, user_year, user_life = line.split(",")
        
        if int(year) == int(user_year):
            print(f"Country: {user_country}, Code: {user_code}, Year: {user_year}, Life: {user_life}")
            
            if largest < float(user_life):
                largest = float(user_life)
                largest_country = user_country

if largest_country:
    print(f"\nThe max life expectancy was in {largest_country} with {largest}")