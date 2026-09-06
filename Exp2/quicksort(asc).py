def interchange(a,i,j):
    a[i],a[j]=a[j],a[i]
def partition(a,m,p):
    v=a[m]
    i=m
    j=p
    while True:
        while True:
            i+=1
            if a[i]>=v:
                break
        while True:
            j-=1
            if a[j]<=v:
                break
        if i<j:
            interchange(a,i,j)
        else:
            break
    a[m],a[j]=a[j],v
    return j
def quickSort(p,q):
    if p>=q:
        return
    if p<q:
        j=partition(arr,p,q+1)
        quickSort(p,j-1)
        quickSort(j+1,q)
def main():
    global arr
    try:
        n=int(input("Enter number of elements: "))
        if n<=0:
            raise ValueError("Number of elements must be greater than 0.")
        values=input("Enter elements: ").split()
        if len(values)!=n:
            raise ValueError("Number of elements entered does not match n.")
        arr=[0]+[int(x) for x in values]+[float("inf")]
        quickSort(1,n)
        print("Sorted array:",arr[1:n+1])
    except ValueError as e:
        print("Error:",e)
main()