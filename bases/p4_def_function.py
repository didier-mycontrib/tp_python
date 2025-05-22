#p4.py : fonctions

#fonction basique sans paramètre retournant une valeur fixe:
def genererMessageSalutation():
	message="bonjour"
	return message
	
#fonction/procedure basique ne retournant aucune valeur
#mais exécutant une action:	
def saluer():
	salutation=genererMessageSalutation() #appel de sous-fonction
	print(salutation)	
	
saluer() #l'appel de la fonction déclenche l'affichage de bonjour

#fonction multiplier avec 2 parametres formels a et b
def multiplier(a,b):
	return a*b
	
x=4; y=5;
res = multiplier(x,y); # appel de la fonction multiplier en passant
                       # les valeurs des paramètres effectifs x et y
					   # lors de l'appel a est une copie de x
					   # et b est une copie de y

print("res=",res) # affiche res=20


########### lambda

def carre(x):
	return x*x

print("carre(4)=", carre(4)) #16

lambdaCarre = lambda x : x*x
print("type(lambdaCarre)=", type(lambdaCarre)) #<class 'function'>
print("lambdaCarre(4)=", lambdaCarre(4)) #16

lambdaMult = lambda x,y : x*y
print("lambdaMult(2,3)=", lambdaMult(2,3)) #6

import datetime;
lambdaReturnNow = lambda  maintenant=datetime.datetime.now() :maintenant.time()
print("heure=" , lambdaReturnNow()) # 18:16:54.789809

def enchainerCalculEtAffichageAvecPrefixage(x, fCalcul ,fPrefixage):
	res = fCalcul(x)
	print(fPrefixage(res))

enchainerCalculEtAffichageAvecPrefixage(6 , 
		lambda x:x*x ,lambda expr : '** ' + str(expr))	# ** 36	

enchainerCalculEtAffichageAvecPrefixage(6 , 
		lambda x:x+x ,lambda expr : '>> ' + str(expr)) # >> 12	


############## paramétres optionnels et nommés

def displayVal(val , color="blue" ,comment ="no comment"):
	message=str(val)+ " color="+color + " comment="+comment
	print(message)

displayVal(5,"red","with_all_params")
#5 color=red comment=with_all_params

displayVal(8,"green")#with default comment	
#8 color=green comment=no comment

displayVal(7) # with default color and comment
#7 color=blue comment=no comment

displayVal(comment="with_named_params",val=9)	#with named params
#9 color=blue comment=with_named_params


####### fonction à nombre d'arguments variables (*args, **kwargs)
# **kwargs for keyword args or **kvargs for keyValue args

def displayArgs(*args):
	for a in args:
		print("a=",a)

def displayKeyValueArgs(**kvargs):
	for k,v in kvargs.items():
		print("k=",k,"v=",v)

def displayArgsAndKeywordArgs(*args,**kwargs):
	for a in args:
		print("a=",a)
	for k,v in kwargs.items():
		print("k=",k,"v=",v)				


def sommeArgs(*args):
	s=0
	for a in args:
		s+=a
	return s

def sommeAnyArgs(*args,**kwargs):
	s=0
	for a in args:
		s+=a
	for v in kwargs.values():
		s+=v
	return s

displayArgs(2,6,8) # a=  , a= 6 , a= 8
print("sommeArgs=",sommeArgs(2,6,8)) # 16

displayKeyValueArgs(a=1,b=3,c=5)#k= a v= 1 , k= b v= 3 , k= c v= 5
displayArgsAndKeywordArgs(2,6,8,a=1,b=3,c=5) #ok
#displayArgsAndKeywordArgs(a=1,b=3,c=5,2,6,8) #error , positional args should be first

print("sommeAnyArgs=",sommeAnyArgs(2,6,8,a=1,b=3,c=5)) # 25