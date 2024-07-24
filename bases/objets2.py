import math

########### code de la classe AnimalDomestique en python :

class AnimalDomestique():

    #constructeur avec valeurs par défaut:
    def __init__(self,nom=""):
        self.nom=nom
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(animal):
    def __str__(self):
        return "AnimalDomestique(nom="+self.nom + ")"
		
    def decrire(self):
        print("AnimalDomestique de nom=",self.nom)
		
    def parler(self):
        print("animal_parlant")

#### classe Chat héritant de AnimalDomestique:

class Chat(AnimalDomestique):

    #constructeur avec valeurs par défaut:
    def __init__(self,nbHeuresSommeil=14,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #AnimalDomestique.__init__(self,*args, **kwargs)
        self.nbHeuresSommeil=nbHeuresSommeil
	
	#méthode spéciale __str__ (équivalent à .toString() de java)
	#qui sera automatiquement appelée lors d'un print(chat):
    def __str__(self):
        return "Chat(nom=" + self.nom + " nbHeuresSommeil=" + str(self.nbHeuresSommeil) +  ")"

    def decrire(self):
        print("Je suis un chat qui dort ",self.nbHeuresSommeil, " h")
        super().decrire()
        #AnimalDomestique.decrire(self)
		
    def parler(self):
        print("miaou miaou")
        
    def ronronner(self):
        print("ronron ...")        
        
###### utilisation de la classe AnimalDomestique 
###### et de ses sous classes		
		
		
a=AnimalDomestique() #instanciation (pas de mot clef new) mais nom de classe
                     #vue comme fonction créant une nouvelle instance
a.nom="animal_domestique_inconnu"
a.decrire()
a.parler()
print("a_as_dict:" , vars(a))

chat1 = Chat( 15 , "malo")
print(chat1)
chat1.decrire()
chat1.parler()
chat1.ronronner()
print("chat1_as_dict:" , vars(chat1))

print("isinstance(chat1,Chat):" ,  isinstance(chat1,Chat))
print("isinstance(a,Chat):" ,  isinstance(a,Chat))
print("issubclass(Chat,AnimalDomestique):" ,  issubclass(Chat,AnimalDomestique))