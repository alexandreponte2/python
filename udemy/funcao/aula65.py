"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""






# def Print():
#     print("varias1")
#     print("varias2")
#     print("varias3")
#     print("varias4")


# def imprimir(a, b ,c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


# def saudacao(nome="sem nome"):
#     print(f"olá, {nome}")


# saudacao("Alexandre Ponte")
# saudacao("Maria")
# saudacao("Dany")
# saudacao()




def multiplo_de(numero, multiplo):
        resultado = numero % multiplo == 0
        print(f'{numero} é múltiplo de {multiplo}?', end=' ')
        print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)












# # def Print(a, b, c):
# #     print('Várias1')
# #     print('Várias2')
# #     print('Várias3')
# #     print('Várias4')

# # def imprimir(a, b, c):
# #     print(a, b, c)


# # imprimir(1, 2, 3)
# # imprimir(4, 5, 6)

# def saudacao(nome='Sem nome'):
#     print(f'Olá, {nome}!')


# saudacao('Luiz Otávio')
# saudacao('Maria')
# saudacao('Helena')
# saudacao()