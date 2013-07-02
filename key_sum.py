def input_num():
    a=[]
    print'Enter the sorted array elements\npress -1 when you are done with the inputs'
    while(1):
        x=int(raw_input())
        if x==-1:
            break
        a.append(x)

    return a

a=input_num()
n=len(a)
print 'Enter the number k:'
k=int(raw_input())
s=0
e=n-1
while s<n-1:
    if a[s]+a[e]==k:
        print 'Pair '+str(a[s])+','+str(a[e])+'\n'
        break
    if a[s]+a[e]<k:
        s=s+1
    if a[s]+a[e]>k:
        e=e-1
