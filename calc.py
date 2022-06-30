# Pede para o usuário entrar dois números inteiros e, em seguida,
# exibe um menu para o usuário escolher qual operação matématica quer realizar:
#     1. Soma
#     2. Subtração
#     3. Multiplicação
#     4. Finalizar programa
# Após a escolha no menu, a operação será executada
# e o programa pergunta se o usuário gostaria de fazer outra operação

def esValido(msgEntrada,msgErro="\n"):
    #testa se a entrada é um numero. Caso não seja, exibe a msgErro e pede uma nova entrada
    #entrada receberá um numero direto do usuario via input(msgEntrada)
    #msgErro é um parametro opcional
    entrada=input(msgEntrada)
    while (not entrada.isnumeric()):
        if msgErro!="\n": entrada=input('"'+entrada+'" '+msgErro+"\n"+msgEntrada)
        else: entrada=input(msgEntrada) #caso msgErro não seja passado como parametro
    else:
      return int(entrada)

def calcular(num_1,num_2,operaccion):
        if operaccion==1: #SOMA
          resultado=str(num_1+num_2)
          print("Resultado: "+str(num_1)+"+"+str(num_2)+"="+resultado)

        elif operaccion==2: #RESTA
          resultado=str(num_1-num_2)
          print("Resultado: "+str(num_1)+"-"+str(num_2)+"="+resultado)

        elif operaccion==3: #MULTIPLICACIÓN
          resultado=str(num_1*num_2)
          print("Resultado: "+str(num_1)+"*"+str(num_2)+"="+resultado)

        elif operaccion==4: #SALIR
          print("Hasta la vista, Baby!")

seguir="si"
while (seguir=="si"):
    num_1=esValido("Ingrese un numero: ","no es un numero.\n")

    num_2=esValido("ingrese mas un numero: ","no es un numero.\n")

    operaccion=esValido(
    "Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n",
    "no es una entrada valida. Intentalo otra ves.\n")

    if operaccion in [1,2,3,4]: calcular(num_1,num_2,operaccion)

    elif operaccion==0 or operaccion>4:
        while (operaccion==0 or operaccion>4):
          print('"'+str(operaccion)+'"'+" no es un numero valido. Intentalo otra ves.\n")
          operaccion=esValido("Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n","no es una entrada valida. Intentalo otra ves.")
        else: calcular(num_1,num_2,operaccion)

    if operaccion!=4: #caso o usuario não escolha a opçao 4 (Finalizar), perguntar se quer continuar o programa
        seguir=input('Te gustaria hacer otra operaccion? ("Si" o "No")\n').lower()
        while (seguir!="si" and seguir!="no"):
        #testa se é uma entrada válida ("si" ou "no")
            print("Entrada Invalida.")
            seguir=input('Te gustarias hacer otra operaccion? ("Si" o "No")\n').lower()
    else:
        #Usuario escolheu 4 no menu de operações, portanto o programa deve ser encerrado
        break
else: print("Fin!")
