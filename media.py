# Pede pro usuário entrar uma lista de números e, ao final, exibe a média aritmética desses números.

seguir=True

while (seguir):
    erro=False # RESETANDO A VARIÁVEL DE CONTROLE
    lista=input("Escreva uma lista de números separados apenas por espaço em branco (ex.: 1 2 3 4 5):\n").split()

    # TESTA SE OS ITENS DA LISTA SÃO APENAS NUMÉRICOS
    for i in range(0,len(lista)):
        if not lista[i].lstrip("-").isnumeric():
            print(f'ERRO: "{lista[i]}" não é uma entrada válida.\nSepare os números apenas com espaço em branco (ex.: 1 2 3 4 5).\n')
            if not erro: erro=True # VARIÁVEL DE CONTROLE erro SERÁ SETADA APENAS UMA VEZ, NA PRIMEIRA OCORRÊNCIA DE ENTRADA INVÁLIDA

    if not erro:
        soma=sum(map(int,lista)) # map() irá transformar cada item da lista em int e sum() irá somar todos os itens da lista resultante
        print(f"Soma={soma}\nMédia={soma/2}")
        seguir=False

### <VERSÃO DA MARJORIE>
### Pergunta quantos números o usuário vai digitar e, em seguida, lê um número por vez, exibindo a média no final
# cuantidad_numeros=int(input("Cuantos numeros desea introducir?\n"))
# lista=[]
#
# for count in range(cuantidad_numeros):
#     numero=int(input(f"Ingrese un numero ({count+1} de {cuantidad_numeros}): "))
#     lista.append(numero)
#     print(f"{lista}\n")
#
# soma=sum(lista)
# print(f"A soma dos números é: {soma}\nA media é: {soma/cuantidad_numeros}")
### <FIM DA VERSÃO DA MARJORIE>
