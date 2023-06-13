

#Sorteo#
import random
comb_ganadora=[]
num_igual=0
suma=1
while(suma==1):
    comb_ganadora.clear()
    for x in range(6):
        num=random.randint(1,49)
        comb_ganadora.append(num)
    #Comprobacion de que no se repiten los numeros aleatorios
   
    suma=0
    #Repeticion del sorteo si se repiten #
    for x in range(1,5):
        if(comb_ganadora[x]==comb_ganadora[x-1] or comb_ganadora[x]==comb_ganadora[x-2]or
           comb_ganadora[x]==comb_ganadora[x-3]or comb_ganadora[x]==comb_ganadora[x-4]):
            
            suma=1
    
    



num_comp=random.randint(1, 49)
reintegro=random.randint(0, 9)
print(f"el resultado del sorteo es {comb_ganadora}")
print(f"el numero complementario es: {num_comp} y el reintegro es :{reintegro} ")
#Apuesta#
jugada=[]
suma=1
while(suma==1):
    jugada.clear()
    for x in range(6):
        num=random.randint(1,49)
        jugada.append(num)
    #Comprobacion de que no se repiten los numeros aleatorios
   
    suma=0
    #Repeticion del sorteo si se repiten #
    for x in range(1,5):
        if(jugada[x]==jugada[x-1] or jugada[x]==jugada[x-2]or
           jugada[x]==jugada[x-3]or jugada[x]==jugada[x-4]):
            
            suma=1
    
    

num_comp_jug=random.randint(1, 9)

print(f"la apuesta jugada es :{jugada} y el numero complementario jugado es {num_comp_jug} ")

#Comprobación#
aciertos=0
reinteg=""
num_comp_ju=""
for x in range(6):
    for i in range(6):
        if(comb_ganadora[x]== jugada[i]):
            aciertos=aciertos+1
        elif(reintegro==jugada[i]):
            reinteg="tienes el reintegro ganado"
        

if(num_comp==num_comp_jug):
    num_comp_ju="has acertado el numero complementario "

print(f"los aciertos que has conseguido en esta apuesta son :{aciertos}")
print(reinteg)
print(num_comp_ju)

l_aciertos=[]
l_aciertos.append(aciertos)
print(l_aciertos)