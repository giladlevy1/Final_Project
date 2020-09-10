sum=0
for grade in range(0,101):
    if grade>=60:
        sum=sum+grade
        average=sum/41

print(average)