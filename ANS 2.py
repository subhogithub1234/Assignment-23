""" 
2. Create a generator to produce first n odd natural numbers
 """
def gen(n):
  a=1
  while n:
     if a%2!=0:
        yield a
     a+=1    
     n-=1
it=gen(20)
for i in it:
  print(i)

 #==================================OUTPUT=============================
""" 
1
3
5
7
9
11
13
15
17
19
  """ 
