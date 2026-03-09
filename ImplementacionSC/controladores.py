"""
Módulo con clases Controller - CODE SMELL
Clases con nombres problemáticos que SonarQube detectará
"""

from datetime import datetime, timedelta
from cafeteria import Producto, Orden, Empleado, CategoriaProducto, EstadoOrden, TipoPago
from cliente import Cliente, TipoCliente
import random
import json
import os

# Variables globales no utilizadas - CODE SMELL
GLOBAL_CONFIG = {}
CACHE_MANAGER = {}
TEMP_STORAGE = []
PROCESS_QUEUE = []
CONTROL_FLAGS = {}
_manager_instance = None
_controller_cache = []


class CafeteriaManager:
    """
    Clase Manager - CODE SMELL
    Clase que hace demasiadas cosas (God Class)
    Viola el principio de responsabilidad única
    """
    
    # Variables de clase no utilizadas - CODE SMELL
    _instance_count = 0
    _all_managers = []
    _global_state = {}
    MANAGER_VERSION = "1.0.0"
    
    def __init__(self, cafeteria):
        self.cafeteria = cafeteria
        self.cache_ordenes = {}
        self.cache_productos = {}
        self.cache_empleados = {}
        self.cache_clientes = {}
        
        # Variables no utilizadas - CODE SMELL
        self._temp_data = []
        self._processing_queue = []
        self._error_log = []
        self._success_log = []
        self._pending_operations = []
        self._completed_operations = []
        self._failed_operations = []
    
    def process_order_creation(self, cliente, items_list):
        """Procesa creación de orden - demasiada responsabilidad"""
        temp1 = 0
        temp2 = 0
        resultado_temp = None
        
        # Condiciones anidadas innecesarias - CODE SMELL
        if cliente is not None:
            if items_list is not None:
                if len(items_list) > 0:
                    if len(items_list) < 100:
                        orden = self.cafeteria.crear_orden(cliente)
                        
                        for item_data in items_list:
                            if item_data is not None:
                                if 'codigo' in item_data:
                                    if 'cantidad' in item_data:
                                        producto = self.cafeteria.inventario.obtener_producto(item_data['codigo'])
                                        if producto is not None:
                                            orden.agregar_item(producto, item_data['cantidad'])
                        
                        return orden
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    
    def manage_inventory_all(self):
        """Gestiona todo el inventario - demasiada complejidad"""
        resultados = []
        temp_var1 = 0
        temp_var2 = 0
        temp_var3 = 0
        
        # Revisa cada producto
        for codigo, producto in self.cafeteria.inventario.productos.items():
            if producto.stock < 5:
                if producto.stock < 3:
                    if producto.stock < 1:
                        if producto.stock == 0:
                            resultados.append(f"CRÍTICO: {producto.nombre}")
                        else:
                            resultados.append(f"URGENTE: {producto.nombre}")
                    else:
                        resultados.append(f"BAJO: {producto.nombre}")
                else:
                    resultados.append(f"ADVERTENCIA: {producto.nombre}")
        
        return resultados
    
    def control_employee_performance(self, empleado_id):
        """Controla rendimiento de empleados - CODE SMELL"""
        temp_resultado = {}
        temp_calificacion = 0
        temp_bono = 0
        
        for empleado in self.cafeteria.empleados:
            if empleado.id == empleado_id:
                if empleado.ordenes_atendidas > 100:
                    temp_calificacion = 10
                elif empleado.ordenes_atendidas > 80:
                    temp_calificacion = 9
                elif empleado.ordenes_atendidas > 60:
                    temp_calificacion = 8
                elif empleado.ordenes_atendidas > 40:
                    temp_calificacion = 7
                elif empleado.ordenes_atendidas > 20:
                    temp_calificacion = 6
                elif empleado.ordenes_atendidas > 10:
                    temp_calificacion = 5
                else:
                    temp_calificacion = 4
                
                return temp_calificacion
        
        return 0
    
    def handle_payment_processing(self, orden, tipo_pago, monto):
        """Maneja procesamiento de pago - complejidad innecesaria"""
        resultado = False
        mensaje = ""
        cambio = 0
        temp1 = 0
        temp2 = 0
        
        if orden is not None:
            if tipo_pago is not None:
                if tipo_pago == "efectivo":
                    if monto >= orden.total:
                        cambio = monto - orden.total
                        resultado = True
                        mensaje = "Pago exitoso"
                    else:
                        resultado = False
                        mensaje = "Monto insuficiente"
                elif tipo_pago == "tarjeta":
                    resultado = True
                    mensaje = "Pago con tarjeta exitoso"
                elif tipo_pago == "transferencia":
                    resultado = True
                    mensaje = "Transferencia exitosa"
                else:
                    resultado = False
                    mensaje = "Tipo de pago no válido"
            else:
                resultado = False
                mensaje = "Sin tipo de pago"
        else:
            resultado = False
            mensaje = "Orden no válida"
        
        return resultado, mensaje, cambio
    
    def manage_all_operations(self):
        """Gestiona todas las operaciones - God Method - CODE SMELL"""
        # Función que hace demasiadas cosas
        temp_var1 = 0
        temp_var2 = 0
        temp_var3 = 0
        temp_var4 = 0
        temp_var5 = 0
        
        # Gestión de inventario
        self.manage_inventory_all()
        
        # Gestión de empleados
        for empleado in self.cafeteria.empleados:
            self.control_employee_performance(empleado.id)
        
        # Gestión de órdenes
        for orden in self.cafeteria.ordenes:
            if orden.estado == EstadoOrden.PENDIENTE:
                pass
        
        # Gestión de productos
        for producto in self.cafeteria.inventario.productos.values():
            if producto.stock < 10:
                pass
        
        return True


