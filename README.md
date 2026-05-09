# Proyecto de automatización de saucedemo

### Cursada: Automatización QA

### Autor: Cristian Alderete

### Profesor: Brayann Farfan
### Tutora: Amancay Arribillaga

## Link del Repositorio
[Repositorio en GitHub](https://github.com/CristianAld91/pre-entrega-automation-testing--cristian-alderete-)

## Propósito del Proyecto
Este proyecto tiene como objetivo automatizar las pruebas de la aplicación web de Sauce Labs utilizando Selenium. Se verifican funcionalidades clave como el inicio de sesión, la visualización del catálogo de productos, la adición de productos al carrito y la interacción con el menú lateral. El propósito es asegurar que la aplicación funcione correctamente y cumpla con los requisitos establecidos.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación utilizado para escribir las pruebas.
- **Selenium**: Herramienta para la automatización de navegadores web.
- **pytest**: Framework de pruebas utilizado para ejecutar y gestionar las pruebas.
- **WebDriver**: Interfaz para controlar un navegador web a través de código.

## Resultados Esperados
Al ejecutar las pruebas, deberías ver un resumen que indique el número de pruebas pasadas y fallidas. Si todas las pruebas pasan, significa que la aplicación funciona como se espera.

## Comandos Utilizados en las Pruebas

Ejecuta los siguientes comandos para correr las pruebas:

```bash
pytest tests/test_saucedemo.py -v
pytest tests/test_saucedemo.py::test_login -v
pytest tests/test_saucedemo.py::test_catalogo_productos -v
pytest tests/test_saucedemo.py::test_agregar_producto_al_carrito -v
pytest tests/test_saucedemo.py::test_menu_lateral -v
```
## Reporte de Pruebas

Este documento proporciona un resumen de los casos de prueba ejecutados y sus resultados, generados en el archivo `reporte.html`. Este reporte es el resultado de la ejecución de pruebas automatizadas utilizando `pytest` y `pytest-html`, y contiene información detallada sobre el estado de cada prueba.

## Descripción del Reporte

El archivo `reporte.html` incluye la siguiente información:

1. **Resumen General**:
   - **Total de Pruebas Ejecutadas**: Indica el número total de pruebas que se han ejecutado durante la sesión.
   - **Estado de las Pruebas**: Muestra cuántas pruebas han pasado, cuántas han fallado y si hubo errores durante la ejecución.
   - **Duración Total**: El tiempo total que tomó ejecutar todas las pruebas.

2. **Detalles de Cada Prueba**:
   - Cada prueba se presenta con su nombre, duración y estado (pasada, fallida, etc.).
   - Se incluyen logs y mensajes de error para las pruebas que no han tenido éxito, lo que facilita el diagnóstico de problemas.

3. **Interactividad**:
   - El reporte permite filtrar los resultados por estado (pasadas, fallidas, etc.), lo que ayuda a concentrarse en áreas específicas que requieren atención.
   - Los detalles de las pruebas pueden expandirse o colapsarse, permitiendo una visualización más clara y organizada de la información.

## Cómo Generar el Reporte

Para generar el reporte, asegúrate de tener instaladas las dependencias necesarias y ejecuta el siguiente comando:

```bash
pytest tests/test_saucedemo.py --html=reporte.html
```

## Instrucciones de Instalación de Dependencias
Para instalar las dependencias necesarias, asegúrate de tener Python y pip instalados en tu sistema. Luego, ejecuta el siguiente comando en tu terminal:
```bash
pip install -r requirements.txt
