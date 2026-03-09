"""
Pruebas unitarias para el sistema de cafetería
"""

import pytest
from datetime import datetime, timedelta
from cafeteria import (
    Producto, ItemOrden, Orden, Cafeteria, Empleado, Inventario,
    CategoriaProducto, TipoPago, EstadoOrden, Promocion
)
from cliente import Cliente, TipoCliente, ProgramaLealtad
from utilidades import Validador, Calculadora, Formateador


class TestProducto:
    """Pruebas para la clase Producto"""
    
    def test_crear_producto(self):
        """Prueba crear un producto"""
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 50)
        assert producto.nombre == "Café"
        assert producto.precio == 3.50
        assert producto.stock == 50
        assert producto.activo is True
    
    def test_descontar_stock(self):
        """Prueba descontar stock"""
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        assert producto.descontar_stock(3) is True
        assert producto.stock == 7
    
    def test_descontar_stock_insuficiente(self):
        """Prueba descontar más stock del disponible"""
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 2)
        assert producto.descontar_stock(5) is False
        assert producto.stock == 2
    
    def test_agregar_stock(self):
        """Prueba agregar stock"""
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        producto.agregar_stock(5)
        assert producto.stock == 15
    
    def test_aplicar_descuento(self):
        """Prueba aplicar descuento"""
        producto = Producto("BEB001", "Café", 10.00, CategoriaProducto.BEBIDA_CALIENTE, 10)
        precio_descuento = producto.aplicar_descuento(20)
        assert precio_descuento == 8.00


class TestItemOrden:
    """Pruebas para la clase ItemOrden"""
    
    def test_crear_item(self):
        """Prueba crear un item de orden"""
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        item = ItemOrden(producto, 2)
        assert item.cantidad == 2
        assert item.subtotal == 7.00
    
    def test_item_con_descuento(self):
        """Prueba item con descuento"""
        producto = Producto("BEB001", "Café", 10.00, CategoriaProducto.BEBIDA_CALIENTE, 10)
        item = ItemOrden(producto, 2, descuento=20)
        assert item.subtotal == 16.00  # 20 con 20% descuento


class TestEmpleado:
    """Pruebas para la clase Empleado"""
    
    def test_crear_empleado(self):
        """Prueba crear un empleado"""
        empleado = Empleado("EMP001", "Juan", "Barista", 10.00)
        assert empleado.nombre == "Juan"
        assert empleado.ordenes_atendidas == 0
    
    def test_registrar_orden(self):
        """Prueba registrar orden atendida"""
        empleado = Empleado("EMP001", "Juan", "Barista", 10.00)
        empleado.registrar_orden()
        empleado.registrar_orden()
        assert empleado.ordenes_atendidas == 2
    
    def test_calcular_salario(self):
        """Prueba calcular salario"""
        empleado = Empleado("EMP001", "Juan", "Barista", 10.00)
        empleado.registrar_horas(40)
        assert empleado.calcular_salario() == 400.00


class TestOrden:
    """Pruebas para la clase Orden"""
    
    def test_crear_orden(self):
        """Prueba crear una orden"""
        orden = Orden("Cliente Test")
        assert orden.cliente == "Cliente Test"
        assert len(orden.items) == 0
        assert orden.total == 0.0
        assert orden.estado == EstadoOrden.PENDIENTE
    
    def test_agregar_item_a_orden(self):
        """Prueba agregar item a orden"""
        orden = Orden("Cliente")
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        orden.agregar_item(producto, 1)
        assert len(orden.items) == 1
        assert orden.subtotal == 3.50
    
    def test_agregar_propina(self):
        """Prueba agregar propina"""
        orden = Orden("Cliente")
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        orden.agregar_item(producto, 1)
        orden.agregar_propina(2.00)
        assert orden.propina == 2.00
    
    def test_calcular_total_con_impuesto(self):
        """Prueba cálculo de total con impuesto"""
        orden = Orden("Cliente")
        producto = Producto("BEB001", "Café", 10.00, CategoriaProducto.BEBIDA_CALIENTE, 10)
        orden.agregar_item(producto, 1)
        # 10.00 + 16% impuesto = 11.60
        assert orden.total == pytest.approx(11.60, 0.01)
    
    def test_cambiar_estado_orden(self):
        """Prueba cambiar estado de orden"""
        orden = Orden("Cliente")
        orden.cambiar_estado(EstadoOrden.PREPARANDO)
        assert orden.estado == EstadoOrden.PREPARANDO
    
    def test_procesar_pago_efectivo(self):
        """Prueba procesar pago en efectivo"""
        orden = Orden("Cliente")
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        orden.agregar_item(producto, 1)
        exito, cambio = orden.procesar_pago(TipoPago.EFECTIVO, 10.00)
        assert exito is True
        assert cambio > 0


class TestInventario:
    """Pruebas para la clase Inventario"""
    
    def test_crear_inventario(self):
        """Prueba crear inventario"""
        inventario = Inventario()
        assert len(inventario.productos) == 0
    
    def test_agregar_producto_inventario(self):
        """Prueba agregar producto al inventario"""
        inventario = Inventario()
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        inventario.agregar_producto(producto)
        assert len(inventario.productos) == 1
    
    def test_obtener_producto(self):
        """Prueba obtener producto por código"""
        inventario = Inventario()
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        inventario.agregar_producto(producto)
        prod = inventario.obtener_producto("BEB001")
        assert prod.nombre == "Café"
    
    def test_buscar_por_nombre(self):
        """Prueba buscar productos por nombre"""
        inventario = Inventario()
        inventario.agregar_producto(Producto("BEB001", "Café Americano", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10))
        inventario.agregar_producto(Producto("BEB002", "Café Latte", 4.50, CategoriaProducto.BEBIDA_CALIENTE, 10))
        resultados = inventario.buscar_por_nombre("Café")
        assert len(resultados) == 2
    
    def test_productos_bajo_stock(self):
        """Prueba obtener productos con bajo stock"""
        inventario = Inventario()
        inventario.agregar_producto(Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 2))
        inventario.agregar_producto(Producto("BEB002", "Té", 3.00, CategoriaProducto.BEBIDA_CALIENTE, 20))
        bajo_stock = inventario.productos_bajo_stock()
        assert len(bajo_stock) == 1


