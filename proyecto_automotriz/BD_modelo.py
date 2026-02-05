from BD_modelo import Api_bd
from empleado_modelo import Empleado_mod 
from api_bd_maquinas import Api_BD_maquinas 

# codigo principal
#codigo de bd empleado 
obj_api = Api_bd()
obj_api.imprimir_api()
obj_api.extender_varios_empleados (obj_api.lista_empleados)
obj_api.insertar_empleado (obj_api.empleado_5)  
obj_api.eliminar_empleado (0)
obj_api.remover_empleado (obj_api.empleado_4)
obj_api.ordenar_empleados()
obj_api.invertir_orden()


obj_empleado = Empleado_mod ("jesus ", "solano ", "1090412915 ", "3505455453 ") 
obj_empleado2 = Empleado_mod ("jonatan ", "rueda ", "1092414996 ", "3222455454 ")
obj_empleado3 = Empleado_mod ("andres ", "gomez ", "1091717527 ", "3505123455 ")

obj_api.guardar_empleado (obj_empleado)
obj_api.guardar_empleado (obj_empleado2)
obj_api.guardar_empleado (obj_empleado3)
obj_api.imprimir_api()


obj_api_maquinas = Api_BD_maquinas()
obj_api_maquinas.imprimir_info()
print (obj_api_maquinas.buscar_info())
