
'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema I2:
    ------------

    Teste de primalidade - Método ingênuo
    Escreva um programa que recebe um inteiro n > 1 e que verifica, através de divisões
    sucessivas se este inteiro é um número primo.

    OBS: em dúvida quanto a que seja o método ingênuo, implementamos duas
    funções, is_prime_naif_1 e is_prime_naif_2; ambas verificam a primalidade através de divisões
    sucessivas, sendo que a primeira (is_prime_naif_1) descarta a verificação dos pares, testa a
    divisibilidade apenas por inteiros ímpares e executa a verificação somente até a raiz quadrada
    do inteiro cuja primalidade queremos verificar.
'''


# função auxiliar para verificar se um inteiro é primo
# algoritmo seletivo(ingênuo?): descarta o teste de divisibilidade quando o inteiro é par e
# verifica divisibilidade por inteiros ímpares somente até a raiz quadrada do número
def is_prime_naif_1(nn):
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
def is_prime_naif_2(nn):
    if nn == 2:     # retorna True pois 2 é primo
        return True
    for div in range(3, (nn-1)//2, 2):  # verifica divisibilidade pelos ímpares desde 3 até (n-1)/2
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
if not is_prime_naif_1(n):
    s += "não "
s += "é primo."
print(s % n)