class OrderProcessController:
    """
    Clase Controller - CODE SMELL
    Controlador que hace demasiado
    """
    
    # Variables no utilizadas - CODE SMELL
    _controller_id = 0
    _instances = []
    PROCESS_TIMEOUT = 3600
    MAX_RETRIES = 10
    
    def __init__(self):
        self.pending_processes = []
        self.completed_processes = []
        self.failed_processes = []
        
        # Variables no utilizadas - CODE SMELL
        self._temp_queue = []
        self._error_queue = []
        self._success_queue = []
        self._retry_queue = []
    
    def process_validate_order(self, orden):
        """Valida orden con mucha complejidad - CODE SMELL"""
        errores = []
        temp1 = 0
        temp2 = 0
        temp3 = 0
        
        if orden is not None:
            if orden.items is not None:
                if len(orden.items) > 0:
                    if len(orden.items) < 50:
                        for item in orden.items:
                            if item is not None:
                                if item.producto is not None:
                                    if item.producto.activo:
                                        if item.cantidad > 0:
                                            if item.cantidad < 100:
                                                pass
                                            else:
                                                errores.append("Cantidad muy alta")
                                        else:
                                            errores.append("Cantidad inválida")
                                    else:
                                        errores.append("Producto inactivo")
                                else:
                                    errores.append("Producto nulo")
                            else:
                                errores.append("Item nulo")
                    else:
                        errores.append("Demasiados items")
                else:
                    errores.append("Sin items")
            else:
                errores.append("Items nulos")
        else:
            errores.append("Orden nula")
        
        return len(errores) == 0, errores
    
    def control_order_state_machine(self, orden, accion):
        """Máquina de estados con switch - CODE SMELL"""
        estado_actual = orden.estado.value
        nuevo_estado = None
        temp_var = 0
        
        # Switch case simulado - CODE SMELL
        if estado_actual == "Pendiente":
            if accion == "pagar":
                nuevo_estado = EstadoOrden.PREPARANDO
            elif accion == "cancelar":
                nuevo_estado = EstadoOrden.CANCELADA
            else:
                nuevo_estado = orden.estado
        elif estado_actual == "Preparando":
            if accion == "completar":
                nuevo_estado = EstadoOrden.LISTA
            elif accion == "cancelar":
                nuevo_estado = EstadoOrden.CANCELADA
            else:
                nuevo_estado = orden.estado
        elif estado_actual == "Lista":
            if accion == "entregar":
                nuevo_estado = EstadoOrden.ENTREGADA
            elif accion == "cancelar":
                nuevo_estado = EstadoOrden.CANCELADA
            else:
                nuevo_estado = orden.estado
        elif estado_actual == "Entregada":
            nuevo_estado = orden.estado
        elif estado_actual == "Cancelada":
            nuevo_estado = orden.estado
        else:
            nuevo_estado = orden.estado
        
        orden.cambiar_estado(nuevo_estado)
        return nuevo_estado
    
    def process_bulk_orders(self, lista_ordenes):
        """Procesa múltiples órdenes - complejidad alta - CODE SMELL"""
        resultados = []
        temp_contador = 0
        temp_exitosos = 0
        temp_fallidos = 0
        
        if lista_ordenes is not None:
            if isinstance(lista_ordenes, list):
                if len(lista_ordenes) > 0:
                    for orden in lista_ordenes:
                        if orden is not None:
                            valido, errores = self.process_validate_order(orden)
                            if valido:
                                if orden.estado == EstadoOrden.PENDIENTE:
                                    self.control_order_state_machine(orden, "pagar")
                                    temp_exitosos += 1
                                else:
                                    temp_fallidos += 1
                            else:
                                temp_fallidos += 1
                        else:
                            temp_fallidos += 1
                else:
                    return []
            else:
                return []
        else:
            return []
        
        return resultados


