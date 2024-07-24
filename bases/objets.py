import math

########### code de la classe Cercle en python :

class Cercle():

    #constructeur avec valeurs par défaut:
    def __init__(self,xc=0,yc=0,rayon=0):
        self.xc=xc
        self.yc=yc
        self.rayon=rayon
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(cercle):
    def __str__(self):
        return "Cercle(xc="+str(self.xc) + ",yc="+str(self.yc) + ",rayon="+str(self.rayon) + ")"
		
    def perimetre(self):
        return 2*math.pi*self.rayon
		
    def aire(self):
        return math.pi*self.rayon*self.rayon

###### utilisation de la classe Cercle		
		
		
c1=Cercle(); #instanciation (pas de mot clef new) mais nom de classe
             #vue comme fonction créant une nouvelle instance
c1.rayon=40;
print("rayon de c1=",c1.rayon) # rayon de c1= 40
print("perimetre de c1=",c1.perimetre()) # perimetre de c1= 251.32741228718345
print("surface de c1=",c1.aire()) # surface de c1= 5026.548245743669

c2=Cercle(40,60,20) # Cercle(xc,yc,rayon)
print("rayon de c2=",c2.rayon) # rayon de c2= 20

print("c2=" , c2) # équivalent à print("c2=" , str(c2)) 
# affiche c2= Cercle(xc=40,yc=60,rayon=20)

print("type(c2)=",type(c2)) # <class '__main__.Cercle'>
#c2AsDict = c2.__dict__ # ok mais moins bien que vars(...)
c2AsDict = vars(c2) # converti un objet en un dictionnaire
print("c2AsDict=",c2AsDict) # {'xc': 40, 'yc': 60, 'rayon': 20}
print("type(c2AsDict)=",type(c2AsDict)) #  <class 'dict'>