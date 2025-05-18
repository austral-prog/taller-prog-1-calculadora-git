# 📟 Calculadora Colaborativa con Git

## Objetivo del Proyecto

Construir entre todos una calculadora en Python que integre diferentes funciones matemáticas, cada una desarrollada en ramas separadas y luego fusionadas al proyecto principal, practicando:

- Creación y manejo de ramas
- Resolución de conflictos
- Trabajo colaborativo
- Organización de código

## 🛠️ Instrucciones Técnicas
### Estructura del Proyecto

```
calculadora/
├── main.py          # Menú principal
├── operaciones/     # Módulos con funciones
│   ├── __init__.py
│   ├── basicas.py
│   ├── avanzadas.py
│   └── especiales.py
└── tests/           # Pruebas unitarias
```

### Pasos para Contribuir

1. Clonar el repositorio:

```bash
git clone [URL-del-repositorio]
cd calculadora
```

2. Crear una rama para tu función (nomenclatura):

```bash
git checkout -b feature/tu-nombre-funcion
```

Ejemplos:

- feature/maria-suma
- feature/carlos-raiz-cuadrada

3. Implementar tu función:

- Añadir código en el archivo correspondiente:
  - basicas.py (+, -, *, /)
  - avanzadas.py (^, √, log)
  - especiales.py (factorial, ecuaciones)
- Incluir pruebas unitarias en tests/

4. Hacer commit:

```bash
git add .
git commit -m "Añadida función de [nombre-funcion]"
git push origin feature/tu-nombre-funcion
```

### ⚠️ Escenarios de Conflicto (Planificados)

1. Archivo main.py: Varios alumnos modifican el menú principal simultáneamente

2. Importaciones: Conflictos en __init__.py al exportar funciones

3. Documentación: Ediciones concurrentes en el README.md

### 🔍 Cómo Resolver Conflictos Típicos

Cuando ocurra un conflicto en main.py:

```python
<<<<<<< HEAD
    print("1. Suma\n2. Resta")
=======
    print("1. Operaciones Básicas\n2. Cálculos Avanzados")
>>>>>>> feature/ana-menu
```

#### Solución:

1. Editar manualmente conservando lo mejor de ambos
2. Eliminar marcadores <<<<<<<, =======, >>>>>>>
3. Confirmar los cambios:

```bash
git add .
git commit -m "Resuelto conflicto en menú"
```

### 📌 Reglas de Colaboración

1. Antes de empezar:

```bash
git pull origin main
```

2. Comunicación: Usar Issues para asignar funciones o comentar en Slack/Discord qué archivos estás modificando

3. Estilo de código: Documentar funciones con docstrings

### 🧪 Pruebas Unitarias
Cada función debe incluir su test:

```python
# tests/test_basicas.py
def test_suma():
    assert suma(2, 3) == 5
```
