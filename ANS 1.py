""" 
1. Use iter and next method to access all the elements of a given set using while loop

 """

l1=[67,"star",67.9,True,]
it=iter(l1)
t=len(l1)
while t>0:
       print(next(it),end=",")
       t-=1

#============================OUTPUT========================================
""" 
67,star,67.9,True
 """