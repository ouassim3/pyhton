#!/usr/bin/python

def puissance(a,n):
 
  b=a
  e=n
  r=1
  c=0 
  S=0 
  if e % 2 == 1:
    s=1 
  else :
    s=0
  while e > 0:

   if e % 2 == 1:
      r=r*b
      s=s+1
   else:
    c=c+1
   b = b * b
   
   e = e // 2
   S=c+s
  return S
  print S
  print r

B=2
k=0
for i in range(200):
  m=puissance(B,i)
  k=k+m 
  print ("le nombre de multplication pour calculer a**n",m)
print k  
       
    
