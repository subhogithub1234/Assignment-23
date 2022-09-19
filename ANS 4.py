""" 
4. Create a generator to produce squares of first N natural numbers
 """
def fun(n):
    while n:
        yield n**2
        n-=1
a=fun(int(input(("Enter the value of N:"))))
for i in a:
    print(i)

#==============================OUTPUT=======================================
""" 
Enter the value of N:10
100
81
64
49
36
25
16
9
4
1
 """    