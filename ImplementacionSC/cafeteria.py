"""
Sistema de Gestión de Cafetería
Proyecto completo con múltiples módulos y funcionalidades
"""

from datetime import datetime, timedelta
from enum import Enum
import random
import sys
import os
import json
import time
import math

# Variables globales no utilizadas - CODE SMELL
VERSION_GLOBAL = "1.0.0"
CONFIG_PATH = "/config/settings.json"
MAX_INTENTOS_GLOBALES = 100
TEMPORARY_DATA = []
CACHE_DATOS = {}
CONTADOR_GLOBAL = 0
FLAG_DEBUG = True
FLAG_PRODUCCION = False
LISTA_TEMPORAL = []
DICCIONARIO_CACHE = {}
_variable_privada_sin_uso = "nunca_se_usa"
__variable_muy_privada = 12345


class CategoriaProducto(Enum):
    """Categorías de productos disponibles"""
    BEBIDA_CALIENTE = "Bebida Caliente"
    BEBIDA_FRIA = "Bebida Fría"
    PANADERIA = "Panadería"
    POSTRE = "Postre"
    COMIDA = "Comida"
    SNACK = "Snack"


class TipoPago(Enum):
    """Tipos de pago aceptados"""
    EFECTIVO = "Efectivo"
    TARJETA = "Tarjeta"
    TRANSFERENCIA = "Transferencia"
    DIGITAL = "Pago Digital"


class EstadoOrden(Enum):
    """Estados posibles de una orden"""
    PENDIENTE = "Pendiente"
    PREPARANDO = "Preparando"
    LISTA = "Lista"
    ENTREGADA = "Entregada"
    CANCELADA = "Cancelada"


