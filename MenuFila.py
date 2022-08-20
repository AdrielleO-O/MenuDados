from Fila2 import *


def menu():
    print("[1] Inserir um elemento na pilha")
    print("[2] Remover um elemento da pilha")
    print("[3] Encontrar a posição de um elemento dentro da pilha")
    print("[4] Buscar um determinado elemento da lista")
    print("[5] Apagar a pilha inteira")
    print("[0] Escolher outra estrutura de dado")

fila = Fila()
menu()
opcao = 0
opcao = int(input("Escolha uma das opções: "))
while opcao != 0:
    if opcao == 1:
        dado = int(input("Digite um valor: "))
        print(fila.inserir(dado))

    elif opcao == 2:
        dado = int(input("Escolha o elemento que deseja remover: "))
        print(fila.remover())

    elif opcao == 3:
        dado = int(input("Digite o valor que deseja encontrar: "))
        posicao = []
        print(fila.encontrar(dado, posicao))

    #elif opcao == 4:

    #elif opcao == 5:

    elif opcao == 0:
        print("Aguarde....")
    else:
        print("Opção inváalida! Tente novamente")

    menu()
    opcao = int(input("Escolha uma das opções: "))
print("Escolha outro\n")
