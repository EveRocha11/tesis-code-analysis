"""
Módulo de utilidades para el sistema de cafetería
"""

import re
from datetime import datetime
import os
import sys
import json
import hashlib

# Variables globales no utilizadas - CODE SMELL
CONFIGURACION_APP = {}
CACHE_VALIDACIONES = {}
HISTORIAL_OPERACIONES = []
CONTADOR_OPERACIONES = 0
_temp_data_global = []
_configuracion_debug = True
MAX_INTENTOS_VALIDACION = 10
TIMEOUT_OPERACION = 300
PATH_CONFIGURACION = \"/config\"
NOMBRE_APLICACION = \"Cafeteria System\"


class Validador:
    """Clase para validar diferentes tipos de datos"""
    
    @staticmethod
    def validar_email(email):
        """Valida formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    @staticmethod
    def validar_telefono(telefono):
        """Valida formato de teléfono (10 dígitos)"""
        patron = r'^\d{10}$'
        return re.match(patron, telefono.replace('-', '').replace(' ', '')) is not None
    
    @staticmethod
    def validar_precio(precio):
        """Valida que el precio sea válido"""
        # Variables no utilizadas - CODE SMELL
        precio_minimo = 0
        precio_maximo = 999999
        precision_decimal = 2
        
        try:
            precio_float = float(precio)
            
            # Condiciones innecesarias - CODE SMELL
            if precio_float is not None:
                if precio_float > 0:
                    if precio_float < 1000000:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validar_rango_precio(precio, min_precio, max_precio):
        """Función nunca usada - CODE SMELL"""
        temp1 = 0
        temp2 = 0
        
        if precio >= min_precio and precio <= max_precio:
            return True
        else:
            return False
    
    @staticmethod
    def validar_codigo_producto(codigo):
        """Función duplicada nunca usada - CODE SMELL"""
        prefijos_validos = ["BEB", "PAN", "COM", "POS", "SNK"]
        resultado = False
        
        if codigo:
            for prefijo in prefijos_validos:
                if codigo.startswith(prefijo):
                    resultado = True
                    break
        
        return resultado
    
    @staticmethod
    def validar_cantidad(cantidad):
        """Valida que la cantidad sea válida"""
        try:
            cantidad_int = int(cantidad)
            return cantidad_int > 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def validar_fecha(fecha_str, formato='%Y-%m-%d'):
        """Valida formato de fecha"""
        try:
            datetime.strptime(fecha_str, formato)
            return True
        except ValueError:
            return False


class Formateador:
    """Clase para formatear datos"""
    
    @staticmethod
    def formatear_moneda(cantidad):
        """Formatea cantidad como moneda"""
        return f"${cantidad:,.2f}"
    
    @staticmethod
    def formatear_fecha(fecha, formato='%d/%m/%Y'):
        """Formatea fecha"""
        if isinstance(fecha, datetime):
            return fecha.strftime(formato)
        return str(fecha)
    
    @staticmethod
    def formatear_fecha_hora(fecha, formato='%d/%m/%Y %H:%M:%S'):
        """Formatea fecha y hora"""
        if isinstance(fecha, datetime):
            return fecha.strftime(formato)
        return str(fecha)
    
    @staticmethod
    def formatear_telefono(telefono):
        """Formatea número de teléfono"""
        numeros = ''.join(filter(str.isdigit, telefono))
        if len(numeros) == 10:
            return f"({numeros[:3]}) {numeros[3:6]}-{numeros[6:]}"
        return telefono
    
    @staticmethod
    def formatear_porcentaje(valor, decimales=2):
        """Formatea valor como porcentaje"""
        return f"{valor:.{decimales}f}%"


class Calculadora:
    """Clase con funciones de cálculo"""
    
    # Variables de clase no utilizadas - CODE SMELL
    _historial_calculos = []
    PRECISION_DECIMALES = 2
    REDONDEO_ACTIVO = True
    
    @staticmethod
    def calcular_descuento(precio, porcentaje):
        """Calcula el descuento"""
        # Variables no utilizadas - CODE SMELL
        descuento_minimo = 0
        descuento_maximo = 100
        factor_ajuste = 1.0
        
        # Condiciones innecesarias - CODE SMELL
        if precio > 0:
            if porcentaje >= 0:
                if porcentaje <= 100:
                    if precio < 1000000:
                        return precio * (porcentaje / 100)
                    else:
                        return precio * (porcentaje / 100)
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    
    @staticmethod
    def calcular_precio_con_descuento(precio, porcentaje):
        """Calcula precio con descuento aplicado"""
        descuento = Calculadora.calcular_descuento(precio, porcentaje)
        return precio - descuento
    
    @staticmethod
    def calcular_impuesto(subtotal, tasa):
        """Calcula el impuesto"""
        return subtotal * tasa
    
    @staticmethod
    def calcular_total(subtotal, tasa_impuesto=0.16, descuento=0):
        """Calcula el total con impuesto y descuento"""
        subtotal_con_descuento = subtotal - (subtotal * descuento / 100)
        impuesto = Calculadora.calcular_impuesto(subtotal_con_descuento, tasa_impuesto)
        return subtotal_con_descuento + impuesto
    
    @staticmethod
    def calcular_propina_sugerida(subtotal, porcentaje=15):
        """Calcula propina sugerida"""
        return subtotal * (porcentaje / 100)
    
    @staticmethod
    def calcular_promedio(valores):
        """Calcula el promedio de una lista de valores"""
        if not valores:
            return 0
        return sum(valores) / len(valores)
    
    @staticmethod
    def calcular_porcentaje_variacion(valor_anterior, valor_actual):
        """Calcula porcentaje de variación entre dos valores"""
        if valor_anterior == 0:
            return 0
        return ((valor_actual - valor_anterior) / valor_anterior) * 100


class GeneradorReportes:
    """Clase para generar reportes en diferentes formatos"""
    
    @staticmethod
    def generar_linea_separadora(longitud=60, caracter='='):
        """Genera una línea separadora"""
        return caracter * longitud
    
    @staticmethod
    def centrar_texto(texto, ancho=60):
        """Centra un texto en un ancho específico"""
        return texto.center(ancho)
    
    @staticmethod
    def generar_encabezado(titulo, ancho=60):
        """Genera un encabezado para reportes"""
        separador = GeneradorReportes.generar_linea_separadora(ancho)
        titulo_centrado = GeneradorReportes.centrar_texto(titulo, ancho)
        return f"\n{separador}\n{titulo_centrado}\n{separador}"
    
    @staticmethod
    def generar_tabla_simple(encabezados, filas, ancho_columnas=None):
        """Genera una tabla simple"""
        if not ancho_columnas:
            ancho_columnas = [15] * len(encabezados)
        
        # Crear línea de encabezados
        encabezado_str = "| "
        for i, enc in enumerate(encabezados):
            encabezado_str += f"{enc:<{ancho_columnas[i]}} | "
        
        # Crear línea separadora
        separador = "+" + "+".join(["-" * (ancho + 2) for ancho in ancho_columnas]) + "+"
        
        # Crear filas
        tabla = [separador, encabezado_str, separador]
        
        for fila in filas:
            fila_str = "| "
            for i, valor in enumerate(fila):
                fila_str += f"{str(valor):<{ancho_columnas[i]}} | "
            tabla.append(fila_str)
        
        tabla.append(separador)
        return "\n".join(tabla)


def limpiar_texto(texto):
    """Limpia y normaliza texto"""
    if not texto:
        return ""
    return " ".join(texto.split()).strip()


def es_numero(valor):
    """Verifica si un valor es numérico"""
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False


def truncar_decimal(valor, decimales=2):
    """Trunca un valor decimal a n decimales"""
    multiplicador = 10 ** decimales
    return int(valor * multiplicador) / multiplicador


def obtener_fecha_actual():
    """Obtiene la fecha actual"""
    return datetime.now()


def calcular_dias_entre_fechas(fecha1, fecha2):
    """Calcula días entre dos fechas"""
    if isinstance(fecha1, datetime) and isinstance(fecha2, datetime):
        diferencia = fecha2 - fecha1
        return abs(diferencia.days)
    return 0


def generar_codigo_unico(prefijo, numero):
    """Genera un código único con formato"""
    return f"{prefijo}{numero:04d}"
