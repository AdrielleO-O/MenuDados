class Nodo: #estrutura encadeada
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.inicio = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def inserir(self, novo_dado):
        novo_nodo = Nodo(novo_dado) #novo nodo é onde o dado será armazenado
        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
        return 'Elemento inserindo com sucesso'

    def remover(self):
        assert self.primeiro is not None
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        return 'Elemento removido com sucesso'

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
