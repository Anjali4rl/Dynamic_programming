
def knapsack(t,wt,vl,W,N):
    for n in range(N+1):
        for w in range(W+1):
            if n == 0 or w == 0:
                t[n][w] = 0
            elif wt[n - 1] <= W:
                t[n][w] = max((vl[n - 1] + t[n - 1][w - wt[n - 1]]), t[n - 1][w])
            else:
                t[n][w] = t[n - 1][w]

    return t[n][w]

print("****FRACTIONAL KNAPSACK****")
n=int(input("Enter no. of items : "))
w=int(input("Enter capacity of knapsack :"))
t=[[int(-1) for i in range(w+1)] for j in range(n+1)]

l=list(map(int,input("Enter their weights: ").split()))
p=list(map(int,input("Enter their values : ").split()))
profit=knapsack(t,l,p,w,n)
print("The maximum profit is :",profit)