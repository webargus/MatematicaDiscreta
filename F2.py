'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema F2:
    ------------

    Implemente o gerador de números pseudo-aleatórios Middle-Square:
    Dada a semente = X0 , tem-se Xn+1 = dois algarismos centrais de Xn**2.

'''

#   Loop para entrada e validação da semente (X0)
while 1:
    try:
        x0 = int(input("Entre a semente ou 0 para sair: "))
        if x0 == 0:
            exit()
        s = str(x0)
        r = []
        while 1:
            x0 = x0 ** 2  # eleva semente ao quadrado
            s = str(x0)  # converte nova semente em cadeia de caracteres numéricos
            if len(s) % 2 == 1:  # completa com 1 zero à esquerda caso semente não tenha nº par de algarismos
                s.zfill(1)
            init = len(s) // 2 - 1  # toma string de comprimento=2 a partir de um caracter à esquerda do meio
            s = s[init:init + 2]
            if s in r:  # imprime lista e aborta loop se semente já ocorreu antes
                print(", ".join(r))
                break
            r.append(s)  # acumula resultado na lista de resultados
            x0 = int(s)  # transforma string em inteiro e repete o loop
    except ValueError:
        print("Entrada inválida! Por favor, entre só inteiros válidos para a semente.")










