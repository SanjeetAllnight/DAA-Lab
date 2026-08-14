def merge(low,mid,high):
    h=low
    i=low
    j=mid+1
    while h<=mid and j<=high:
        if arr[h]<=arr[j]:
            b[i]=arr[h]
            h+=1
        else:
            b[i]=arr[j]
            j+=1
        i+=1
    if h>mid:
        for k in range(j,high+1):
            b[i]=arr[k]
            i+=1
    else:
        for k in range(h,mid+1):
            b[i]=arr[k]
            i+=1
    for k in range(low,high+1):
        arr[k]=b[k]
def display():
    for i in range(n):
        if i in div:
            print("|",end=" ")
        print(arr[i],end=" ")
    print()
def mergeSort(low,high):
    if low<high:
        mid=(low+high)//2
        div.add(mid+1)
        display()
        mergeSort(low,mid)
        mergeSort(mid+1,high)
        merge(low,mid,high)
        div.remove(mid+1)
        display()
def main():
    global arr,b,n,div
    try:
        n=int(input("Enter number of elements: "))
        if n<=0:
            raise ValueError("Number of elements must be greater than 0.")
        values=input("Enter elements: ").split()
        if len(values)!=n:
            raise ValueError("Number of elements entered does not match n.")
        arr=[int(x) for x in values]
        b=[0]*n
        div=set()
        display()
        mergeSort(0,n-1)
    except ValueError as e:
        print("Error:",e)
main()