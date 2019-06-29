'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema F2:
    ------------

    Implemente o gerador de números pseudo-aleatórios Middle-Square:
    Dada a semente = X0 , tem-se Xn+1 = dois algarismos centrais de Xn**2.

'''

#   Loop para entrada e validação da quantidade (n) de números aleatórios a gerar e a semente (X0)
while 1:
    try:
        n, x0 = [int(x) for x in input("Entre a quantidade e a semente separadas por espaço: ").split()]
        if x0 < 10:
            raise ValueError
        break
    except ValueError:
        print("Entrada inválida! Por favor, entre só inteiros e no mínimo 2 algarismos para a semente.")


s = str(x0)
for i in range(n):
    print(s.zfill(2))       # imprime resultado preenchido com 0 à esquerda, se necessário
    x0 = x0**2              # eleva semente ao quadrado
    s = str(x0)             # converte nova semente em cadeia de caracteres numéricos
    if len(s) % 2 == 1:     # completa com zero à esquerda caso nova semente não tenha nº par de algarismos
        s.zfill(1)
    init = len(s)//2 - 1    # toma string de comprimento=2 a partir de um caracter à esquerda do meio
    s = s[init:init+2]
    x0 = int(s)             # transforma string em inteiro e repete o loop









