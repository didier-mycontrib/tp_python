tab =  [ 10, 5, 2, 8 , 4 ,7 , 3 , 6 , 9 ]

print("longueur=",len(tab))

for x in tab :
    print("x=",x , "x*x=", x*x)

for v in tab :
    if v%2==0:
        print ("valeur paire: ",v)    

for i in range(len(tab)-1,-1,-1):
    print("tab["+str(i)+"]=",tab[i])

premierImpair = None
for v in tab :
    if v % 2 !=0 :
        premierImpair=v
        break
print("premier impair=",premierImpair)