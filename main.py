
def  soma ():
    num1  =  float ( input ( '1) Digite o número: ' ))
    num2  =  float ( input ( '2) Digite o número: ' ))
    print ( 'Resultado da soma: ' , num1  +  num2 )


def  sub ():
    num1  =  float ( input ( '1) Digite o número: ' ))
    num2  =  float ( input ( '2) Digite o número: ' ))
    print ( 'Resultado da subtração: ' , num1  -  num2 )


def  mult ():
    num1  =  float ( input ( '1) Digite o número: ' ))
    num2  =  float ( input ( '2) Digite o número: ' ))
    print ( 'Resultado da multiplicação: ' , num1  *  num2 )


def divi ():
    num1  =  float ( input ( '1) Digite um número: ' ))
    num2  =  float ( input ( '2) Digite um número: ' ))
    print ( 'Resultado da divisão: ' , num1  /  num2 )
def sair ():
   print ("Sair")

op = 1

while op:
    print('1 = Somar'), print('2 = Subtrair'), print('3 = Multiplicação'), print('4 = Divisão'), print('5 = Sair')

    op = int(input('Escolha uma opção: '))

    if op == 1:
        soma()
    elif op == 2:
        sub()
    elif op == 3:
        mult()
    elif op == 4:
        divi()
    elif op == 5:
        print('Programa finalizado com sucesso.')
        break
    else:
        print('Essa opção não existe')