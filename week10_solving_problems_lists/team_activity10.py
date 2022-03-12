#Team Activity Week 10 - Solving Problems Using Lists
#From: https://byui-cse.github.io/cse110-course/lesson10/teach.html
#By: Group 4 

from statistics import mean


bank_accounts = []
balances = []
account_name = None
account_value = 0

def show_values():
    print('\nAccount Information:')
    for i in range(len(bank_accounts)):
        print(f'{i}. {bank_accounts[i]} - ${balances[i]}')

while account_name != 'quit':
    account_name = input('What is the name of this account? ').lower()
    if account_name != 'quit':
        account_value = float(input('What is the balance? ') or 0)
        bank_accounts.append(account_name)
        balances.append(account_value)

show_values()

print(f'\nTotal: ${sum(balances)}')
print(f'Average: ${mean(balances):.2f}')

max_value = max(balances)
max_index = balances.index(max_value)
print(f'Highest balance: {bank_accounts[max_index]} - ${balances[max_index]}')

change = 'yes'
while change == 'yes':
    change = input('Do you want to update an account? ').lower()
    if change == 'yes':
        account_index = int(input('What account index do you want to update? '))
        new_amount = float(input('What is the new amount? '))
        balances[account_index] = new_amount
        show_values()
