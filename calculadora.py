def soma(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    return n1 / n2
def escolha():
    print ('Escolha a operação:')
    print ('1 - Soma')
    print ('2 - Subtração')
    print ('3 - Multiplicação')
    print ('4 - Divisão')
    op = int(input())
    while op < 1 or op > 4:
        print ('Opção inválida, digite novamente:')
        op = int(input())
    return op
def numero():
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    return n1, n2
def main():
    op = escolha()
    n1, n2 = numero()
    if (op == 1):
        res = soma(n1, n2)
        print ('{} + {} = {}'.format(n1, n2, res))
    elif (op == 2):
        res = subtracao(n1, n2)
        print ('{} - {} = {}'.format(n1, n2, res))
    elif (op == 3):
        res = multiplicacao(n1, n2)
        print ('{} x {} = {}'.format(n1, n2, res))
    elif (op == 4):
        res = divisao(n1, n2)
        print ('{} / {} = {}'.format(n1, n2, res))
main()

print ('Deseja fazer mais alguma operacao?')
print ('1 - Sim')
print ('2 - Não')
answer = int(input())

while answer == 1:
    main()
    print ('Deseja fazer mais alguma operacao?')
    print ('1 - Sim')
    print ('2 - Não')
    answer = int(input())
