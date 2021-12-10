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

    def buscar_contacto(self,consulta):
        n=0
        
        for c in self.__contactos:
            if (consulta in c.get_nombre()):
                print("El nombre ",consulta," está en el nombre")
                n=n+1
            elif (consulta in c.get_telefono()):

                print("El nombre ",consulta," esta en la tel")
                n=n+1
            elif (consulta in c.get_email()):
                print("El nombre ",consulta," esta en el email")
                n=n+1

        if(n==0):
            print("El termino ",consulta," no está en la agenda")
    


    def editar_contacto(self):
        """Función editar contacto"""
        pass
    
    """def borrar_contacto(self):
        	option=int(input("Introduzca la opción deseada a borrar: "))
			if option==1:
                del(c1)
    


        for c in self.__contactos:

                pass"""

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
            n=0
            while(n<1):
                consulta=str(input("Escribe el termino que quiera buscar: "))
                n=2
            self.buscar_contacto(consulta)

        elif(opcion ==5 ):
            self.cerrar_agenda()
        """Listar Contact"""










        "Eliminar Contacto"
        
     