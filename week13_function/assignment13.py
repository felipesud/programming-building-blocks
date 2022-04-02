#Assignment Week 13
#From: https://byui-cse.github.io/cse110-course/lesson13/prove.html
#By: Felipe dos Santos Belisário


# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def calculate_windchill(temperature, wind_speed):
    windchill= 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16 ) + (0.4275 * temperature) * (wind_speed ** 0.16 )
    return windchill

def celsius_to_fahrenheit(degree):
    return (degree * (9 / 5) + 32)

welcome = ''
goodbye = ''    
def welcome_screen(welcome):
    welcome = 'Welcome to the Wind Chill Calculations!'
    return welcome

def goodbye_screen(goodbye):
    goodbye = 'Thank you, Good Bye!'
    return goodbye

print(welcome_screen(welcome))    
user_temperature = float(input('\nWhat is the temperature? '))

degree_type = input('Fahrenheit or Celsius (F/C)? ').upper()
if degree_type == 'C':
    user_temperature = celsius_to_fahrenheit(user_temperature)
        

for wind_speed in range(5, 61, 5):
    windchill = calculate_windchill(user_temperature, wind_speed)
    print(f"At temperature {user_temperature}F, and wind speed {wind_speed} mph, the windchill is: {windchill:6.2f}F")
print()
print(goodbye_screen(goodbye))