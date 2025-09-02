def cuadrado(base):
    print(id(base))
    base = base*base
    print(id(base))
    return base

i1 = 10
print(id(i1))
cuadrado(i1)

print(id(i1))
#Que pasará si imprimo i1?
print(i1)

def adicionar(lista, elemento):
    print(id(lista))
    l2 = lista
    print(id(l2))
    l2.append(elemento)
    print(id(l2))
    return l2

v1 = [1,2,3]
print(id(v1))

adicionar(v1,4)
print(id(v1))
#¿Que pasará si imprimo v1?
print(v1)