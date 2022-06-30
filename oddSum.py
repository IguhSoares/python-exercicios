# SOMA TODOS OS NUMEROS IMPARES DE 0 a 100
soma=1
for n in range(0,101,soma):
    if n%2==1: # n é um número ímpar
        resultado=soma+n
        print(f"{soma}+{n}={resultado}")
        soma=resultado
