class Api_BD:
    def __init__(self):
        self.api_datos = []
        
    def guardar_empleado(self, obj_nuevo_empleado):
        self.api_datos.append(obj_nuevo_empleado)
        
    def imprimir_api(self):
        for empleado in self.api_datos:
            print(empleado)
            
    def extender_api(self, lista_empleados):
        self.api_datos.extend(lista_empleados)
        
