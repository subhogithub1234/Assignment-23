""" 
3. Create a generator to produce first n even natural numbers

 """
def gen(n):
  a=2
  while n:
     yield a
     a+=2    
     n-=1
it=gen(10)
for i in it:
  print(i,end=" ") 

 #=====================================OUTPUT===================================
 # 2 4 6 8 10 12 14 16 18 20  