from Pilha3 import *


def menu():
    print("[1] Inserir um elemento na pilha")
    print("[2] Remover um elemento da pilha")
    print("[3] Encontrar a posição de um elemento dentro da pilha")
    print("[4] Buscar um determinado elemento da lista")
    print("[5]Apagar a pilha inteira")
    print("[0] Escolher outra estrutura de dado")

pilha = Pilha()
menu()
opcao = 0
opcao = int(input("Escolha uma das opções: "))
while opcao != 0:
    if opcao == 1:
        dado = int(input("Digite um valor: "))
        print(pilha.inserir(dado))
    elif opcao == 2:
        dado = int(input(("Digite o elemento que deseja remover: ")))
        print(pilha.remover())
    elif opcao == 3:
        dado = int(input("Digite o valor  na Pilha: "))
        posicao = []
        print(pilha.encontrar(dado, posicao))

    #elif opcao == 4:

    #elif opcao == 5:

    #elif opcao == 6:

    elif opcao == 0:
        print("Escolha")
    else:
        print("Opção inváalida! Tente novamente")

    menu()
    opcao = int(input("Escolha uma das opções: "))
print("Escolha outro\n")
