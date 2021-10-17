# 1)
student = ['billu',17,15,12,14,False,True,9393939393]

stdDict = {
    'name':'billu',
    'maths':17,
    'english':15,
    'hindi':12,
    'age':14,
    'studies':False,
    'delinquent':True,
    'phone':9393939393
}

print(stdDict)

# 2)

myinfo = {
    'city':'lucknow',
    'state':'UP',
    'phone':'002',
    'phone':'007',              # repeating keys will overwrite contents
}

print(myinfo)

# 3) using constructor

address = dict(sno=121,street='abcd street',location='jdsjd',city='lucknow',pincode=226015)

print(address)


