#Single Linked List - Lista Enlazada Simple

class Single_Linked_List:
    class _Nodo:    #El guion bajo hace que la clase sea privada
        def __init__(self, valor):  #Constructor de la clase nodo (propiedad, parametro)
            self.valor = valor  #Representamos el nodo
            self.nodo_siguiente = None  #Apuntador hacia otros nodos
        def __init_subclass__(self):    #Constructor general de SLL
            self.cabeza = None  
            self.cola = None        #Propiedades
            self.tamaño = 0
