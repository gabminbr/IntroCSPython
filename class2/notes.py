a = "me"
b = "myself"

c = a + b # memyself
d = a + " " + b # me myself
silly = a * 3 # mememe

# len() retrive the length of a string in parentheses
s = "abc"
chars = len(s) # chars = 3

# slicing a string
s = "abc"
#s[0] = 'a'
#s[1] = 'b'
#s[2] = 'c'

#s[-1] = 'c'
#s[-2] = 'b'
#s[-3] = 'a'

# substrings

    # [start:stop:step]
    # get chars at start up to stop - 1 taking every
    # step

s = "abcdefgh"
s[3:6] # 'def'
s[3:6:2] # 'df'
s[::-1] # 'hgfedcba'
s[6:1] # ''

# string are immutable, cannot be modified
# can only create new objects from the original
# so, when i made s = "a" and after s = "b", i'm not
# changing the value in memory of s, i'm just
# changing the reference box that s is doing
s = "car"

# input and output

#print(a, b, c) #will print separately the values
# print(a + b + c) # if all of them are string, will
#print them together, like "oneTwoThree"

#input
# x = input(s)
# input always return a string
# print the value s, user types and enter, the value
# is assigned to the variable x

# text = input("Type anything: ")
# print(5 * text)