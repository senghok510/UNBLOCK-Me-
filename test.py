


def quick_sort(a,p,r):
    pivot = partition(a,p,r)
    quick_sort(a,pivot)
    quick_sort(pivot+1,r)
    return a
def swab(i,j):
    i = aux
    aux = j
    j = aux
    


def partition(a,p,r):
    right = a[r]
    
    i =0
    for j in range(p,r):
        if a[j] < right:
            i += 1
            swab(a[i],a[j])
    swab(a[i+1],r)
    
def quick_sort(a):
    return quick_sort(a,0, a[len(a)-1])
                
    
    
    
    
    