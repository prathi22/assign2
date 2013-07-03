final=[]
min_arr=[]
sub_list=[[18,20],[1,2,3],[9,10,11,12]]
loc=0
def heapify(a,n):
    s=(n-2)/2
    while s>=0:
        shiftd(a,s,n-1)
        s=s-1
    return a

def shiftd(a,s,e):
    root=s
    while root*2+1<=e:
        child=root*2+1
        if child+1<=e and a[child]>a[child+1]:
            child=child+1
        if a[root]>a[child]:
            #swap(a[root],a[child])
            t=a[root]
            a[root]=a[child]
            a[child]=t
            root=child
        else:
            return
    return a

def combine(sub_list):
    global min_arr
    global final
    
    min_ele=[]
    k=len(sub_list)
    
    for i in range(k):
        for j in range(i+1):
            if len(sub_list[i])!=0:
                min_ele.append(sub_list[i][j])        
                break
            else:
                sub_list.remove(sub_list[i])
    #len_min_arr=len(min_ele)
    min_arr=heapify(min_ele,k)
    final.append(min_arr[0])
    #print 'min arr',min_arr
    #return sub_list

k=len(sub_list)
print 'List of sublists',sub_list

combine(sub_list)
print min_arr
for i in range(k):
    if min_arr[0]==sub_list[i][0]:
        loc=i
        sub_list[i].remove(min_arr[0])
        if len(sub_list[i])!=0:
            print sub_list
            combine(sub_list)

print 'Array:\n'
print final
#print sub_list
