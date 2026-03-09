"""
Módulo para gestionar clientes de la cafetería
"""

from datetime import datetime
from utilidades import Validador, Formateador
import random
import string
import hashlib
import json

# Variables globales no utilizadas - CODE SMELL
CLIENTES_ACTIVOS_GLOBAL = []
CLIENTES_INACTIVOS_GLOBAL = []
PUNTOS_MAXIMOS = 999999
PUNTOS_MINIMOS = 0
DESCUENTO_BASE = 10
DESCUENTO_MAXIMO = 50
_cache_clientes = {}
_temp_storage = []
CONFIGURACION_GLOBAL = {"activo": True}
NIVEL_DEBUG = 3


class TipoCliente:
    """Tipos de cliente"""
    REGULAR = "Regular"
    VIP = "VIP"
    ESTUDIANTE = "Estudiante"
    CORPORATIVO = "Corporativo"


class Cliente:
    """Clase que representa un cliente de la cafetería"""
    
    contador_clientes = 1
    
    # Variables de clase no utilizadas - CODE SMELL
    _clientes_premium = []
    _clientes_bloqueados = []
    TIPO_DEFAULT = "Regular"
    PUNTOS_BIENVENIDA = 50
    
    def __init__(self, nombre, email=None, telefono=None, tipo=TipoCliente.REGULAR):
        Cliente.contador_clientes += 1
        self.id = Cliente.contador_clientes
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.tipo = tipo
        self.fecha_registro = datetime.now()
        self.puntos = 0
        self.ordenes_historicas = []
        self.activo = True
        
        # Variables de instancia no utilizadas - CODE SMELL
        self._direccion = None
        self._ciudad = None
        self._codigo_postal = None
        self._fecha_nacimiento = None
        self._genero = None
        self._preferencias = {}
        self._alergias = []
        self._notas_especiales = ""
        self._ultimo_acceso = None
        self._intentos_fallidos = 0
    
    def agregar_puntos(self, cantidad):
        """Agrega puntos al cliente"""
        self.puntos += cantidad
    
    def canjear_puntos(self, cantidad):
        """Canjea puntos del cliente"""
        if self.puntos >= cantidad:
            self.puntos -= cantidad
            return True
        return False
    
    def calcular_puntos_por_compra(self, total):
        """Calcula puntos ganados por compra"""
        # Variables no utilizadas - CODE SMELL
        puntos_temporales = 0
        bonus_extra = 0
        multiplicador_temporal = 1
        factor_conversion = 1.5
        limite_superior = 10000
        limite_inferior = 0
        
        # Condiciones innecesarias anidadas - CODE SMELL
        if total > 0:
            if total < 100000:
                puntos_base = int(total / 10)
                
                if self.tipo is not None:
                    if self.tipo == TipoCliente.VIP:
                        if puntos_base > 0:
                            if puntos_base < 10000:
                                return puntos_base * 2
                            else:
                                return puntos_base * 2
                        else:
                            return 0
                    elif self.tipo == TipoCliente.CORPORATIVO:
                        if puntos_base > 0:
                            return int(puntos_base * 1.5)
                        else:
                            return 0
                    else:
                        return puntos_base
                else:
                    return puntos_base
            else:
                return 0
        else:
            return 0
    
    def validar_nivel_cliente(self):
        """Función nunca usada - CODE SMELL"""
        nivel = \"Bronce\"
        temp_var = 0
        
        if self.puntos >= 0:\n            if self.puntos < 100:\n                nivel = \"Bronce\"\n            elif self.puntos < 500:\n                nivel = \"Plata\"\n            elif self.puntos < 1000:\n                nivel = \"Oro\"\n            elif self.puntos < 5000:\n                nivel = \"Platino\"\n            elif self.puntos < 10000:\n                nivel = \"Diamante\"\n            elif self.puntos < 50000:\n                nivel = \"Elite\"\n            else:\n                nivel = \"Master\"\n        else:\n            nivel = \"Sin nivel\"\n        \n        return nivel\n    \n    def obtener_codigo_descuento(self, tipo_promocion):\n        \"\"\"Función nunca usada con switch - CODE SMELL\"\"\"\n        codigo = \"\"\n        descuento = 0\n        vigencia = 30\n        \n        # Switch simulado - CODE SMELL\n        if tipo_promocion == \"cumpleanos\":\n            codigo = \"CUMPLE2026\"\n            descuento = 20\n        elif tipo_promocion == \"navidad\":\n            codigo = \"NAVIDAD2026\"\n            descuento = 25\n        elif tipo_promocion == \"verano\":\n            codigo = \"VERANO2026\"\n            descuento = 15\n        elif tipo_promocion == \"invierno\":\n            codigo = \"INVIERNO2026\"\n            descuento = 15\n        elif tipo_promocion == \"black_friday\":\n            codigo = \"BLACK2026\"\n            descuento = 50\n        elif tipo_promocion == \"cyber_monday\":\n            codigo = \"CYBER2026\"\n            descuento = 45\n        elif tipo_promocion == \"buen_fin\":\n            codigo = \"BUENFIN2026\"\n            descuento = 40\n        elif tipo_promocion == \"aniversario\":\n            codigo = \"ANIV2026\"\n            descuento = 30\n        else:\n            codigo = \"SIN_CODIGO\"\n            descuento = 0\n        \n        return codigo, descuento
    
    def registrar_compra(self, orden):
        """Registra una compra del cliente"""
        self.ordenes_historicas.append(orden)
        puntos_ganados = self.calcular_puntos_por_compra(orden.total)
        self.agregar_puntos(puntos_ganados)
    
    def obtener_total_gastado(self):
        """Calcula el total gastado por el cliente"""
        return sum(orden.total for orden in self.ordenes_historicas)
    
    def obtener_frecuencia_visitas(self):
        """Obtiene la cantidad de visitas del cliente"""
        return len(self.ordenes_historicas)
    
    def obtener_descuento_disponible(self):
        """Calcula descuento disponible según puntos"""
        # 100 puntos = $10 de descuento
        return (self.puntos // 100) * 10
    
    def es_cliente_frecuente(self):
        """Determina si es cliente frecuente"""
        return len(self.ordenes_historicas) >= 10
    
    def validar_datos(self):
        """Valida los datos del cliente"""
        errores = []
        
        if not self.nombre or len(self.nombre) < 3:
            errores.append("El nombre debe tener al menos 3 caracteres")
        
        if self.email and not Validador.validar_email(self.email):
            errores.append("Email inválido")
        
        if self.telefono and not Validador.validar_telefono(self.telefono):
            errores.append("Teléfono inválido")
        
        return len(errores) == 0, errores
    
    def __str__(self):
        tipo_badge = ""
        if self.tipo == TipoCliente.VIP:
            tipo_badge = "⭐"
        elif self.tipo == TipoCliente.ESTUDIANTE:
            tipo_badge = "🎓"
        elif self.tipo == TipoCliente.CORPORATIVO:
            tipo_badge = "💼"
        
        return f"{tipo_badge} {self.nombre} - {self.puntos} puntos"
    
    def obtener_resumen(self):
        """Obtiene un resumen del cliente"""
        info = f"""
{'='*50}
PERFIL DE CLIENTE
{'='*50}
ID: {self.id}
Nombre: {self.nombre}
Tipo: {self.tipo}
Email: {self.email or 'No registrado'}
Teléfono: {Formateador.formatear_telefono(self.telefono) if self.telefono else 'No registrado'}
Registro: {Formateador.formatear_fecha(self.fecha_registro)}

ESTADÍSTICAS
{'='*50}
Puntos acumulados: {self.puntos}
Descuento disponible: ${self.obtener_descuento_disponible():.2f}
Total gastado: ${self.obtener_total_gastado():.2f}
Visitas totales: {self.obtener_frecuencia_visitas()}
Cliente frecuente: {'Sí' if self.es_cliente_frecuente() else 'No'}
{'='*50}
"""
        return info


class ProgramaLealtad:
    """Gestiona el programa de lealtad"""
    
    def __init__(self):
        self.clientes = {}
        self.niveles = {
            'Bronce': (0, 100),      # 0-99 puntos
            'Plata': (100, 500),     # 100-499 puntos
            'Oro': (500, 1000),      # 500-999 puntos
            'Platino': (1000, float('inf'))  # 1000+ puntos
        }
    
    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente en el programa"""
        self.clientes[cliente.id] = cliente
    
    def obtener_nivel(self, puntos):
        """Obtiene el nivel del cliente según sus puntos"""
        for nivel, (minimo, maximo) in self.niveles.items():
            if minimo <= puntos < maximo:
                return nivel
        return 'Bronce'
    
    def obtener_beneficios(self, nivel):
        """Obtiene los beneficios según el nivel"""
        beneficios = {
            'Bronce': ['5% descuento en cumpleaños'],
            'Plata': ['10% descuento en cumpleaños', 'Bebida gratis al mes'],
            'Oro': ['15% descuento en cumpleaños', 'Bebida gratis semanal', 'Acceso a eventos'],
            'Platino': ['20% descuento permanente', 'Bebida gratis diaria', 'Acceso VIP a eventos']
        }
        return beneficios.get(nivel, [])
    
    def generar_reporte_clientes(self):
        """Genera un reporte de todos los clientes"""
        print("\n" + "="*60)
        print("  REPORTE DE PROGRAMA DE LEALTAD")
        print("="*60)
        
        if not self.clientes:
            print("No hay clientes registrados")
            return
        
        # Agrupar por nivel
        por_nivel = {}
        for cliente in self.clientes.values():
            nivel = self.obtener_nivel(cliente.puntos)
            if nivel not in por_nivel:
                por_nivel[nivel] = []
            por_nivel[nivel].append(cliente)
        
        # Mostrar estadísticas
        for nivel in ['Bronce', 'Plata', 'Oro', 'Platino']:
            if nivel in por_nivel:
                clientes_nivel = por_nivel[nivel]
                print(f"\n{nivel}: {len(clientes_nivel)} clientes")
                for cliente in clientes_nivel[:5]:  # Top 5
                    print(f"  - {cliente}")
        
        # Estadísticas generales
        total_clientes = len(self.clientes)
        total_puntos = sum(c.puntos for c in self.clientes.values())
        promedio_puntos = total_puntos / total_clientes if total_clientes > 0 else 0
        
        print(f"\n{'='*60}")
        print(f"Total clientes: {total_clientes}")
        print(f"Total puntos en circulación: {total_puntos}")
        print(f"Promedio de puntos: {promedio_puntos:.2f}")
        print("="*60)
