"""Vai começar lendo sempre o parenteses interno"""
"""Saber quantos valores tem dentro da lista usando o print(lista.__len__())"""
lista = []
for i in range(0, 7):
    lista.append(int(input("Informe o valor: \n")))

# Procurando valores pares
i = 0
print("Valores pares:\n")
for valor in lista:
    if valor % 2 == 0:
        print(valor, " na posição ", i)
        print("\n")
        i += 1

# Procurando valores impares
i = 0
print("Valores impares:\n")
for valor in lista:
    if valor % 2 != 0:
        print(valor, " na posição ", i)
        print("\n")
        i += 1
