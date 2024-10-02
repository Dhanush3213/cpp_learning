Original_array=[0, -1, -2, -4, 5, 0, -6]
a=sorted(Original_array)
max=0
index=0
for i in range(len(a)-1):
    if a[i]*a[i+1] > max:
        max=a[i]*a[i+1]
        index=i
print(max)
print(a[index],a[index+1])
    
["abc9", "def3", "abc4def", "abcd"]