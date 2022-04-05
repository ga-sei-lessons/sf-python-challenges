from calendar import prmonth


print("Welcome to Chase bank.")

# have a bank accout
account = 1000

prompt = '>'

still_banking = True

while still_banking:
  print('if you would like to see your balance: 1')
  print('if you would like to deposit: 2')
  print('if you would like to withdraw: 3')
  print('if you would like to stop banking: 4')

  method = input(prompt)

  if method == '1':
    print(account)
  elif method == '2':
    print('enter amount')
    amount = int(input(prompt))
    account += amount
    print(f'your balance current is: {account}')
  elif method == '3':
    print('enter amount')
    amount = int(input(prompt))
    account -= amount
    print(f'your balance current is: {account}')
  elif method == '4':
    still_banking = False
  else: 
    print('you push a wrong button, goodbye')

# function for display 

# function for deposit 

# function for withdraw

print("Have a nice day!")