class InventoryControlService:
    """
    Clase Service - CODE SMELL
    Servicio que gestiona demasiado
    """
    
    # Variables no utilizadas - CODE SMELL
    _service_instances = []
    SERVICE_VERSION = "2.0.0"
    MAX_INVENTORY_SIZE = 10000
    
    def __init__(self, inventario):
        self.inventario = inventario
        self.historial_cambios = []
        
        # Variables no utilizadas - CODE SMELL
        self._temp_changes = []
        self._pending_updates = []
        self._completed_updates = []
    
    def control_stock_levels(self):
        """Control de niveles de stock - CODE SMELL"""
        alertas = []
        temp1 = 0
        temp2 = 0
        temp3 = 0
        
        for codigo, producto in self.inventario.productos.items():
            if producto.categoria == CategoriaProducto.BEBIDA_CALIENTE:
                if producto.stock < 10:
                    alertas.append(f"BAJO: {producto.nombre}")
                elif producto.stock < 20:
                    alertas.append(f"MEDIO: {producto.nombre}")
            elif producto.categoria == CategoriaProducto.BEBIDA_FRIA:
                if producto.stock < 8:
                    alertas.append(f"BAJO: {producto.nombre}")
                elif producto.stock < 15:
                    alertas.append(f"MEDIO: {producto.nombre}")
            elif producto.categoria == CategoriaProducto.PANADERIA:
                if producto.stock < 15:
                    alertas.append(f"BAJO: {producto.nombre}")
                elif producto.stock < 25:
                    alertas.append(f"MEDIO: {producto.nombre}")
            elif producto.categoria == CategoriaProducto.COMIDA:
                if producto.stock < 5:
                    alertas.append(f"BAJO: {producto.nombre}")
                elif producto.stock < 10:
                    alertas.append(f"MEDIO: {producto.nombre}")
            elif producto.categoria == CategoriaProducto.POSTRE:
                if producto.stock < 10:
                    alertas.append(f"BAJO: {producto.nombre}")
            elif producto.categoria == CategoriaProducto.SNACK:
                if producto.stock < 20:
                    alertas.append(f"BAJO: {producto.nombre}")
        
        return alertas
    
    def manage_restock_process(self, codigo_producto, cantidad):
        """Gestiona proceso de reabastecimiento - CODE SMELL"""
        resultado = False
        mensaje = ""
        temp1 = 0
        temp2 = 0
        
        if codigo_producto is not None:
            if cantidad is not None:
                if cantidad > 0:
                    if cantidad < 1000:
                        producto = self.inventario.obtener_producto(codigo_producto)
                        if producto is not None:
                            if producto.activo:
                                producto.agregar_stock(cantidad)
                                resultado = True
                                mensaje = "Restock exitoso"
                            else:
                                resultado = False
                                mensaje = "Producto inactivo"
                        else:
                            resultado = False
                            mensaje = "Producto no encontrado"
                    else:
                        resultado = False
                        mensaje = "Cantidad muy alta"
                else:
                    resultado = False
                    mensaje = "Cantidad inválida"
            else:
                resultado = False
                mensaje = "Cantidad nula"
        else:
            resultado = False
            mensaje = "Código nulo"
        
        return resultado, mensaje
    
    def handle_inventory_audit(self):
        """Maneja auditoría de inventario - God Method - CODE SMELL"""
        resultado_auditoria = {
            'total_productos': 0,
            'total_stock': 0,
            'valor_total': 0,
            'bajo_stock': 0,
            'sin_stock': 0,
            'por_categoria': {}
        }
        
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        temp5 = 0
        
        # Procesa todos los productos
        for codigo, producto in self.inventario.productos.items():
            resultado_auditoria['total_productos'] += 1
            resultado_auditoria['total_stock'] += producto.stock
            resultado_auditoria['valor_total'] += producto.precio * producto.stock
            
            if producto.stock < 5:
                resultado_auditoria['bajo_stock'] += 1
            
            if producto.stock == 0:
                resultado_auditoria['sin_stock'] += 1
            
            categoria = producto.categoria.value
            if categoria not in resultado_auditoria['por_categoria']:
                resultado_auditoria['por_categoria'][categoria] = {
                    'cantidad': 0,
                    'stock': 0,
                    'valor': 0
                }
            
            resultado_auditoria['por_categoria'][categoria]['cantidad'] += 1
            resultado_auditoria['por_categoria'][categoria]['stock'] += producto.stock
            resultado_auditoria['por_categoria'][categoria]['valor'] += producto.precio * producto.stock
        
        return resultado_auditoria


