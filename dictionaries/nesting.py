class_9 = {
    'teacher': 'pk shukla sir',
    'students':{
        '001':{
            'name':'raja babu',
            'father':'babu ji',
            'grade':'c'
        },
        '002':{
            'name':'raja',
            'father':'maharaj',
            'mother':'maharani',
            'grade':'b'
        },
        '007':{
        'name': 'james bond',    
        'father':'j',
        'mother':'m',
        'grade':'a'
        },
    
    }
}

print(class_9)

from pprint import pprint

# how to access

print(class_9['students']['002']['father'])

print(class_9['students']['007']['father'])

print(class_9['students']['001']['father'])

# loop

for k,val in class_9.items():
    print(k, end=' -> ')
    if isinstance(val,str):
        print(val)
    
    if isinstance(val,dict):
        for k,data in val.items():
            print(k,end=' -> ')
            if isinstance(data,str):
                print(data)
            if isinstance(data,dict):
                for k,v in data.items():
                    print(k,end=' -> ')
                    if isinstance(v,str):
                        print(v)


