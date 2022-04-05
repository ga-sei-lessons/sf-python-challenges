# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input('select a method: add, subtract, divide, multiply')
num1 = int(input('input a number'))
num2 = int(input('input another number'))

# if method == 'add':
#   print(num1 + num2)
# elif method == 'subtract':
#   print(num1 - num2)
# elif method == 'divide':
#   print(num1 / num2)
# elif method == 'multiply':
#   print(num1 * num2)
# else:
#   print('i dont think that is a math!')

math = {
  'add': num1 + num2,
  'subtract': num1 - num2,
  'multiply': num1 * num2,
  'divide': num1 / num2
}

if method not in math:
  print('i dont think that is a math!')
else:
  print(math[method])

# print(method, num1, num2)
