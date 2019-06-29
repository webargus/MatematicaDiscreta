
'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema I2:
    ------------

    Teste de primalidade - Método ingênuo
    Escreva um programa que recebe um inteiro n > 1 e que verifica, através de divisões
    sucessivas se este inteiro é um número primo.

    OBS: por falta de uma definição precisa do que seja o método ingênuo, implementamos duas
    funções, is_prime e is_prime_naif; ambas verificam a primalidade através de divisões
    sucessivas, sendo que a primeira (is_prime) descarta a verificação dos pares, testa a
    divisibilidade apenas por inteiros ímpares e executa a verificação somente até a raiz quadrada
    do inteiro cuja primalidade queremos verificar.
'''


# função auxiliar para verificar se um inteiro é primo
# algoritmo seletivo(ingênuo?): descarta o teste de divisibilidade quando o inteiro é par e
# verifica divisibilidade por inteiros ímpares somente até a raiz quadrada do número
def is_prime(nn):
    if nn == 2:     # retorna True pois 2 é primo
        return True
    if nn % 2 == 0:     # descarta os pares
        return False
    for div in range(3, int(nn**.5) + 1, 2):        # testa divisibilidade até raiz de n
        if nn % div == 0:
            return False
    return True


# função para verificar se um inteiro é primo
# algoritmo ingênuo (?): testa divisibilidade por todos os inteiros de 3 até n-1
def is_prime_naif(nn):
    if nn == 2:     # retorna True pois 2 é primo
        return True
    for div in range(3, nn):     # verifica divisibilidade desde 3 até n-1, inclusive pelos pares
        if nn % div == 0:
            return False
    return True


#   Loop para entrada e validação de n
while 1:
    try:
        n = int(input("Entre n: "))
        if n < 2:
            raise ValueError
        break
    except ValueError:
        print("Entrada inválida! Por favor, entre novamente um valor para n > 1.")

s = "%d "
if not is_prime_naif(n):
    s += "não "
s += "é primo."
print(s % n)





