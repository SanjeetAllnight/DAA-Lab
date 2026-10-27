def Place(k,i):
    for j in range(1,k):
        if x[j]==i or abs(x[j]-i)==abs(j-k):
            return False
    return True
def NQueens(k,n):
    global count
    for i in range(1,n+1):
        if Place(k,i):
            x[k]=i
            if k==n:
                count+=1
                print(f"\nSolution {count}: {x[1:n+1]}")
                for j in range(1,n+1):
                    print(" ".join("1" if x[j]==i else "0" for i in range(1,n+1)))
            else:
                NQueens(k+1,n)
def main():
    global x,count
    try:
        n=int(input("Enter number of queens: "))
        if n<=0:
            raise ValueError("Number of queens must be greater than 0.")
        x=[0]*(n+1)
        count=0
        NQueens(1,n)
        if count==0:
            print("No solutions exist.")
        else:
            print("\nTotal solutions =",count)
    except ValueError as e:
        print("Error:",e)
if __name__=="__main__":
    main()