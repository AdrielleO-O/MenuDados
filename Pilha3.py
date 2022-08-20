class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' %(self.dado, self.anterior)


class Pilha:
    def __init__(self):
        self.topo = None
        self.inicio = None

    def __repr__(self):
        return "["+str(self.topo)+"]"

    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        return 'Elemento inserindo com sucesso'

    def remover(self):
        assert self.topo
        self.topo = self.topo.anterior
        return 'Elemento removido'

    def encontrar(self, posicao, dado):
        if posicao == 1:
            novo_nodo = Nodo(dado)
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
                novo_nodo = Nodo(dado)
                novo_nodo.prox = atual_nodo.prox
                atual_nodo.prox = novo_nodo
            return 'Elemento encontrado'
        
