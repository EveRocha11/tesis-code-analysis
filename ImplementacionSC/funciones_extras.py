"""
Módulo con funciones adicionales nunca utilizadas - CODE SMELL
Este archivo completo es un code smell ya que nunca se importa ni usa
"""

import random
import string
import hashlib
from datetime import datetime, timedelta

# Variables globales no utilizadas - CODE SMELL
CONFIGURACION_EXTRA = {}
DATOS_TEMPORALES = []
CACHE_FUNCIONES = {}
CONTADOR_LLAMADAS = 0
_variable_privada_1 = "sin_uso"
_variable_privada_2 = 12345
_variable_privada_3 = True
CONSTANTE_PI = 3.14159
CONSTANTE_E = 2.71828
MAX_ITERACIONES = 1000


def funcion_nunca_usada_1(parametro1, parametro2):
    """Función completamente innecesaria - CODE SMELL"""
    resultado = 0
    temp1 = 0
    temp2 = 0
    temp3 = 0
    
    # Condiciones innecesarias anidadas - CODE SMELL
    if parametro1 is not None:
        if parametro2 is not None:
            if parametro1 > 0:
                if parametro2 > 0:
                    if parametro1 < 1000:
                        if parametro2 < 1000:
                            resultado = parametro1 + parametro2
                        else:
                            resultado = parametro1
                    else:
                        resultado = parametro2
                else:
                    resultado = parametro1
            else:
                resultado = parametro2
        else:
            resultado = parametro1
    else:
        resultado = 0
    
    return resultado


def funcion_nunca_usada_2(lista_datos):
    """Función duplicada innecesaria - CODE SMELL"""
    resultado_final = []
    contador = 0
    suma_total = 0
    promedio = 0
    
    if lista_datos:
        if len(lista_datos) > 0:
            if len(lista_datos) < 10000:
                for dato in lista_datos:
                    if dato is not None:
                        if isinstance(dato, (int, float)):
                            if dato > 0:
                                resultado_final.append(dato * 2)
                            elif dato < 0:
                                resultado_final.append(dato * -1)
                            else:
                                resultado_final.append(0)
                        else:
                            resultado_final.append(0)
                    else:
                        resultado_final.append(0)
            else:
                return []
        else:
            return []
    else:
        return []
    
    return resultado_final


def calcular_algo_complejo(valor1, valor2, valor3, valor4, valor5):
    """Función con alta complejidad ciclomática - CODE SMELL"""
    resultado = 0
    temp_a = 0
    temp_b = 0
    temp_c = 0
    temp_d = 0
    temp_e = 0
    
    # Muchas condiciones anidadas - CODE SMELL
    if valor1 > 0:
        if valor2 > 0:
            if valor3 > 0:
                if valor4 > 0:
                    if valor5 > 0:
                        resultado = valor1 + valor2 + valor3 + valor4 + valor5
                    else:
                        if valor1 > 10:
                            resultado = valor1 * 2
                        else:
                            resultado = valor1
                else:
                    if valor2 > 10:
                        resultado = valor2 * 2
                    else:
                        resultado = valor2
            else:
                if valor3 > 10:
                    resultado = valor3 * 2
                else:
                    resultado = valor3
        else:
            if valor4 > 10:
                resultado = valor4 * 2
            else:
                resultado = valor4
    else:
        if valor5 > 10:
            resultado = valor5 * 2
        else:
            resultado = valor5
    
    return resultado


def validar_datos_complejos(dato):
    """Función con switch case simulado nunca usada - CODE SMELL"""
    tipo_dato = type(dato).__name__
    resultado = False
    mensaje = ""
    codigo_error = 0
    
    # Switch simulado con muchos elif - CODE SMELL
    if tipo_dato == "str":
        if len(dato) > 0:
            resultado = True
            mensaje = "String válido"
        else:
            resultado = False
            mensaje = "String vacío"
    elif tipo_dato == "int":
        if dato >= 0:
            resultado = True
            mensaje = "Entero válido"
        else:
            resultado = False
            mensaje = "Entero negativo"
    elif tipo_dato == "float":
        if dato >= 0.0:
            resultado = True
            mensaje = "Float válido"
        else:
            resultado = False
            mensaje = "Float negativo"
    elif tipo_dato == "list":
        if len(dato) > 0:
            resultado = True
            mensaje = "Lista válida"
        else:
            resultado = False
            mensaje = "Lista vacía"
    elif tipo_dato == "dict":
        if len(dato) > 0:
            resultado = True
            mensaje = "Diccionario válido"
        else:
            resultado = False
            mensaje = "Diccionario vacío"
    elif tipo_dato == "tuple":
        resultado = True
        mensaje = "Tupla válida"
    elif tipo_dato == "set":
        resultado = True
        mensaje = "Set válido"
    elif tipo_dato == "bool":
        resultado = True
        mensaje = "Booleano válido"
    else:
        resultado = False
        mensaje = "Tipo desconocido"
    
    return resultado, mensaje


