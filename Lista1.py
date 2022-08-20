class Node:
    def __init__(self, dado):
        self.inicio = None
        self.dado = dado
        self.prox = None


class Lista:
    def __init__(self):
        self.inicio = None

    def ins_no_in(self, dado): #inserir no inicio
        novo_nodo = Node(dado)
        novo_nodo.prox = self.inicio
        self.inicio = novo_nodo
        return 'Elemento inserindo com sucesso'

    def ins_final(self, dado): #inserir no final
        novo_nodo = Node(dado)
        novo_nodo.prox = novo_nodo
        return 'Elemento inserindo com sucesso'

    def encontrar(self, posicao, dado):
        if posicao == 1:
            novo_nodo = Node(dado)
            novo_nodo.prox = self.inicio
            self.inicio = novo_nodo
        else:
            i = 1
            atual_nodo = self.inicio
            while i < posicao - 1 and atual_nodo is not None:
                atual_nodo = atual_nodo.prox
                i = i + 1
            if atual_nodo is None:
                print("Posiçao inválida.")
            else:
                novo_nodo = Node(dado)
                novo_nodo.prox = atual_nodo.prox
                atual_nodo.prox = novo_nodo
            return 'Elemento encontrado'

    def remover(self, dado):
        if self.inicio.dado == dado:
            self.inicio = self.inicio.prox
        else:
            anterior = None
            posterior = self.inicio
            while posterior and posterior.dado != dado:
                anterior = posterior
                posterior = posterior.prox
            if posterior:
                anterior.prox = posterior.prox
            else:
                anterior.prox = None
        return 'Elemento removido'

    def buscar(self, local):
        if local >= self.tamanho or local < 0:
            print("Posição ", local, " inválida.")
            return None
        atual_posicao = 0
        atual_nodo = self.inicio
        while atual_nodo != None:
            if atual_posicao == local:
                print("Posição ", local, " com o valor", atual_nodo.dado)
                return atual_nodo.dado
            atual_nodo = atual_nodo.prox
            atual_posicao += 1
        return 'Elemento buscado'
    
