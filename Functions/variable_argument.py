def avg(*number):
    if number:
        return sum(number)/len(number)

print( avg(12,13,34,23,44) )

print(avg())



def stats(*val, action='max'):
    '''
    function for doing stats,like min ,max,sum,avg,count etc
    '''
    if val:
        if action =='max':
            return max(val)
        elif action == 'min':
            return min(val)
        elif action == 'sum':
            return sum(val)
        elif action == 'avg':
            return avg(val)
        elif action == 'count':
            return len(val)
        elif action == 'all':
            return max(val), min(val), sum(val), avg(val), len(val)

print('calling stats')
print(stats(1,23,12))
print(stats(1,22,2,2,2,2 ))
print(stats(1,2,4,5,2,action='count'))
print(stats(1,2,3,action='min'))    