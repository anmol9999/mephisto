# for temp_var in iterable:
#   statement 1
#   statement 2


# iterables can be of 
# -string
# -list
# -tuple , set,dict,special functions like range(),zip,enumerate()
# anything with multiple elements



num = [1,2,3,4,7,8,6,9]
for i in num:
    print(i)

msg = "we are now using loops"
print('characters in in msg:',len(msg))

#traversal
 
for char in msg:
    if char != ' ':
        print(char)

# muemric loop
for i in range(10):
     print(i, end=',')