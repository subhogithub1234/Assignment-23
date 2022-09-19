""" 
6. Create a generator to produce first n prime numbers

 """
def fun(e):
    for i in e:
        for u in range(2,i):
            if i%u!=0:
               yield i

    
 

li=[e for e in range(1,int(input("Enter the value of N:"))+1)]
e=fun(li)
for i in e:
    print(i)

