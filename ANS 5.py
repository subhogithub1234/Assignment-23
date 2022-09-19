""" 
5. Create a generator to produce first n terms of Fibonacci series

 """
def fibo(n):
    a,b=0,1
    while n:
        
        a,b=b,a+b
        yield a
        n-=1
t=fibo(int(input("Enter the value of N:"))-1)
print(0,end=" ")
for i in t:
    
    print(i,end=" ")

#===============================OUTPUT==========================================
""" 
Enter the value of N:10
0 1 1 2 3 5 8 13 21 34 
 """
