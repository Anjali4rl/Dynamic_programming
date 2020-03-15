
def knapsack(t,wt,v,w,n):
    if n==0 or w==0:
        return 0
    if t[n][w]!=-1:
        return t[n][w]
    else:
        if wt[n-1]<=w:
            t[n][w]=max((v[n-1]+knapsack(t,wt,v,w-wt[n-1],n-1)),knapsack(t,wt,v,w,n-1))
            return t[n][w]
        elif wt[n - 1] > w:
            t[n][w]=knapsack(t,wt,v,w,n-1)
            return t[n][w]


print("****FRACTIONAL KNAPSACK****")
n=int(input("Enter no. of items : "))
w=int(input("Enter capacity of knapsack :"))
t=[[int(-1) for i in range(w+1)] for j in range(n+2)]

l=list(map(int,input("Enter their weights: ").split()))
p=list(map(int,input("Enter their values : ").split()))
profit=knapsack(t,l,p,w,n)
print("The maximum profit is :",profit)