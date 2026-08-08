def maxmin(i,j,max,min):
    #base case:single element
    if i==j:
        mx=mn=arr[i]
    #base case:two elements
    elif j==i+1:
        if arr[i]>arr[j]:
            mx,mn=arr[i],arr[j]
        else:
            mx,mn=arr[j],arr[i]
    #recursive case
    else:
        mid=(i+j)//2
        max1,min1=maxmin(i,mid,max,min)
        max2,min2=maxmin(mid+1,j,max,min)
        mx=max(max1,max2)
        mn=min(min1,min2)
    print(i+1,"\t",j+1,"\t",mn,"\t",mx)
    return mx,mn
#main program
def main():
    try:
        #input
        n=int(input("Enter number of elements: "))
        #Exception Handling
        if n<0:
            raise ValueError("Number of elements cannot be negative.")
        if n==0:
            print("Array is empty.")
            return
        #input
        data=input("Enter elements: ").split()
        #Exception Handling
        if not data:
            raise ValueError("No elements were entered.")
        if len(data)!=n:
            raise ValueError(f"Expected {n} elements, but {len(data)} were entered.")
        #main code
        global arr
        arr=list(map(int,data))
        print("\ni\tj\tMin\tMax")
        maximum,minimum=maxmin(0,n-1,None,None)
        print("\nFinal Minimum =",minimum)
        print("Final Maximum =",maximum)
    #raise exception
    except ValueError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)
#execute main
if __name__=="__main__":
    main()