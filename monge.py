
def monge_array(a,c):
    l1=len(a)
    l2=len(c)
    k=int(raw_input("Enter the value k:"))
    i=0
    j=0
    while i<l1 and j<l2:
        if a[i]+c[j]==k:
            print 'Pair=',a[i],c[j]
            return
        elif a[i]+c[j]<k and i<l1:
            i=i+1
        elif a[i]+c[j]>k and j<l2:
            j=j+1
    print 'Not found'

print 'Array1 in sorted order:\n'
a=[1,2,5,7,9]
print a
print 'Array2 in sorted order:\n'
b=[3,4,5,6,8]
print b
b.reverse()
c=b
monge_array(a,c)

