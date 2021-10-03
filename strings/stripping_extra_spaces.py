name = '  anmol  '

cleaned_name = name.strip()
print(f"{len(name)}, {len(cleaned_name)}")

msg = '''
 i am here

'''

print(msg)
cleaned_msg = msg.strip()
print(cleaned_msg)
print(f"{len(msg)}, {len(cleaned_msg)}")

msg3 = 'we;come to wakanda, you wil have fun,just dont steal from us,or you will have no fun'

print('normal->', msg3.split(','))
print('normal 2 split->', msg3.split(',', maxsplit = 2))
print('reverse->', msg3.rsplit(','))
print('reverse 2 split->', msg3.rsplit(',', maxsplit = 2))


print(msg3[:18])


