from NodoAVL import NodoAVL

class ArbolAVL:
    def __init__(self):
        self.raiz : NodoAVL = None
    
    @staticmethod
    def rotacionDerecha(nodo_x:NodoAVL, nodo_y:NodoAVL):
        "Rota nodo_x alrededor de nodo_y"
        nodo_x.li = nodo_y.ld
        nodo_y.ld = nodo_x
        nodo_x.altura = NodoAVL.calculaNuevaAltura(nodo_x)
        nodo_y.altura = NodoAVL.calculaNuevaAltura(nodo_y)

    @staticmethod
    def rotacionIzquierda(nodo_x:NodoAVL, nodo_y:NodoAVL):
        "Rota nodo_x alrededor de nodo_y"
        nodo_x.ld = nodo_y.li
        nodo_y.li = nodo_x
        nodo_x.altura = NodoAVL.calculaNuevaAltura(nodo_x)
        nodo_y.altura = NodoAVL.calculaNuevaAltura(nodo_y)

    def _insertar(self, dato, nodo_p:NodoAVL):
        if not nodo_p:
            return NodoAVL(dato)
        
        if dato < nodo_p.dato:
            nodo_p.li = self._insertar(dato, nodo_p.li)
        elif dato > nodo_p.dato:
            nodo_p.ld = self._insertar(dato, nodo_p.ld)
        else:
            raise Exception("No se permiten datos repetidos en un AVL.")
        
        nodo_p.altura = NodoAVL.calculaNuevaAltura(nodo_p)
        balance_padre = nodo_p.retornaFB()

        #Casos de balanceo

        balance_izq = nodo_p.li.retornaFB() if nodo_p.li else 0
        balance_der = nodo_p.ld.retornaFB() if nodo_p.ld else 0

        #El nodo P es el que queremos balancear.

        #Izquierda-Izquierda
        if balance_padre >= 2 and balance_izq >= 0:
            nodo_q = nodo_p.li
            ArbolAVL.rotacionDerecha(nodo_p, nodo_q)
            return nodo_q
        
        #Derecha-Derecha
        if balance_padre <= -2 and balance_der <= 0:
            nodo_q = nodo_p.ld
            ArbolAVL.rotacionIzquierda(nodo_p, nodo_q)
            return nodo_q
        
        #Izquierda-Derecha
        if balance_padre >= 2 and balance_izq <= -1:
            nodo_q = nodo_p.li
            nodo_r = nodo_q.ld
            ArbolAVL.rotacionIzquierda(nodo_q, nodo_r)
            ArbolAVL.rotacionDerecha(nodo_p, nodo_r)
            return nodo_r
        
        #Derecha-Izquierda
        if balance_padre <= -2 and balance_der >= 1:
            nodo_q = nodo_p.ld
            nodo_r = nodo_q.li
            ArbolAVL.rotacionDerecha(nodo_q, nodo_r)
            ArbolAVL.rotacionIzquierda(nodo_p, nodo_r)
            return nodo_r

        return nodo_p
    
    def insertar(self, dato):
        "Inserta un nuevo dato buscando desde la raiz"
        self.raiz = self._insertar(dato,self.raiz)
    
    @staticmethod
    def inorden(padre:NodoAVL):
        if not padre:
            return
        ArbolAVL.inorden(padre.li)
        print(padre.dato, end=" ")
        ArbolAVL.inorden(padre.ld)

arbol = ArbolAVL()

arbol.insertar('F')
arbol.insertar('G')
arbol.insertar('B')
arbol.insertar('A')
arbol.insertar('D')
arbol.insertar('C')