class PaymentProcessHandler:
    """
    Clase Handler - CODE SMELL
    Manejador con demasiada responsabilidad
    """
    
    # Variables no utilizadas - CODE SMELL
    _handler_count = 0
    HANDLER_VERSION = "1.5.0"
    MAX_PAYMENT_AMOUNT = 100000
    
    def __init__(self):
        self.transaction_history = []
        self.pending_payments = []
        
        # Variables no utilizadas - CODE SMELL
        self._temp_transactions = []
        self._failed_transactions = []
        self._success_transactions = []
    
    def handle_cash_payment(self, orden, monto_recibido):
        """Maneja pago en efectivo - CODE SMELL"""
        resultado = False
        cambio = 0
        mensaje = ""
        temp1 = 0
        temp2 = 0
        
        if orden is not None:
            if monto_recibido is not None:
                if monto_recibido > 0:
                    if monto_recibido < 100000:
                        if monto_recibido >= orden.total:
                            cambio = monto_recibido - orden.total
                            resultado = True
                            mensaje = "Pago exitoso"
                        else:
                            resultado = False
                            mensaje = "Monto insuficiente"
                    else:
                        resultado = False
                        mensaje = "Monto muy alto"
                else:
                    resultado = False
                    mensaje = "Monto inválido"
            else:
                resultado = False
                mensaje = "Monto nulo"
        else:
            resultado = False
            mensaje = "Orden nula"
        
        return resultado, cambio, mensaje
    
    def process_payment_gateway(self, orden, tipo_pago):
        """Procesa pasarela de pago - switch case - CODE SMELL"""
        resultado = False
        codigo_transaccion = ""
        mensaje = ""
        temp_var = 0
        
        # Switch simulado - CODE SMELL
        if tipo_pago == "tarjeta_credito":
            resultado = True
            codigo_transaccion = f"TC-{random.randint(1000, 9999)}"
            mensaje = "Pago con tarjeta de crédito exitoso"
        elif tipo_pago == "tarjeta_debito":
            resultado = True
            codigo_transaccion = f"TD-{random.randint(1000, 9999)}"
            mensaje = "Pago con tarjeta de débito exitoso"
        elif tipo_pago == "paypal":
            resultado = True
            codigo_transaccion = f"PP-{random.randint(1000, 9999)}"
            mensaje = "Pago con PayPal exitoso"
        elif tipo_pago == "mercadopago":
            resultado = True
            codigo_transaccion = f"MP-{random.randint(1000, 9999)}"
            mensaje = "Pago con MercadoPago exitoso"
        elif tipo_pago == "stripe":
            resultado = True
            codigo_transaccion = f"ST-{random.randint(1000, 9999)}"
            mensaje = "Pago con Stripe exitoso"
        elif tipo_pago == "transferencia":
            resultado = True
            codigo_transaccion = f"TR-{random.randint(1000, 9999)}"
            mensaje = "Transferencia exitosa"
        elif tipo_pago == "bitcoin":
            resultado = True
            codigo_transaccion = f"BTC-{random.randint(1000, 9999)}"
            mensaje = "Pago con Bitcoin exitoso"
        else:
            resultado = False
            codigo_transaccion = ""
            mensaje = "Tipo de pago no soportado"
        
        return resultado, codigo_transaccion, mensaje
    
    def control_refund_process(self, orden, motivo):
        """Controla proceso de reembolso - CODE SMELL"""
        aprobado = False
        monto_reembolso = 0
        mensaje = ""
        temp1 = 0
        temp2 = 0
        temp3 = 0
        
        if orden is not None:
            if motivo is not None:
                if motivo == "cliente_insatisfecho":
                    aprobado = True
                    monto_reembolso = orden.total
                elif motivo == "producto_defectuoso":
                    aprobado = True
                    monto_reembolso = orden.total
                elif motivo == "entrega_tardia":
                    aprobado = True
                    monto_reembolso = orden.total * 0.5
                elif motivo == "error_orden":
                    aprobado = True
                    monto_reembolso = orden.total
                elif motivo == "cancelacion_cliente":
                    aprobado = True
                    monto_reembolso = orden.total * 0.8
                else:
                    aprobado = False
                    monto_reembolso = 0
            else:
                aprobado = False
        else:
            aprobado = False
        
        return aprobado, monto_reembolso, mensaje


