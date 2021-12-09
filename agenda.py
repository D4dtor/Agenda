class Agenda:
    """Clase Agenda que gestiona listado de Contacto"""
    def __init__(self):
        self.__contactos = []
        self.__abierta = False
    
    def agregar_contacto(self, contacto):
        """Agrega un Contacto a una lista"""
        self.__contactos.append(contacto)
    
    def listar_contacto(self):
       for c in self.__contactos:
           print(str(c))

    def buscar_contacto(self, x):
        for c in self.__contactos:
            if(c.get_nombre() == x):
                return c


    def editar_contacto(self):
        """Función editar contacto"""
        pass
    
    def borrar_contacto(self, x):
        "Funcion borrar contacto"
        for c in self.contactos:
            if(c.get_nombre()==x):
                delattr x
        
        
       

    def cerrar_agenda(self):
       self.__abierta = False

    def abrir_agenda(self):
        self.__abierta = True
        while( self.__abierta):
            self.__muestra_menu()
            self.__leer_opcion()
            
    
    def __muestra_menu(self):
        
        """Muestra las opciones disponibles"""
        print("------ SELECCIONA OPCIÓN ------")
        print("| 1.- Listar Contacto: ")
        print("| 2.- Buscar Contacto: ")
        print("| 3.- Editar Contacto: ")
        print("| 4.- Eliminar Contacto: ")
        print("| 5.- Cerrar Agenda: ")
        print("-----------------------")
    
    def __leer_opcion(self):
        """ Función auxiliar para leer datos del Usuario"""
        try:
            opcion = -1
            while((opcion > 4) or (opcion < 1)):
                opcion = int(input(">"))
        except:
            print("Error")     
        
            if(opcion == 1):
            self.listar_contacto()
        elif(opcion == 2 ):
            x=str(input("Escribe el nombre que quiera buscar"))
            self.buscar_contacto(x)

        elif(opcion ==5 ):
            self.cerrar_agenda()
        """Listar Contact"""










        "Eliminar Contacto"
        
     