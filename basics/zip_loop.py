num = [12,13,14,15]
num2 = [13,67,78,98]
num3 = [88,90,73]

for i,j in zip(num,num2):
    print(i,j)

for i,j in zip(num,num2):
    print(i + j)

for i,j,k in zip(num,num2,num3):
    print(i,j,k)