print("Olá! Seja Bem-Vindo a Calculadora! Vamos fazer uma operação de complexos! ")
print("Vamos digitar o z1 ")
x1 = float(input('Digite a parte real : '))
y1 = float(input('Digite a parte imaginaria : '))
print("Vamos digitar o z2 ")
x2 = float(input('Digite a parte real : '))
y2 = float(input('Digite a parte imaginaria : '))

z1 = complex(x1,y1)
print("Você digitou : ", z1)
z2 = complex(x2,y2)
print("Você digitou : ", z2)
def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ Para adição
- Para subtração
* Para multplicação
/ Para divisão
c Para conjugar 
''')

    
    if operation == '+':
        
        print("z1+z2 = ",z1 + z2)

    elif operation == '-':
        
        print("z1-z2 = ",z1 - z2)

    elif operation == 'c':
        
        print("O conjugado dele é :  " , z1.conjugate())
    elif operation == '*':
        
        print("z1*z2 =", z1 * z2)

    elif operation == '/':
        
        print("z1/z2 = ",z1 / z2)

    else:
        print('Você digitou algo INVALIDO! Por favor tente novamente.')

    again()

def again():
    calc_again = input('''
Quer fazer outra operação?
Digite  S para Sim ou N for Não.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Obrigado por sua atenção.')
    else:
        again()

calculate()