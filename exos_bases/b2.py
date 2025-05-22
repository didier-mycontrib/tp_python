sSuite="2;7;8;9;26;5"
values = sSuite.split(";")
for v in values :
    print(v)

values.insert(0,4)  #ajouter valeur 4 en position  0
values.append(30)
inverseValues=values.copy(); inverseValues.reverse();
print("values=",values)
print("values (ordre inverse)=",inverseValues)