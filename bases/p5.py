from math import *
#NB: sqrt() calcule la racine carree (square root).

#resolution ax^2+bx+c=0
def resolEq2ndDegre(a,b,c):
	delta = b*b-4*a*c
	if delta==0 :
		x1=x2=-b/(2*a)
	if delta > 0:
		x1=(-b-sqrt(delta))/(2*a)
		x2=(-b+sqrt(delta))/(2*a)
	if delta <0:
		x1=(-b-1j*sqrt(-delta))/(2*a)
		x2=(-b+1j*sqrt(-delta))/(2*a)
	print("solutions pour equation ax^2+bx+c=0 avec a=",a, "b=",b , "c=" ,c );
	print("x1=",x1)
	print("x2=",x2)
		
resolEq2ndDegre(2,-9,-5); # x1=-0.5 et x2=5

resolEq2ndDegre(2,-1,-6); # x1=-1.5 et x2=2

resolEq2ndDegre(1,3,9/8); # x1=x2=4/4=0.75

resolEq2ndDegre(1,2,5); # x1=-1-2j et -1+2j avec j=i et j^2=i^2=-1

