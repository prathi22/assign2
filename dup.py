#Remove all duplicates from an array

def input_num():
        a=[]
        print'Enter the array elements\npress -1 when you are done with the inputs'
        while(1):
            x=int(raw_input())
            if x==-1:
                break
            a.append(x)

        return a

def merge_sort(a):
    b=[]
    c=[]
    n=len(a)
    if n>1:
        for i in range(0,n/2):
            b.append(a[i])
        for i in range(n/2,n):
            c.append(a[i])
        merge_sort(b)
        merge_sort(c)
        merge(b,c,a)
        return a
    else:
        return a

def merge(b,c,a):
    i=0
    j=0
    k=0
    p=len(b)
    q=len(c)
    while i<p and j<q:
        if b[i]<=c[j]:
            a[k]=b[i]
            i=i+1
        else:
            a[k]=c[j]
            j=j+1
        k=k+1
    if i==p:
        while j<q:
            a[k]=c[j]
            j=j+1
            k=k+1
    else:
        while i<p:
            a[k]=b[i]
            i=i+1
            k=k+1
    return a

a=input_num()
n=len(a)
b=merge_sort(a)#Sort the array first
s=[]
s.append(b[0])
j=0
for i in range(1,n):
        if s[j]!=b[i]:
                s.append(b[i])
                j=j+1
print 'Array after removing duplicate elements:\n'
print s
        

