class Empleado_mod: 
    def __init__(self, nombre, apellido, cedula, celular):
        self.nombre_empleado= nombre
        self.apellido_empleado = apellido
        self.cedula_empleado = cedula
        self.celular_empleado = celular
    
    def set_nombre_empleado (self, nuevo_nombre ):
        self.nombre_empleado = nuevo_nombre 
        
    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_apellido_empleado (self, nuevo_apellido ):
        self.apellido_empleado = nuevo_apellido
        
    def get_apellido_empleado(self):
        return self.apellido_empleado
    
    def set_cedula_empleado (self, nueva_cedula ):
        self.cedula_empleado = nueva_cedula
        
    def get_cedula_empleado(self):
        return self.cedula_empleado
    
    def set_celular_empleado (self, nuevo_celular ):
        self.celular_empleado = nuevo_celular
        
    def get_celular_empleado(self):
        return self.celular_empleado
    
    def ver_info(self):
        info = "Nombre empleado: " + self.nombre_empleado + "Apellido empleado : " + self.apellido_empleado 
        info = info + "cedula empleado: " +  self.cedula_empleado + "celular empleado: " + self.celular_empleado
        return info
        
