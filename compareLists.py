# Neste exercício, dadas duas strings o programa deverá comparar
# e imprimir na tela quais letras se repetem nas duas strings
# (letras que se repetem mais de uma vez nas duas strings, devem ser impressas uma única vez ao final da execução)

### O CÓDIGO ABAIXO É USANDO set()
set1=set("Hola Mundo!")
set2=set("Hola Luna!")

print(list(set1&set2))

### USANDO list()
list1=list("Hola mundo!")
list2=list("Hola Luna!")

result=[]
for i in range(0,len(list2)):
    if list2[i] in list1 and list2[i] not in result:
        result.append(list2[i])

print(result)
