def merge(*args):
    lst = list(args)
    initial = [0] * len(lst)
    out = []

    while lst:
        m = 0
        for i in range(len(lst)):
            if lst[i][initial[i]] < lst[m][initial[m]]:
                m = i
        out.append(lst[m][initial[m]])
        initial[m] += 1
        if initial[m] >= len(lst[m]):
            del lst[m]
            del initial[m]

    return out

a=[1,2,3]
b=[9,11,18]
c=[0,21]
d=[a,b,c]
print 'Initial array'
print d
out=merge(a,b,c)
print 'Sorted Array\n'
print out
