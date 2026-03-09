# Sistema de Cafetería en Python

Sistema completo de gestión de cafetería con múltiples módulos y funcionalidades avanzadas.

## 📋 Descripción

Sistema integral de gestión de cafetería que incluye:
- **Gestión de productos** (bebidas, comidas, panadería, postres, snacks)
- **Inventario inteligente** con alertas de stock
- **Sistema de órdenes** con estados y seguimiento
- **Gestión de empleados** con registro de horas y comisiones
- **Programa de lealtad** para clientes con puntos y niveles
- **Promociones y descuentos** con vigencia temporal
- **Reportes detallados** de ventas, inventario y rendimiento
- **Sistema de pagos** múltiples tipos (efectivo, tarjeta, digital)
- **Validaciones y utilidades** para manejo de datos
- **Suite completa de pruebas unitarias**

## 🏗️ Arquitectura del Proyecto

El proyecto está organizado en módulos especializados:

- `cafeteria.py` - Núcleo del sistema (Productos, Órdenes, Inventario, Empleados)
- `cliente.py` - Gestión de clientes y programa de lealtad
- `utilidades.py` - Validadores, calculadoras y formateadores
- `controladores.py` - Clases Controller/Manager/Service (CODE SMELLS)
- `funciones_extras.py` - Funciones adicionales nunca usadas (CODE SMELLS)
- `test_cafeteria.py` - Suite completa de pruebas unitarias

## 🚀 Requisitos

- Python 3.8 o superior
- pytest (para ejecutar las pruebas)

## 📦 Instalación

1. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 🎯 Uso

### Ejecutar la aplicación principal
```bash
python cafeteria.py
```

Esto ejecutará una demostración completa que incluye:
- Inicialización de inventario con 20+ productos
- Creación de empleados
- Configuración de promociones
- Procesamiento de órdenes de ejemplo
- Generación de reportes

### Ejecutar pruebas unitarias
```bash
# Ejecutar todas las pruebas
pytest test_cafeteria.py -v

# Con cobertura de código
pytest test_cafeteria.py --cov=cafeteria --cov=cliente --cov=utilidades

# Generar reporte HTML de cobertura
pytest test_cafeteria.py --cov=. --cov-report=html
```

## 📁 Estructura del Proyecto

```
ImplementacionSC/
│
├── cafeteria.py          # Módulo principal del sistema
│   ├── CategoriaProducto (Enum)
│   ├── TipoPago (Enum)
│   ├── EstadoOrden (Enum)
│   ├── Producto
│   ├── ItemOrden
│   ├── Empleado
│   ├── Orden
│   ├── Inventario
│   ├── Promocion
│   └── Cafeteria
│
├── cliente.py            # Gestión de clientes
│   ├── TipoCliente
│   ├── Cliente
│   └── ProgramaLealtad
│
├── utilidades.py         # Funciones auxiliares
│   ├── Validador
│   ├── Formateador
│   ├── Calculadora
│   └── GeneradorReportes
│
├── controladores.py      # Clases Controller (CODE SMELLS)
│   ├── CafeteriaManager
│   ├── OrderProcessController
│   ├── InventoryControlService
│   ├── PaymentProcessHandler
│   └── ReportGeneratorProcess
│
├── funciones_extras.py   # Funciones nunca usadas (CODE SMELLS)
├── test_cafeteria.py     # Pruebas unitarias (40+ tests)
├── requirements.txt      # Dependencias
└── README.md            # Esta documentación
```

## 🔍 Características Detalladas

### Gestión de Productos
- Categorización por tipo (Bebidas, Comidas, Postres, etc.)
- Control de stock automático
- Aplicación de descuentos
- Estado activo/inactivo

### Sistema de Órdenes
- Estados: Pendiente → Preparando → Lista → Entregada
- Cálculo automático de subtotales e impuestos
- Soporte para descuentos por item
- Gestión de propinas
- Múltiples métodos de pago

### Gestión de Empleados
- Registro de horas trabajadas
- Cálculo de salarios
- Comisiones por ventas
- Tracking de órdenes atendidas

### Programa de Lealtad
- 4 niveles: Bronce, Plata, Oro, Platino
- Acumulación de puntos por compras
- Descuentos según nivel
- Beneficios escalonados

### Reportes y Analytics
- Reporte de ventas con estadísticas
- Análisis de inventario
- Producto más vendido
- Ticket promedio
- Rendimiento de empleados
- Alertas de stock bajo

## 💡 Ejemplos de Uso en Código

### Crear y gestionar una cafetería
```python
from cafeteria import Cafeteria, Producto, CategoriaProducto

# Crear cafetería
cafe = Cafeteria("Mi Café", "Calle Principal 123")

# Agregar productos
producto = Producto("BEB001", "Café Americano", 3.50, 
                    CategoriaProducto.BEBIDA_CALIENTE, stock=50)
cafe.inventario.agregar_producto(producto)

# Crear orden
orden = cafe.crear_orden("Juan Pérez")
orden.agregar_item(producto, cantidad=2)
orden.procesar_pago(TipoPago.TARJETA)
```

### Gestionar clientes
```python
from cliente import Cliente, TipoCliente, ProgramaLealtad

# Crear cliente
cliente = Cliente("María García", "maria@email.com", 
                  tipo=TipoCliente.VIP)

# Registrar compra y puntos
cliente.registrar_compra(orden)
print(f"Puntos: {cliente.puntos}")
```

### Usar utilidades
```python
from utilidades import Validador, Calculadora, Formateador

# Validar datos
if Validador.validar_email("test@email.com"):
    print("Email válido")

# Calcular descuento
precio_final = Calculadora.calcular_precio_con_descuento(100, 20)

# Formatear moneda
print(Formateador.formatear_moneda(1234.56))  # $1,234.56
```

## 🧪 Pruebas

El proyecto incluye más de 40 pruebas unitarias que cubren:
- Creación y validación de objetos
- Lógica de negocio
- Cálculos matemáticos
- Manejo de estados
- Validaciones de datos
- Casos límite y errores

## 🔧 Análisis con SonarQube

Este proyecto está diseñado para ser analizado con SonarQube para detectar:
- Code smells
- Bugs potenciales
- Vulnerabilidades de seguridad
- Duplicación de código
- Complejidad ciclomática
- Deuda técnica
25+
- **Métodos**: 150+
- **Líneas de código**: 2000+
- **Tests**: 40+
- **Módulos**: 6
- **Code Smells Intencionados**: 200+r-scanner`

## 📊 Métricas del Proyecto

- **Clases**: 15+
- **Métodos**: 100+
- **Líneas de código**: 1000+
- **Tests**: 40+
- **Módulos**: 4

## 🎓 Propósito Educativo

Este proyecto sirve como ejemplo completo de:
- Programación orientada a objetos en Python
- Arquitectura modular
- Testing con pytest
- Buenas prácticas de desarrollo
- Documentación de código
- Análisis de calidad con SonarQube

## 📝 Licencia

Proyecto de ejemplo para fines educativos.
