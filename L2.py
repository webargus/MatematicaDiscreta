'''
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    Problema L2:
    ------------

    Escreva um programa que recebe duas cadeias de bits x e y e retorna
    as cadeias x OR y, x XOR y e x AND y, onde essas operações são realizadas bit a bit.

'''


#   Loop para entrada e validação das cadeias de bits
while 1:
    try:
        c1, c2 = input("Entre as cadeias de bits x e y separadas por espaço: ").split()
        x, y = [int(x, 2) for x in (c1, c2)]
        break
    except ValueError:
        print("Entrada inválida! Por favor, entre novamente as cadeias somente com 1s e 0s.")


# salva o comprimento da maior cadeia em max_len
max_len = max(len(c1), len(c2))
# preenche cadeias com zeros à esquerda para que fiquem com o mesmo comprimento (açúcar)
c1 = c1.zfill(max_len)
c2 = c2.zfill(max_len)
# executa operações lógicas bit a bit e as imprime formatadas
print(c1 + " OR " + c2 + " = " + bin(x | y)[2:].zfill(max_len))
print(c1 + " XOR " + c2 + " = " + bin(x ^ y)[2:].zfill(max_len))
print(c1 + " AND " + c2 + " = " + bin(x & y)[2:].zfill(max_len))