class TestPromocion:
    """Pruebas para la clase Promocion"""
    
    def test_crear_promocion(self):
        """Prueba crear promoción"""
        hoy = datetime.now()
        futuro = hoy + timedelta(days=30)
        promo = Promocion("Descuento", 20, hoy, futuro)
        assert promo.nombre == "Descuento"
        assert promo.descuento == 20
    
    def test_promocion_valida(self):
        """Prueba si promoción está vigente"""
        hoy = datetime.now()
        futuro = hoy + timedelta(days=30)
        promo = Promocion("Descuento", 20, hoy, futuro)
        assert promo.es_valida() is True
    
    def test_promocion_expirada(self):
        """Prueba promoción expirada"""
        ayer = datetime.now() - timedelta(days=2)
        hoy = datetime.now() - timedelta(days=1)
        promo = Promocion("Descuento", 20, ayer, hoy)
        assert promo.es_valida() is False


class TestCafeteria:
    """Pruebas para la clase Cafeteria"""
    
    def test_crear_cafeteria(self):
        """Prueba crear cafetería"""
        cafeteria = Cafeteria("Mi Café", "Calle 123")
        assert cafeteria.nombre == "Mi Café"
        assert len(cafeteria.ordenes) == 0
    
    def test_contratar_empleado(self):
        """Prueba contratar empleado"""
        cafeteria = Cafeteria("Mi Café", "Calle 123")
        empleado = Empleado("EMP001", "Juan", "Barista", 10.00)
        cafeteria.contratar_empleado(empleado)
        assert len(cafeteria.empleados) == 1
    
    def test_crear_orden_cafeteria(self):
        """Prueba crear orden en cafetería"""
        cafeteria = Cafeteria("Mi Café", "Calle 123")
        orden = cafeteria.crear_orden("Cliente")
        assert len(cafeteria.ordenes) == 1
    
    def test_ingresos_totales(self):
        """Prueba calcular ingresos totales"""
        cafeteria = Cafeteria("Mi Café", "Calle 123")
        producto = Producto("BEB001", "Café", 3.50, CategoriaProducto.BEBIDA_CALIENTE, 10)
        cafeteria.inventario.agregar_producto(producto)
        
        orden = cafeteria.crear_orden("Cliente")
        orden.agregar_item(producto, 1)
        orden.cambiar_estado(EstadoOrden.ENTREGADA)
        
        ingresos = cafeteria.obtener_ingresos_totales()
        assert ingresos > 0


class TestCliente:
    """Pruebas para la clase Cliente"""
    
    def test_crear_cliente(self):
        """Prueba crear cliente"""
        cliente = Cliente("Juan Pérez", "juan@email.com", "1234567890")
        assert cliente.nombre == "Juan Pérez"
        assert cliente.puntos == 0
    
    def test_agregar_puntos(self):
        """Prueba agregar puntos"""
        cliente = Cliente("Juan Pérez")
        cliente.agregar_puntos(100)
        assert cliente.puntos == 100
    
    def test_canjear_puntos(self):
        """Prueba canjear puntos"""
        cliente = Cliente("Juan Pérez")
        cliente.agregar_puntos(100)
        exito = cliente.canjear_puntos(50)
        assert exito is True
        assert cliente.puntos == 50
    
    def test_canjear_puntos_insuficientes(self):
        """Prueba canjear más puntos de los disponibles"""
        cliente = Cliente("Juan Pérez")
        cliente.agregar_puntos(50)
        exito = cliente.canjear_puntos(100)
        assert exito is False
        assert cliente.puntos == 50


class TestValidador:
    """Pruebas para la clase Validador"""
    
    def test_validar_email_correcto(self):
        """Prueba validar email correcto"""
        assert Validador.validar_email("test@example.com") is True
    
    def test_validar_email_incorrecto(self):
        """Prueba validar email incorrecto"""
        assert Validador.validar_email("test@") is False
    
    def test_validar_precio(self):
        """Prueba validar precio"""
        assert Validador.validar_precio(10.50) is True
        assert Validador.validar_precio(-5) is False
    
    def test_validar_cantidad(self):
        """Prueba validar cantidad"""
        assert Validador.validar_cantidad(5) is True
        assert Validador.validar_cantidad(0) is False


class TestCalculadora:
    """Pruebas para la clase Calculadora"""
    
    def test_calcular_descuento(self):
        """Prueba calcular descuento"""
        descuento = Calculadora.calcular_descuento(100, 20)
        assert descuento == 20.0
    
    def test_calcular_precio_con_descuento(self):
        """Prueba calcular precio con descuento"""
        precio_final = Calculadora.calcular_precio_con_descuento(100, 20)
        assert precio_final == 80.0
    
    def test_calcular_impuesto(self):
        """Prueba calcular impuesto"""
        impuesto = Calculadora.calcular_impuesto(100, 0.16)
        assert impuesto == 16.0
    
    def test_calcular_propina_sugerida(self):
        """Prueba calcular propina sugerida"""
        propina = Calculadora.calcular_propina_sugerida(100, 15)
        assert propina == 15.0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