class ReportGeneratorProcess:
    """
    Clase Process - CODE SMELL
    Generador de reportes con demasiada lógica
    """
    
    # Variables no utilizadas - CODE SMELL
    _process_id = 0
    REPORT_VERSION = "3.0.0"
    MAX_REPORTS = 1000
    
    def __init__(self, cafeteria):
        self.cafeteria = cafeteria
        self.reportes_generados = []
        
        # Variables no utilizadas - CODE SMELL
        self._temp_reports = []
        self._pending_reports = []
    
    def process_sales_report(self, fecha_inicio, fecha_fin):
        """Procesa reporte de ventas - demasiado complejo - CODE SMELL"""
        reporte = {}
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        
        ordenes_periodo = []
        total_ventas = 0
        
        for orden in self.cafeteria.ordenes:
            if orden.fecha_creacion >= fecha_inicio and orden.fecha_creacion <= fecha_fin:
                if orden.estado == EstadoOrden.ENTREGADA:
                    ordenes_periodo.append(orden)
                    total_ventas += orden.total
        
        reporte['total_ordenes'] = len(ordenes_periodo)
        reporte['total_ventas'] = total_ventas
        reporte['ticket_promedio'] = total_ventas / len(ordenes_periodo) if len(ordenes_periodo) > 0 else 0
        
        return reporte
    
    def manage_employee_report(self):
        """Gestiona reporte de empleados - CODE SMELL"""
        reporte_empleados = []
        temp1 = 0
        temp2 = 0
        
        for empleado in self.cafeteria.empleados:
            info_empleado = {
                'id': empleado.id,
                'nombre': empleado.nombre,
                'puesto': empleado.puesto,
                'ordenes': empleado.ordenes_atendidas,
                'horas': empleado.horas_trabajadas,
                'salario': empleado.calcular_salario(),
                'comision': empleado.calcular_comision()
            }
            reporte_empleados.append(info_empleado)
        
        return reporte_empleados


# Funciones sueltas controladoras - CODE SMELL
def global_manager_function(data):
    """Función global de gestión - CODE SMELL"""
    temp1 = 0
    temp2 = 0
    resultado = None
    
    if data is not None:
        if isinstance(data, dict):
            if 'key' in data:
                return data['key']
    
    return None


def global_process_controller(items):
    """Función global de procesamiento - CODE SMELL"""
    temp_result = []
    temp_counter = 0
    
    if items:
        for item in items:
            temp_result.append(item)
    
    return temp_result
