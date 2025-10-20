import time

class MinHeap:

    def __init__(self):
        """Inicializa el montículo como una lista vacía.

        No recibe parámetros y crea la estructura interna `nodos`.
        """
        self.nodos = []

    def esVacio(self):
        """Devuelve True si el montículo está vacío, False en caso contrario."""
        return len(self.nodos) == 0
    
    def cantidad(self):
        """Retorna el número de elementos contenidos en el montículo."""
        return len(self.nodos)

    def _indice_hijo_izq(self, indice_padre):
        """Calcula el índice del hijo izquierdo de un nodo padre dado."""
        return 2 * indice_padre + 1
    
    def _indice_hijo_der(self, indice_padre):
        """Calcula el índice del hijo derecho de un nodo padre dado."""
        return 2 * indice_padre + 2
    
    def _indice_padre(self, indice_hijo):
        """Calcula el índice del padre de un hijo dado."""
        return (indice_hijo - 1) // 2
    
    def _tiene_padre(self, indice):
        """Devuelve True si el nodo en `indice` tiene un padre válido."""
        return self._indice_padre(indice) >= 0
    
    def _tiene_hijo_der(self,indice_padre):
        """Indica si el nodo en `indice_padre` posee un hijo derecho dentro del arreglo."""
        return self._indice_hijo_der(indice_padre) < len(self.nodos)
    
    def _tiene_hijo_izq(self,indice_padre):
        """Indica si el nodo en `indice_padre` posee un hijo izquierdo dentro del arreglo."""
        return self._indice_hijo_izq(indice_padre) < len(self.nodos)
    
    def _intercambiar(self,indice_hijo, indice_padre):
        """Intercambia los elementos en los índices indicados.

        Lanza una excepción con contexto si ocurre un error durante el intercambio.
        """
        try:
            temporal = self.nodos[indice_padre]
            self.nodos[indice_padre] = self.nodos[indice_hijo]
            self.nodos[indice_hijo] = temporal
        except Exception as e:
            raise Exception(f"Error intercambiando índices '{indice_padre}', '{indice_hijo}'") from e
        
    def _indice_hijo_menor(self,indice_padre):
        """Devuelve el índice del hijo con menor valor o -1 si no tiene hijos."""
        if not self._tiene_hijo_izq(indice_padre):
            return -1
        
        indice_hijo_izq = self._indice_hijo_izq(indice_padre)

        if not self._tiene_hijo_der(indice_padre):
            return indice_hijo_izq
        
        indice_hijo_der = self._indice_hijo_der(indice_padre)

        if self.nodos[indice_hijo_izq] < self.nodos[indice_hijo_der]:
            return indice_hijo_izq
        
        return indice_hijo_der
    
    def _flotar(self, indice_hijo):
        """Mueve hacia arriba (flota) el nodo en `indice_hijo` hasta restaurar la propiedad de min-heap."""
        if not self._tiene_padre(indice_hijo):
            return 
        
        indice_padre = self._indice_padre(indice_hijo)

        if  self.nodos[indice_hijo] < self.nodos[indice_padre]:
            self._intercambiar(indice_hijo, indice_padre)
            self._flotar(indice_padre)

    def _hundir(self,indice_padre):
        """Mueve hacia abajo (hunde) el nodo en `indice_padre` hasta restaurar la propiedad de min-heap."""
        if indice_padre >= len(self.nodos):
            return
        
        indice_hijo_menor = self._indice_hijo_menor(indice_padre)

        if indice_hijo_menor == -1 or self.nodos[indice_padre] < self.nodos[indice_hijo_menor]:
            return
        
        self._intercambiar(indice_hijo_menor, indice_padre)
        self._hundir(indice_hijo_menor)
    
    def insertar(self,dato):
        """Inserta `dato` en el montículo y lo posiciona correctamente (flotar)."""
        posicion = len(self.nodos)
        self.nodos.append(dato)
        self._flotar(posicion)

    def eliminar_menor(self):
        """Elimina y devuelve el elemento mínimo (raíz) del montículo.

        Si el montículo está vacío, lanza una excepción.
        """
        if self.esVacio():
            raise Exception("EL montículo está vacío, no se puede eliminar")
        
        dato = self.nodos[0]
        indice_ultimo = len(self.nodos) -1

        self.nodos[0] = self.nodos[indice_ultimo]
        self.nodos.pop() #Elimina el elemento de la última posición

        if not self.esVacio():
            self._hundir(0)

        return dato
    
    def _encontrar(self,dato):
        """Busca la primera ocurrencia de `dato` y devuelve su índice, o -1 si no existe."""
        for indice in range(len(self.nodos)):
            if self.nodos[indice] == dato:
                return indice
        return -1

    def eliminar(self,dato):
        """Elimina la primera ocurrencia de `dato` en el montículo.

        Realiza intercambio con el último elemento y ajusta la estructura
        mediante flotar y hundir según corresponda.
        """
        indice = self._encontrar(dato)
        if indice == -1:
            raise Exception(f"No se encontró el dato a eliminar en el montículo")
        if indice == 0:
            self.eliminar_menor()
            return
        
        indice_ultimo = len(self.nodos) - 1

        self._intercambiar(indice, indice_ultimo)

        self.nodos.pop()

        if indice >= len(self.nodos):
            return 
        
        self._flotar(indice)
        self._hundir(indice)

    def imprime_arbol(self, indice=0, prefijo="", es_hijo_izq=True):
        """Imprime una representación en texto del árbol (orientado) desde `indice`.

        Utiliza recursión para dibujar hijos derecho e izquierdo con sangrías.
        """
        
        # 1. Comprobación de límites y nodos nulos
        if indice >= len(self.nodos):
            return

        # 2. Llamada recursiva para el hijo DERECHO (para que aparezca arriba)
        #    '└—' para el último hijo, '| ' para los hijos que tienen hermanos.
        if self._tiene_hijo_der(indice):
            # El hijo derecho siempre es el "primero" en imprimir en esta orientación
            self.imprime_arbol(self._indice_hijo_der(indice), prefijo + ("|   " if es_hijo_izq else "    "), False)

        # 4. Imprimir el nodo actual
        print(prefijo + ("└— " if es_hijo_izq else "┌— ") + str(self.nodos[indice]))

        # 5. Llamada recursiva para el hijo IZQUIERDO (para que aparezca abajo)
        #    '|   ' para indicar que hay más debajo, '    ' si es el último.
        if self._tiene_hijo_izq(indice):
            # El hijo izquierdo es el "último" en imprimir en esta orientación
            self.imprime_arbol(self._indice_hijo_izq(indice), prefijo + ("    " if es_hijo_izq else "|   "), True)

mh = MinHeap()

n = int(input("Ingrese la cantidad de números que quiere insertar al MinHeap:"))

for i in range(n):
    dato = int(input(f"Ingrese el elemento {i}: "))
    mh.insertar(dato)
    mh.imprime_arbol()
    input("Presione enter para continuar:")

m = int(input("Ingrese la cantidad de números que quiere eliminar del MinHeap:"))

for i in range(min(m,mh.cantidad())):
    dato = int(input(f"Ingrese el elemento {i+1} a eliminar: "))
    mh.eliminar(dato)
    mh.imprime_arbol()
    input("Presione enter para continuar:")

input("Presione enter para eliminar el resto de los elementos desde la raiz.")

for i in range(mh.cantidad()):
    dato = mh.eliminar_menor()
    print(f"Eliminado el dato {dato} que estaba en la raiz.")
    mh.imprime_arbol()
    input("Presione enter para continuar:")