class Producto:
    """Clase que representa un producto de la cafetería"""
    
    # Variables de clase no utilizadas - CODE SMELL
    _contador_productos = 0
    _lista_eliminados = []
    _historial_precios = {}
    VERSION_PRODUCTO = "2.1.0"
    
    def __init__(self, codigo, nombre, precio, categoria, stock=0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.activo = True
        
        # Variables de instancia no utilizadas - CODE SMELL
        self._timestamp_creacion = datetime.now()
        self._usuario_creador = "sistema"
        self._version_interna = 1
        self._metadata = {}
        self._flags = []
        self._temp_data = None
    
    def hay_stock(self, cantidad=1):
        """Verifica si hay stock suficiente"""
        return self.stock >= cantidad
    
    def descontar_stock(self, cantidad=1):
        """Descuenta stock del producto"""
        if self.hay_stock(cantidad):
            self.stock -= cantidad
            return True
        return False
    
    def agregar_stock(self, cantidad):
        """Agrega stock al producto"""
        self.stock += cantidad
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio"""
        # Variables locales no utilizadas - CODE SMELL
        temp_variable = 0
        contador_interno = 0
        resultado_temporal = None
        bandera_descuento = True
        valor_maximo = 1000
        valor_minimo = 0
        
        # Condiciones innecesarias anidadas - CODE SMELL
        if porcentaje > 0:
            if porcentaje < 100:
                if porcentaje >= 5:
                    if porcentaje <= 90:
                        if self.precio > 0:
                            if self.precio < 10000:
                                if self.activo == True:
                                    if self.stock >= 0:
                                        descuento = self.precio * (porcentaje / 100)
                                        return self.precio - descuento
                                    else:
                                        descuento = self.precio * (porcentaje / 100)
                                        return self.precio - descuento
                                else:
                                    descuento = self.precio * (porcentaje / 100)
                                    return self.precio - descuento
                            else:
                                descuento = self.precio * (porcentaje / 100)
                                return self.precio - descuento
                        else:
                            descuento = self.precio * (porcentaje / 100)
                            return self.precio - descuento
                    else:
                        descuento = self.precio * (porcentaje / 100)
                        return self.precio - descuento
                else:
                    descuento = self.precio * (porcentaje / 100)
                    return self.precio - descuento
            else:
                descuento = self.precio * (porcentaje / 100)
                return self.precio - descuento
        else:
            descuento = self.precio * (porcentaje / 100)
            return self.precio - descuento
    
    def validar_codigo_producto(self, codigo):
        """Función nunca utilizada - CODE SMELL"""
        temp1 = 0
        temp2 = 0
        temp3 = 0
        if codigo:
            if len(codigo) > 0:
                if len(codigo) < 100:
                    if codigo.startswith("BEB"):
                        return True
                    elif codigo.startswith("PAN"):
                        return True
                    elif codigo.startswith("COM"):
                        return True
                    elif codigo.startswith("POS"):
                        return True
                    elif codigo.startswith("SNK"):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def calcular_precio_especial(self, tipo_cliente):
        """Función con switch case simulado - CODE SMELL"""
        resultado = 0
        precio_base = self.precio
        descuento = 0
        impuesto = 0
        recargo = 0
        
        # Simular switch case con muchos elif - CODE SMELL
        if tipo_cliente == "normal":
            resultado = precio_base
        elif tipo_cliente == "vip":
            resultado = precio_base * 0.9
        elif tipo_cliente == "premium":
            resultado = precio_base * 0.85
        elif tipo_cliente == "estudiante":
            resultado = precio_base * 0.95
        elif tipo_cliente == "profesor":
            resultado = precio_base * 0.92
        elif tipo_cliente == "empleado":
            resultado = precio_base * 0.80
        elif tipo_cliente == "corporativo":
            resultado = precio_base * 0.88
        elif tipo_cliente == "mayorista":
            resultado = precio_base * 0.75
        elif tipo_cliente == "distribuidor":
            resultado = precio_base * 0.70
        elif tipo_cliente == "socio":
            resultado = precio_base * 0.65
        elif tipo_cliente == "fundador":
            resultado = precio_base * 0.50
        else:
            resultado = precio_base
        
        return resultado
    
    def __str__(self):
        estado = "✓" if self.activo else "✗"
        stock_info = f"Stock: {self.stock}" if self.stock > 0 else "Sin stock"
        return f"[{estado}] {self.nombre} - ${self.precio:.2f} ({self.categoria.value}) - {stock_info}"


class ItemOrden:
    """Representa un item dentro de una orden"""
    
    def __init__(self, producto, cantidad, descuento=0):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
        self.descuento = descuento
        self.subtotal = self.calcular_subtotal()
    
    def calcular_subtotal(self):
        """Calcula el subtotal del item"""
        subtotal = self.precio_unitario * self.cantidad
        if self.descuento > 0:
            subtotal -= subtotal * (self.descuento / 100)
        return subtotal
    
    def __str__(self):
        desc_info = f" (-{self.descuento}%)" if self.descuento > 0 else ""
        return f"{self.cantidad}x {self.producto.nombre} ${self.precio_unitario:.2f}{desc_info} = ${self.subtotal:.2f}"


class Empleado:
    """Clase que representa un empleado de la cafetería"""
    
    # Variables de clase no utilizadas - CODE SMELL
    _empleados_totales = 0
    _lista_despedidos = []
    _salario_minimo = 5.0
    _salario_maximo = 50.0
    TIPO_CONTRATO = "indefinido"
    
    def __init__(self, id_empleado, nombre, puesto, salario_hora):
        self.id = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario_hora = salario_hora
        self.ordenes_atendidas = 0
        self.horas_trabajadas = 0
        self.activo = True
        
        # Variables no utilizadas - CODE SMELL
        self._fecha_contratacion = datetime.now()
        self._evaluaciones = []
        self._bonos_acumulados = 0
        self._faltas = 0
        self._vacaciones_disponibles = 15
        self._departamento = "ventas"
        self._nivel = 1
    
    def registrar_orden(self):
        """Registra que el empleado atendió una orden"""
        self.ordenes_atendidas += 1
    
    def registrar_horas(self, horas):
        """Registra horas trabajadas"""
        self.horas_trabajadas += horas
    
    def calcular_salario(self):
        """Calcula el salario del empleado"""
        return self.horas_trabajadas * self.salario_hora
    
    def calcular_comision(self, porcentaje_comision=0.05):
        """Calcula comisión por ordenes atendidas"""
        # Variables no utilizadas - CODE SMELL
        comision_base = 10
        comision_extra = 5
        multiplicador = 1.5
        bono_mensual = 100
        
        # Condiciones innecesarias - CODE SMELL
        if self.ordenes_atendidas > 0:
            if self.ordenes_atendidas < 1000:
                if porcentaje_comision > 0:
                    if porcentaje_comision < 1:
                        if self.activo:
                            if self.horas_trabajadas > 0:
                                return self.ordenes_atendidas * porcentaje_comision
                            else:
                                return self.ordenes_atendidas * porcentaje_comision
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return self.ordenes_atendidas * porcentaje_comision
        else:
            return 0
    
    def calcular_bono_anual(self):
        """Función nunca usada con mucha complejidad - CODE SMELL"""
        bono = 0
        temp_var1 = 0
        temp_var2 = 0
        temp_var3 = 0
        
        if self.ordenes_atendidas > 100:
            if self.ordenes_atendidas < 200:
                bono = 100
            elif self.ordenes_atendidas < 300:
                bono = 200
            elif self.ordenes_atendidas < 400:
                bono = 300
            elif self.ordenes_atendidas < 500:
                bono = 400
            elif self.ordenes_atendidas < 600:
                bono = 500
            elif self.ordenes_atendidas < 700:
                bono = 600
            elif self.ordenes_atendidas < 800:
                bono = 700
            elif self.ordenes_atendidas < 900:
                bono = 800
            elif self.ordenes_atendidas < 1000:
                bono = 900
            else:
                bono = 1000
        else:
            bono = 50
        
        return bono
    
    def validar_permisos_empleado(self, accion):
        """Función nunca usada - CODE SMELL"""
        if self.puesto == "Barista Senior":
            if accion == "crear_orden":
                return True
            elif accion == "modificar_orden":
                return True
            elif accion == "cancelar_orden":
                return True
            elif accion == "aplicar_descuento":
                return True
            elif accion == "modificar_precio":
                return False
            elif accion == "ver_reportes":
                return True
            else:
                return False
        elif self.puesto == "Cajera":
            if accion == "crear_orden":
                return True
            elif accion == "cobrar":
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self):
        return f"{self.nombre} - {self.puesto} (Ordenes: {self.ordenes_atendidas})"


class Orden:
    """Clase que representa una orden de cliente"""
    
    contador_ordenes = 1000
    
    # Variables de clase no utilizadas - CODE SMELL
    _ordenes_canceladas = []
    _ordenes_pendientes_historico = []
    _total_ordenes_dia = 0
    _promedio_ordenes = 0
    ESTADO_DEFAULT = "pendiente"
    PRIORIDAD_NORMAL = 1
    
    def __init__(self, cliente, empleado=None):
        Orden.contador_ordenes += 1
        self.numero_orden = Orden.contador_ordenes
        self.cliente = cliente
        self.empleado = empleado
        self.items = []
        self.subtotal = 0.0
        self.impuesto = 0.0
        self.total = 0.0
        self.estado = EstadoOrden.PENDIENTE
        self.fecha_creacion = datetime.now()
        self.fecha_entrega = None
        self.tipo_pago = None
        self.propina = 0.0
        
        # Variables no utilizadas - CODE SMELL
        self._prioridad = 1
        self._notas_especiales = ""
        self._tiempo_estimado = 0
        self._mesa_numero = None
        self._delivery = False
        self._direccion_entrega = None
        self._telefono_contacto = None
        self._codigo_confirmacion = None
    
    def agregar_item(self, producto, cantidad=1, descuento=0):
        """Agrega un item a la orden"""
        # Variables no utilizadas - CODE SMELL
        resultado_validacion = True
        mensaje_error = ""
        contador_items = 0
        limite_items = 100
        precio_total_temp = 0
        
        # Condiciones innecesariamente anidadas - CODE SMELL
        if producto is not None:
            if producto.activo is not None:
                if not producto.activo:
                    print(f"⚠️ El producto {producto.nombre} no está disponible")
                    return False
                else:
                    if cantidad > 0:
                        if cantidad < 1000:
                            if producto.stock is not None:
                                if not producto.hay_stock(cantidad):
                                    print(f"⚠️ Stock insuficiente para {producto.nombre}")
                                    return False
                                else:
                                    item = ItemOrden(producto, cantidad, descuento)
                                    self.items.append(item)
                                    producto.descontar_stock(cantidad)
                                    self.calcular_total()
                                    return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    
    def eliminar_item(self, index):
        """Elimina un item de la orden"""
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            item.producto.agregar_stock(item.cantidad)
            self.calcular_total()
            return True
        return False
    
    def calcular_total(self, tasa_impuesto=0.16):
        """Calcula el total de la orden con impuestos"""
        # Variables no utilizadas - CODE SMELL
        temp_subtotal = 0
        temp_impuesto = 0
        temp_descuento = 0
        temp_recargo = 0
        factor_conversion = 1.0
        
        self.subtotal = sum(item.subtotal for item in self.items)
        self.impuesto = self.subtotal * tasa_impuesto
        self.total = self.subtotal + self.impuesto + self.propina
        return self.total
    
    def validar_orden_completa(self):
        """Función nunca usada con switch case - CODE SMELL"""
        errores = []
        advertencias = []
        info = []
        
        # Switch case simulado - CODE SMELL
        estado_actual = self.estado.value
        
        if estado_actual == "Pendiente":
            if len(self.items) == 0:
                errores.append("No hay items")
            elif len(self.items) > 50:
                advertencias.append("Muchos items")
            else:
                info.append("Orden válida")
        elif estado_actual == "Preparando":
            if self.empleado is None:
                errores.append("Sin empleado")
            else:
                info.append("En proceso")
        elif estado_actual == "Lista":
            if self.total == 0:
                errores.append("Total en cero")
            else:
                info.append("Lista para entregar")
        elif estado_actual == "Entregada":
            if self.fecha_entrega is None:
                errores.append("Sin fecha entrega")
            else:
                info.append("Completada")
        elif estado_actual == "Cancelada":
            info.append("Orden cancelada")
        else:
            errores.append("Estado desconocido")
        
        return len(errores) == 0
    
    def calcular_descuento_especial(self, tipo_descuento):
        """Función duplicada innecesaria - CODE SMELL"""
        descuento = 0
        temp1 = 0
        temp2 = 0
        temp3 = 0
        
        if tipo_descuento == "cumpleanos":
            descuento = 0.15
        elif tipo_descuento == "estudiante":
            descuento = 0.10
        elif tipo_descuento == "empleado":
            descuento = 0.20
        elif tipo_descuento == "corporativo":
            descuento = 0.12
        elif tipo_descuento == "mayorista":
            descuento = 0.25
        elif tipo_descuento == "black_friday":
            descuento = 0.40
        elif tipo_descuento == "cyber_monday":
            descuento = 0.35
        elif tipo_descuento == "navidad":
            descuento = 0.30
        elif tipo_descuento == "ano_nuevo":
            descuento = 0.28
        else:
            descuento = 0
        
        return self.subtotal * descuento
    
    def aplicar_descuento_total(self, porcentaje):
        """Aplica un descuento a toda la orden"""
        for item in self.items:
            item.descuento = porcentaje
            item.subtotal = item.calcular_subtotal()
        self.calcular_total()
    
    def agregar_propina(self, monto):
        """Agrega propina a la orden"""
        self.propina = monto
        self.calcular_total()
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la orden"""
        self.estado = nuevo_estado
        if nuevo_estado == EstadoOrden.ENTREGADA:
            self.fecha_entrega = datetime.now()
            if self.empleado:
                self.empleado.registrar_orden()
    
    def procesar_pago(self, tipo_pago, monto_recibido=None):
        """Procesa el pago de la orden"""
        self.tipo_pago = tipo_pago
        
        if tipo_pago == TipoPago.EFECTIVO and monto_recibido:
            cambio = monto_recibido - self.total
            if cambio >= 0:
                self.cambiar_estado(EstadoOrden.PREPARANDO)
                return True, cambio
            else:
                print("⚠️ Monto insuficiente")
                return False, 0
        else:
            self.cambiar_estado(EstadoOrden.PREPARANDO)
            return True, 0
    
    def tiempo_preparacion(self):
        """Calcula el tiempo de preparación estimado"""
        if self.fecha_entrega:
            return (self.fecha_entrega - self.fecha_creacion).seconds / 60
        return 0
    
    def mostrar_orden(self):
        """Muestra los detalles de la orden"""
        print(f"\n{'='*60}")
        print(f"  ORDEN #{self.numero_orden} - {self.estado.value}")
        print(f"{'='*60}")
        print(f"Cliente: {self.cliente}")
        if self.empleado:
            print(f"Atendido por: {self.empleado.nombre}")
        print(f"Fecha: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M')}")
        print(f"\n{'-'*60}")
        
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        
        print(f"{'-'*60}")
        print(f"Subtotal:        ${self.subtotal:>10.2f}")
        print(f"Impuesto (16%):  ${self.impuesto:>10.2f}")
        if self.propina > 0:
            print(f"Propina:         ${self.propina:>10.2f}")
        print(f"{'='*60}")
        print(f"TOTAL:           ${self.total:>10.2f}")
        print(f"{'='*60}")
        
        if self.tipo_pago:
            print(f"Método de pago: {self.tipo_pago.value}")


class Inventario:
    """Gestiona el inventario de productos"""
    
    def __init__(self):
        self.productos = {}
        self.alertas_stock_minimo = 5
    
    def agregar_producto(self, producto):
        """Agrega un producto al inventario"""
        self.productos[producto.codigo] = producto
    
    def obtener_producto(self, codigo):
        """Obtiene un producto por código"""
        return self.productos.get(codigo)
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre"""
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)
        return resultados
    
    def productos_bajo_stock(self):
        """Retorna productos con stock bajo"""
        return [p for p in self.productos.values() 
                if p.stock < self.alertas_stock_minimo and p.activo]
    
    def productos_sin_stock(self):
        """Retorna productos sin stock"""
        return [p for p in self.productos.values() 
                if p.stock == 0 and p.activo]
    
    def valor_total_inventario(self):
        """Calcula el valor total del inventario"""
        return sum(p.precio * p.stock for p in self.productos.values())
    
    def reporte_inventario(self):
        """Genera un reporte del inventario"""
        print("\n" + "="*60)
        print("  REPORTE DE INVENTARIO")
        print("="*60)
        
        for categoria in CategoriaProducto:
            productos_cat = [p for p in self.productos.values() 
                           if p.categoria == categoria]
            if productos_cat:
                print(f"\n{categoria.value}:")
                for p in productos_cat:
                    print(f"  - {p}")
        
        print(f"\n{'='*60}")
        print(f"Valor total: ${self.valor_total_inventario():.2f}")
        print(f"Productos bajo stock: {len(self.productos_bajo_stock())}")
        print(f"Productos sin stock: {len(self.productos_sin_stock())}")


class Promocion:
    """Clase para gestionar promociones y descuentos"""
    
    def __init__(self, nombre, descuento, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.descuento = descuento
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.activa = True
    
    def es_valida(self):
        """Verifica si la promoción está vigente"""
        hoy = datetime.now()
        return self.activa and self.fecha_inicio <= hoy <= self.fecha_fin
    
    def __str__(self):
        return f"{self.nombre} - {self.descuento}% OFF"


class Cafeteria:
    """Clase principal de la cafetería"""
    
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.inventario = Inventario()
        self.empleados = []
        self.ordenes = []
        self.promociones = []
        self.fecha_apertura = datetime.now()
    
    def contratar_empleado(self, empleado):
        """Contrata un nuevo empleado"""
        self.empleados.append(empleado)
    
    def despedir_empleado(self, id_empleado):
        """Marca un empleado como inactivo"""
        for empleado in self.empleados:
            if empleado.id == id_empleado:
                empleado.activo = False
                return True
        return False
    
    def obtener_empleado_disponible(self):
        """Obtiene un empleado disponible aleatoriamente"""
        empleados_activos = [e for e in self.empleados if e.activo]
        if empleados_activos:
            return random.choice(empleados_activos)
        return None
    
    def crear_orden(self, cliente, empleado=None):
        """Crea una nueva orden"""
        if not empleado:
            empleado = self.obtener_empleado_disponible()
        
        orden = Orden(cliente, empleado)
        self.ordenes.append(orden)
        return orden
    
    def agregar_promocion(self, promocion):
        """Agrega una nueva promoción"""
        self.promociones.append(promocion)
    
    def obtener_promociones_activas(self):
        """Obtiene promociones vigentes"""
        return [p for p in self.promociones if p.es_valida()]
    
    def obtener_ingresos_totales(self):
        """Calcula los ingresos totales"""
        return sum(orden.total for orden in self.ordenes 
                  if orden.estado == EstadoOrden.ENTREGADA)
    
    def obtener_ingresos_por_periodo(self, fecha_inicio, fecha_fin):
        """Calcula ingresos en un periodo"""
        return sum(orden.total for orden in self.ordenes 
                  if orden.estado == EstadoOrden.ENTREGADA 
                  and fecha_inicio <= orden.fecha_creacion <= fecha_fin)
    
    def obtener_producto_mas_vendido(self):
        """Obtiene el producto más vendido"""
        ventas = {}
        for orden in self.ordenes:
            if orden.estado == EstadoOrden.ENTREGADA:
                for item in orden.items:
                    codigo = item.producto.codigo
                    ventas[codigo] = ventas.get(codigo, 0) + item.cantidad
        
        if ventas:
            codigo_mas_vendido = max(ventas, key=ventas.get)
            return self.inventario.obtener_producto(codigo_mas_vendido), ventas[codigo_mas_vendido]
        return None, 0
    
    def calcular_ticket_promedio(self):
        """Calcula el ticket promedio"""
        ordenes_completadas = [o for o in self.ordenes 
                              if o.estado == EstadoOrden.ENTREGADA]
        if ordenes_completadas:
            total = sum(o.total for o in ordenes_completadas)
            return total / len(ordenes_completadas)
        return 0
    
    def generar_reporte_ventas(self):
        """Genera un reporte de ventas"""
        print("\n" + "="*60)
        print(f"  REPORTE DE VENTAS - {self.nombre}")
        print("="*60)
        print(f"Dirección: {self.direccion}")
        print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"\n{'-'*60}")
        
        ordenes_completadas = [o for o in self.ordenes 
                              if o.estado == EstadoOrden.ENTREGADA]
        
        print(f"Total de órdenes: {len(self.ordenes)}")
        print(f"Órdenes completadas: {len(ordenes_completadas)}")
        print(f"Órdenes pendientes: {len([o for o in self.ordenes if o.estado == EstadoOrden.PENDIENTE])}")
        print(f"Órdenes en preparación: {len([o for o in self.ordenes if o.estado == EstadoOrden.PREPARANDO])}")
        
        print(f"\n{'-'*60}")
        print(f"Ingresos totales: ${self.obtener_ingresos_totales():.2f}")
        print(f"Ticket promedio: ${self.calcular_ticket_promedio():.2f}")
        
        producto_top, cantidad = self.obtener_producto_mas_vendido()
        if producto_top:
            print(f"Producto más vendido: {producto_top.nombre} ({cantidad} unidades)")
        
        print(f"\n{'-'*60}")
        print(f"Empleados activos: {len([e for e in self.empleados if e.activo])}")
        
        if self.empleados:
            empleado_top = max(self.empleados, key=lambda e: e.ordenes_atendidas)
            print(f"Empleado destacado: {empleado_top.nombre} ({empleado_top.ordenes_atendidas} ordenes)")
        
        print("="*60)


def inicializar_datos_ejemplo(cafeteria):
    """Inicializa datos de ejemplo para la cafetería"""
    
    # Agregar productos al inventario
    productos = [
        Producto("BEB001", "Café Americano", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 50),
        Producto("BEB002", "Cappuccino", 4.50, CategoriaProducto.BEBIDA_CALIENTE, 45),
        Producto("BEB003", "Latte", 4.75, CategoriaProducto.BEBIDA_CALIENTE, 40),
        Producto("BEB004", "Espresso", 3.00, CategoriaProducto.BEBIDA_CALIENTE, 60),
        Producto("BEB005", "Té Verde", 3.00, CategoriaProducto.BEBIDA_CALIENTE, 35),
        Producto("BEB006", "Chocolate Caliente", 4.00, CategoriaProducto.BEBIDA_CALIENTE, 30),
        Producto("BEB007", "Frappé", 5.50, CategoriaProducto.BEBIDA_FRIA, 25),
        Producto("BEB008", "Smoothie", 5.00, CategoriaProducto.BEBIDA_FRIA, 20),
        Producto("BEB009", "Jugo Natural", 4.00, CategoriaProducto.BEBIDA_FRIA, 30),
        Producto("PAN001", "Croissant", 2.50, CategoriaProducto.PANADERIA, 40),
        Producto("PAN002", "Muffin", 3.00, CategoriaProducto.PANADERIA, 35),
        Producto("PAN003", "Dona", 2.00, CategoriaProducto.PANADERIA, 50),
        Producto("PAN004", "Bagel", 2.75, CategoriaProducto.PANADERIA, 30),
        Producto("COM001", "Sandwich Club", 6.50, CategoriaProducto.COMIDA, 25),
        Producto("COM002", "Wrap de Pollo", 6.00, CategoriaProducto.COMIDA, 20),
        Producto("COM003", "Ensalada César", 7.50, CategoriaProducto.COMIDA, 15),
        Producto("POS001", "Cheesecake", 5.00, CategoriaProducto.POSTRE, 20),
        Producto("POS002", "Brownie", 3.50, CategoriaProducto.POSTRE, 30),
        Producto("POS003", "Tiramisú", 5.50, CategoriaProducto.POSTRE, 15),
        Producto("SNK001", "Galletas", 2.50, CategoriaProducto.SNACK, 60),
        Producto("SNK002", "Chips", 2.00, CategoriaProducto.SNACK, 50),
    ]
    
    for producto in productos:
        cafeteria.inventario.agregar_producto(producto)
    
    # Contratar empleados
    empleados = [
        Empleado("EMP001", "Ana García", "Barista Senior", 12.50),
        Empleado("EMP002", "Carlos López", "Barista", 10.00),
        Empleado("EMP003", "María Rodríguez", "Cajera", 9.50),
        Empleado("EMP004", "Juan Pérez", "Supervisor", 15.00),
    ]
    
    for empleado in empleados:
        cafeteria.contratar_empleado(empleado)
        empleado.registrar_horas(random.randint(20, 40))
    
    # Crear algunas promociones
    hoy = datetime.now()
    promociones = [
        Promocion("Happy Hour", 15, hoy, hoy + timedelta(days=30)),
        Promocion("Combo Desayuno", 20, hoy, hoy + timedelta(days=15)),
        Promocion("Descuento Estudiantes", 10, hoy, hoy + timedelta(days=90)),
    ]
    
    for promo in promociones:
        cafeteria.agregar_promocion(promo)


def main():
    """Función principal de demostración"""
    print("\n" + "="*60)
    print("  SISTEMA DE GESTIÓN DE CAFETERÍA")
    print("="*60)
    
    # Crear cafetería
    mi_cafeteria = Cafeteria("Café Deluxe", "Av. Principal #123")
    
    # Inicializar datos de ejemplo
    inicializar_datos_ejemplo(mi_cafeteria)
    
    # Mostrar inventario
    mi_cafeteria.inventario.reporte_inventario()
    
    # Mostrar promociones activas
    print("\n" + "="*60)
    print("  PROMOCIONES ACTIVAS")
    print("="*60)
    for promo in mi_cafeteria.obtener_promociones_activas():
        print(f"✨ {promo}")
    
    # Crear algunas órdenes de ejemplo
    print("\n" + "="*60)
    print("  PROCESANDO ÓRDENES")
    print("="*60)
    
    # Orden 1
    orden1 = mi_cafeteria.crear_orden("María González")
    orden1.agregar_item(mi_cafeteria.inventario.obtener_producto("BEB001"), 2)
    orden1.agregar_item(mi_cafeteria.inventario.obtener_producto("PAN001"), 1)
    orden1.agregar_propina(2.00)
    orden1.procesar_pago(TipoPago.TARJETA)
    orden1.cambiar_estado(EstadoOrden.PREPARANDO)
    orden1.cambiar_estado(EstadoOrden.LISTA)
    orden1.cambiar_estado(EstadoOrden.ENTREGADA)
    orden1.mostrar_orden()
    
    # Orden 2
    orden2 = mi_cafeteria.crear_orden("Pedro Martínez")
    orden2.agregar_item(mi_cafeteria.inventario.obtener_producto("BEB002"), 1)
    orden2.agregar_item(mi_cafeteria.inventario.obtener_producto("COM001"), 1)
    orden2.agregar_item(mi_cafeteria.inventario.obtener_producto("POS001"), 1, descuento=15)
    orden2.agregar_propina(3.50)
    exito, cambio = orden2.procesar_pago(TipoPago.EFECTIVO, 30.00)
    if exito:
        print(f"\n💵 Cambio: ${cambio:.2f}")
    orden2.cambiar_estado(EstadoOrden.PREPARANDO)
    orden2.cambiar_estado(EstadoOrden.LISTA)
    orden2.cambiar_estado(EstadoOrden.ENTREGADA)
    orden2.mostrar_orden()
    
    # Orden 3
    orden3 = mi_cafeteria.crear_orden("Laura Sánchez")
    orden3.agregar_item(mi_cafeteria.inventario.obtener_producto("BEB007"), 2)
    orden3.agregar_item(mi_cafeteria.inventario.obtener_producto("SNK001"), 1)
    orden3.aplicar_descuento_total(20)  # Descuento combo
    orden3.procesar_pago(TipoPago.DIGITAL)
    orden3.cambiar_estado(EstadoOrden.PREPARANDO)
    orden3.cambiar_estado(EstadoOrden.LISTA)
    orden3.cambiar_estado(EstadoOrden.ENTREGADA)
    orden3.mostrar_orden()
    
    # Generar reporte de ventas
    mi_cafeteria.generar_reporte_ventas()
    
    # Mostrar alertas de inventario
    print("\n" + "="*60)
    print("  ALERTAS DE INVENTARIO")
    print("="*60)
    productos_bajo_stock = mi_cafeteria.inventario.productos_bajo_stock()
    if productos_bajo_stock:
        print("⚠️ Productos con stock bajo:")
        for p in productos_bajo_stock:
            print(f"  - {p.nombre}: {p.stock} unidades")
    else:
        print("✓ Todos los productos tienen stock adecuado")
    
    # Información de empleados
    print("\n" + "="*60)
    print("  RENDIMIENTO DE EMPLEADOS")
    print("="*60)
    for empleado in mi_cafeteria.empleados:
        if empleado.activo:
            print(f"{empleado}")
            print(f"  Horas trabajadas: {empleado.horas_trabajadas}")
            print(f"  Salario: ${empleado.calcular_salario():.2f}")
            print(f"  Comisión: ${empleado.calcular_comision():.2f}")
            print()
    
    print("="*60)
    print("  FIN DEL REPORTE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
