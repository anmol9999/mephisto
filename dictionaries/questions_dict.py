# wap to ask a user his/her expenses 
#on different items.Take around 15 keys and values from user.And then perform sum and average
# on the values.


items={}
print("******Expenses******")
for i in range(3):
    k=input("Enter the item : ")
    v=int(input("Enter the expense : "))
    items[k]=v

total=sum(list(items.values()))
avg=sum(list(items.values())/len(items))
print(f"total is {total},  average is {average}")

sum=0
for i in items:
    sum=sum+items[i]

print('\nItem and expenses are : ')
for k,v in items.items():
    print(k,"=>",v,end=', ')

print("\nSum of expenses is : ",sum)
print("\nAverage of expenses is : ",sum/len(items))