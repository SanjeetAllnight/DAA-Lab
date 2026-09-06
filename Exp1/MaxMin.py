def maxmin(i,j,max,min):
    if i==j:
        mx=mn=arr[i]
    elif j==i+1:
        if arr[i]>arr[j]:
            mx,mn=arr[i],arr[j]
        else:
            mx,mn=arr[j],arr[i]
    else:
        mid=(i+j)//2
        max1,min1=maxmin(i,mid,max,min)
        max2,min2=maxmin(mid+1,j,max,min)
        if max1>max2:
            mx=max1
        else:
            mx=max2
        if min1<min2:
            mn=min1
        else:
            mn=min2
    print(i+1,"\t",j+1,"\t",mn,"\t",mx)
    return mx,mn
def main():
    try:
        n=int(input("Enter number of elements: "))
        if n<0:
            raise ValueError("Number of elements cannot be negative.")
        if n==0:
            print("Array is empty.")
            return
        data=input("Enter elements: ").split()
        if not data:
            raise ValueError("No elements were entered.")
        if len(data)!=n:
            raise ValueError(f"Expected {n} elements, but {len(data)} were entered.")
        global arr
        arr=list(map(int,data))
        print("\ni\tj\tMin\tMax")
        maximum,minimum=maxmin(0,n-1,None,None)
        print("\nFinal Minimum =",minimum)
        print("Final Maximum =",maximum)
    except ValueError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)
main()