import MenuLista
import MenuFila
import MenuPilha

class Menu:
    def menu(self):
        print("[1] Lista")
        print("[2] Fila")
        print("[3] Filha")
        print("[0] Sair do programa")


menu = Menu()
escolha = int(input("Escolha  o que deseja: "))

while escolha != 0:
    if escolha == 1:
        MenuLista.ListaMenu(menu)
    elif escolha == 2:
        MenuFila.FilaMenu(menu)
    elif escolha == 3:
        MenuPilha.PilhaMenu(menu)
    elif escolha == 4:
        print("Finalizando...")
    else:
        print("Opção inválida! Observe o menu e tente novamente")

    menu()
    escolha = int(input("Escolha o que deseja: "))
print("Fim do programa")
