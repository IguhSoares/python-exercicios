# Dada uma determinada lista (oculta para o usuário), contendo números de 0 a 9,
# o programa pede pro usuário digitar um número entre 0 e 9
# e testa se o valor entrado é valido e, caso seja válido,
# verifica se o número digitado se encontra na lista
# caso o número não esteja na lista, pede pro usuário tentar novamente
# caso o número esteja na lista, o programa encerra exibindo a lista para o usuário.

lista=[1,3,4,6,7,9] # LISTA ARBITRÁRIA, PODERIAM SER QUAISQUER OUTROS VALORES

seguir=True
while(seguir):
    numero=input("Ingrese un numero de 0 a 9: ")
    while not numero.isnumeric() or int(numero)>9 or int(numero)<0:
        numero=input("Entrada invalida.\n\nIngrese un numero de 0 a 9: ")
    else:
        numero=int(numero)
        if numero in lista:
            print(f'Numero "{numero}" esta en la lista!\nLista: {lista}')
            seguir=False
        else: print(f'Numero "{numero}" no esta en la lista. Intenta otra vez.\n')
