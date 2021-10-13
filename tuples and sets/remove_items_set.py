words = {'alex','alan','josh'}
print(words)

if 'alan' in words:
    words.remove('alan')

print(words)


remvd_value = words.pop()
print(words)
print(remvd_value)


words.clear()
print(words)
