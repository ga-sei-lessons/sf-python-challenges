# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
string = 'http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1'

# print(string[::-1])
print(dir(str))
empty = ''
for letter in string:
  empty = letter + empty

# print(empty)
text = ''.join(list(reversed(string)))
print(text)

# print(dir(text))


