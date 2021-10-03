msg = 'once upon a time there was a kingdom.'

# find-
# index

idx = msg.find('time')
print(f'`time` was found at index {idx}')

idx = msg.find('queen')
print(f'`queen` was found at index {idx}')

if idx == -1:
    print(f'`quuen` was not found')

idxking = msg.find('king')
print(f'`king` was found at index {idxking}')

idxA = msg.find('a')  
print(f'`a` was found at index {idxA}')
print(len(msg))

# find and index are same in functionality except index gives crash error


idxKing = msg.index('king')
print(f'`king` found at index {idxKing}')

idxQueen = msg.index('queen')
print(f'`queen` found at index {idxQueen}')