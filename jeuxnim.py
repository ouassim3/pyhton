#!/usr/bin/python
  
def joueur1(liste):
   x=0
   if liste[3] > 0:
      x=liste[3]-4
      if x<=0:
       print("le joueur n1 sa perdu")
      else :
       print("le joueur n1 introduire le tas i et le nombre de pierre", 3,x)  

   liste[3]=x
   print(liste) 
   return liste
def joueur2(l):
    a=l[1]
    b=l[2]
    s=0
    c=0 
    while l[1]>0 & l[2]>0 :
      s=l[1]-1
      c=l[2]-1 
    l[1]=s
    l[2]=c
    print l
    
    return l
    
        
list=[3,5,7,8]
d=len(list)
print(list)
for i in range(10):
  liste1=joueur1(list)
  print("le joueur suivante")
  liste2=joueur2(liste1)
  
  for k in range(d):
    if liste1[k] > 0 :
       f=open('mscor.txt','w') 
    else :
       f=open('mscor.txt','w') 
  list=[6,7,9,12]
f=open('mscor.txt','w')
a=10
for i in range(4):
  a=i*a**i
print ("le scor finale ",a)  
f.write("la liste des meilleur joueur \n")

f.write("sidahmed son scor 1234 \n")
f.write("mohamed son scor  1123\n")
f.write("wassim son scor 1122\n")
f.write("jamel son scor 1111\n")
f.write("fysale son  scor 1110\n")
f.write("khaled son scor  1050\n")
f.write("iselem son scor  1000\n")
f.write("billel son scor 9786\n")
f.write("ahmed son scor 8907\n")
f.write("hamid son scor  7896\n")
f.close()
f=open('mscor.txt','r')
b=f.read()
print b

