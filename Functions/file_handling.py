'''
file handling basics:
1. read a file -open()
2. write a file -open()
3.update a file - open()
open() functions has option to set mode of file 
it returns a file object
'''


file = open('dummy.txt')
print(file.read())
file.close()

f1 = open('radiants.txt','w')
f1.write("the radiants are chutiya\n")
f1.write("radiants are gaaadu\n")
f1.write("to be continued\n")
f1.close()  # save 

f2 = open('dummy.txt','a')  # update or add a content
f2.write("\n written by gaandu")
f2.close()
