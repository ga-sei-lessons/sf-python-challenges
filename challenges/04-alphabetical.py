# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

s = 'sadfkjhsadlkjhkdjfhlkjhewqkrjweryhhgdmngkiuposerdascxsamknvsdahfsadfsdaaaaa'

# convert to list
li = list(s) 
# sort the list
li.sort()
# convert ot new string
new_string = "".join(li)

print(new_string)
