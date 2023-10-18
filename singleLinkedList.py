#Single Linked List - Lista Enlazada Simple

class Single_Linked_List:
    class _Nodo:    #El guion bajo hace que la clase sea privada
        def __init__(self, valor):  #Constructor de la clase nodo (propiedad, parametro)
            self.valor = valor  #Representamos el nodo
            self.nodo_siguiente = None  #Apuntador hacia otros nodos
    def __init__(self):    #Constructor general de SLL
        self.cabeza = None  
        self.cola = None        #Propiedades
        self.tamaño = 0

#Metodo de impresion de la SLL

    def __str__(self):
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + " Tamaño: " + str(self.tamaño)

#Metodo Append para insertar elementos en la SLL
    def append(self, valor):
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

#Metodo Prepend
    def prepend(self, valor):
        #Agrega un elemento al principio de la SLL
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamaño += 1
#Eliminar primer elemento de la lista SHIFT
    def shift(self):
        #Saca el primer elemento de la linkedlist
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            return print(nodo_eliminado.valor)

sll = Single_Linked_List()


sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')
sll.prepend('Z')

sll.shift()
sll.shift()

print(sll)