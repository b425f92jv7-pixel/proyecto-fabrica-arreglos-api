from empleado_modelo import Empleado_mod 
from BD_modelo import Api_BD
from api_bd_maquinas import Api_BD_maquinas 
# codigo principal

obj_api = Api_BD()
obj_api_maquinas = Api_BD_maquinas()
obj_api_maquinas.imprimir_info()
print (obj_api_maquinas.buscar_info())
obj_empleado = Empleado_mod ("jesus ", "solano ", "1090412915 ", "3505455453 ") 
obj_empleado2 = Empleado_mod ("jonatan ", "rueda ", "1092414996 ", "3222455454 ")
obj_empleado3 = Empleado_mod ("andres ", "gomez ", "1091717527 ", "3505123455 ")
obj_api.guardar_empleado (obj_empleado)
obj_api.guardar_empleado (obj_empleado2)
obj_api.guardar_empleado (obj_empleado3)
obj_api.imprimir_api()


