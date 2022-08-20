from Lista1 import *

lista = Lista()
def menu():
    print("[1] Inserir um elemento no inicio da lista")
    print("[2] Inserir um elemento no final da lista")
    print("[3] Inserir um elemento em uma determinada posição da lista")
    print("[4] Encontrar a posição de um elemento dentro de uma lista")
    print("[5] Buscar um determinado elemento da lista")
    print("[6] Remover um elemento da lista")
    print("[7] Apagar a lista")
    print("[0] Escolher outra estrutura de dado")


menu()
opcao = 0
opcao = int(input("Escolha uma opcao: "))
while opcao != 0:
    if opcao == 1:
        dado = int(input("Digite um valor: "))
        print(lista.ins_no_in(dado))
    elif opcao == 2:
        dado = int(input("Dgite um valor para o final: "))
        print(lista.ins_final(dado))

    #elif opcao == 3:

    elif opcao == 4:
        dado = int(input("Digite o valor: "))
        posicao = []
        print(lista.encontrar(dado, posicao))

    #elif opcao == 5:
    elif opcao == 6:
        dado = int(input("Remover o elemento da lista: "))
        print(lista.remover())
    #elif opcao == 7:

    elif opcao == 0:
        print("Aguarde...")
    else:
        print("Opção inválida! Tente novamente")

    menu()
    opcao = int(input("Escolha uma opcao: "))
print("Escolha outro\n")
