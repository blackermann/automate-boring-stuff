#character count program
import pprint #pretty print module

message = 'It was a bright cold day in April, and the clocks were striking thirteen.' #can do this with any size message, like a book
count = {} #empty count dictionary

for character in message.upper():  #want to count all the letters upper and lower case
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count) #prints out a line, unordered

pprint.pprint(count) #pprint will list the key/values in an easy to read column in alphabetical order

#can also to this
rjtext = pprint.pformat(count) #returns a value that can be captured in a variable
print(rjtext)



