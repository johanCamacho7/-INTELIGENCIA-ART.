class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar_rec(nodo.izq, valor)
        else:
            nodo.der = self._insertar_rec(nodo.der, valor)
        return nodo

    def inorden(self):
        self._inorden_rec(self.raiz)

    def _inorden_rec(self, nodo):
        if nodo is not None:
            self._inorden_rec(nodo.izq)
            print(nodo.valor, end=' ')
            self._inorden_rec(nodo.der)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
valores = [7, 3, 9, 1, 5, 8, 10]

for v in valores:
    arbol.insertar(v)

print("Recorrido inorden del árbol:")
arbol.inorden()
