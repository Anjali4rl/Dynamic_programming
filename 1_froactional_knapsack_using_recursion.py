def knapsack(wt,v,w,n):
    if n==0 or w==0:
        return 0
    if wt[n-1]<=w:
        return max((v[n-1]+knapsack(wt,v,w-wt[n-1],n-1)),knapsack(wt,v,w,n-1))
    elif wt[n - 1] > w:
        return knapsack(wt,v,w,n-1)

print("****FRACTIONAL KNAPSACK****")
n=int(input("Enter no. of items : "))
w=int(input("Enter capacity of knapsack :"))
l=list(map(int,input("Enter their weights: ").split()))
p=list(map(int,input("Enter their values : ").split()))
profit=knapsack(l,p,w,n)
print("The maximum profit is :",profit)