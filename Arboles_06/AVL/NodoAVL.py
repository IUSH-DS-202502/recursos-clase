class NodoAVL:
    def __init__(self,dato):
        self.dato = dato
        self.li:NodoAVL = None
        self.ld:NodoAVL = None
        self.altura = 1

    def retornaFB(self):
        altura_izq = self.li.altura if self.li else 0
        altura_der = self.ld.altura if self.ld else 0
        return altura_izq - altura_der
    
    @staticmethod
    def calculaNuevaAltura(nodo):
        altura_izq = nodo.li.altura if nodo.li else 0
        altura_der = nodo.ld.altura if nodo.ld else 0
        altura = 1 + max(altura_izq, altura_der)
        return altura