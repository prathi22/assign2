
#Heap sort
def heapsort(a):
    n=len(a)
    heapify(a,n)
    e=n-1
    while e>0:
        #swap(a[e],a[0])
        t=a[e]
        a[e]=a[0]
        a[0]=t
        e=e-1
        shiftd(a,0,e)
    return a

#create max heap
def heapify(a,n):
    s=(n-2)/2
    while s>=0:
        shiftd(a,s,n-1)
        s=s-1
    return a

#rearrange the tree to form max heap after deletion of max element from the tree
def shiftd(a,s,e):
    root=s
    while root*2+1<=e:
        child=root*2+1
        if child+1<=e and a[child]<a[child+1]:
            child=child+1
        if a[root]<a[child]:
            #swap(a[root],a[child])
            t=a[root]
            a[root]=a[child]
            a[child]=t
            root=child
        else:
            return
    return a


def input_num():
    a=[]
    print'Enter the array elements\npress -1 when you are done with the inputs'
    while(1):
        x=int(raw_input())
        if x==-1:
            break
        a.append(x)

    return a

arr=input_num()
sort_arr=heapsort(arr)
print 'Sorted array:\n'
print sort_arr