def procesar_lista_compleja(lista):
    """Función nunca usada con código duplicado - CODE SMELL"""
    resultado = []
    temp_lista = []
    contador_items = 0
    suma_valores = 0
    
    if lista is not None:
        if isinstance(lista, list):
            if len(lista) > 0:
                for item in lista:
                    if item is not None:
                        if isinstance(item, int):
                            if item > 0:
                                if item < 100:
                                    resultado.append(item * 2)
                                elif item < 500:
                                    resultado.append(item * 1.5)
                                elif item < 1000:
                                    resultado.append(item * 1.2)
                                else:
                                    resultado.append(item)
                            else:
                                resultado.append(0)
                        elif isinstance(item, float):
                            resultado.append(int(item))
                        elif isinstance(item, str):
                            try:
                                resultado.append(int(item))
                            except:
                                resultado.append(0)
                        else:
                            resultado.append(0)
                    else:
                        resultado.append(0)
            else:
                return []
        else:
            return []
    else:
        return []
    
    return resultado


def generar_codigo_aleatorio(longitud):
    """Función nunca usada - CODE SMELL"""
    caracteres = string.ascii_uppercase + string.digits
    codigo = ""
    temp_var = 0
    
    if longitud > 0:
        if longitud < 100:
            for i in range(longitud):
                codigo += random.choice(caracteres)
        else:
            codigo = "ERROR_LONGITUD"
    else:
        codigo = "ERROR"
    
    return codigo


def calcular_hash_datos(datos):
    """Función nunca usada - CODE SMELL"""
    hash_resultado = ""
    temp_hash = ""
    
    if datos:
        if isinstance(datos, str):
            hash_resultado = hashlib.md5(datos.encode()).hexdigest()
        else:
            hash_resultado = hashlib.md5(str(datos).encode()).hexdigest()
    else:
        hash_resultado = "SIN_DATOS"
    
    return hash_resultado


class ClaseInnecesaria:
    """Clase completamente innecesaria - CODE SMELL"""
    
    # Variables de clase no utilizadas
    contador_instancias = 0
    lista_instances = []
    CONSTANTE_CLASE = "VALOR"
    
    def __init__(self, valor):
        self.valor = valor
        self.timestamp = datetime.now()
        
        # Variables de instancia no utilizadas
        self._privada1 = None
        self._privada2 = 0
        self._privada3 = []
        self._privada4 = {}
    
    def metodo_nunca_usado_1(self):
        """Método nunca usado"""
        temp1 = 0
        temp2 = 0
        return temp1 + temp2
    
    def metodo_nunca_usado_2(self, parametro):
        """Método nunca usado"""
        if parametro:
            if isinstance(parametro, int):
                return parametro * 2
            else:
                return 0
        else:
            return 0
    
    def metodo_nunca_usado_3(self):
        """Método nunca usado con complejidad"""
        resultado = 0
        
        for i in range(100):
            if i % 2 == 0:
                if i % 3 == 0:
                    if i % 5 == 0:
                        resultado += i
                    else:
                        resultado += i / 2
                else:
                    resultado += i / 3
            else:
                resultado += i
        
        return resultado


# Código duplicado - CODE SMELL
def duplicado_funcion_1(a, b):
    """Función duplicada 1"""
    if a > b:
        return a - b
    else:
        return b - a


def duplicado_funcion_2(x, y):
    """Función duplicada 2 - exactamente igual a la anterior"""
    if x > y:
        return x - y
    else:
        return y - x


def duplicado_funcion_3(m, n):
    """Función duplicada 3 - exactamente igual a las anteriores"""
    if m > n:
        return m - n
    else:
        return n - m
