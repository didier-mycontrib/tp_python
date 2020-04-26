# importation de toutes les fonctions du fichier my_fct.py
# pour pouvoir les appeler depuis ce fichier my_app.py
from my_fct import *

#from my_util.op3 import *
from my_util.op3 import tripleDe
from my_util.op4 import *

x=12;
print(doubleDe(x)) # affiche 24
print(moitieDe(x)) # affiche 6

print(tripleDe(x)) # affiche 36
print(quartDe(x)) # affiche 3.0

#importations nécessaires pour pouvoir utiliser pi , cos() , sin() 
#du module prédéfini math
from math import *

a=pi/2;
print('a=',a) # affiche 1.5707963267948966
x=cos(a)
print('x=',x) # affiche 6.123233995736766e-17 très proche de 0