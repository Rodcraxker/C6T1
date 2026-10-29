# C6T1
Implementación de Funciones y Procedimientos para la Resolución de Problemas Reales

# Sistema Modular Automatizado - Funciones y Procedimientos

Este repositorio contiene la solución modular desarrollada en Python para cinco desafíos de optimización de sistemas en contextos reales (edificios inteligentes, logística, vehículos autónomos, fábricas industriales y agricultura de precisión).

## Estructura del Proyecto y Modularidad

El código se estructuró dividiendo cada dominio en funciones y procedimientos específicos con responsabilidad única. Esto evita la duplicación de código, mejora la legibilidad y optimiza el rendimiento del sistema en tiempo de ejecución.

### Explicación de Funciones y su Impacto en el Rendimiento

#### 1. Control de Temperatura (Edificio Inteligente)
* **`leer_sensores_temperatura` y `calcular_temperatura_optima`**: Aíslan la lógica de adquisición de datos y toma de decisiones heurísticas. Permiten realizar cálculos bajo demanda sin sobrecargar el bucle principal de ejecución del sistema.
* **`enviar_senal_climatizacion` y `registrar_analizar_consumo`**: Procedimientos dedicados al control de actuadores y análisis financiero energético, facilitando la escalabilidad del sistema a cientos de zonas del edificio sin alterar la lógica central.

#### 2. Gestión de Inventario (Almacén)
* **`registrar_entrada` y `registrar_salida`**: Modifican de forma limpia y segura la estructura de datos del diccionario en memoria, reduciendo la complejidad algorítmica de búsqueda y actualización.
* **`calcular_nivel_optimo_inventario` y `generar_alertas_reabastecimiento`**: Separan el procesamiento matemático del control lógico de stock, permitiendo auditorías rápidas y eficientes del inventario.

#### 3. Sistema de Navegación (Vehículo Autónomo)
* **`leer_sensores_proximidad` y `detectar_y_evitar_obstaculos`**: Optimizan la respuesta en tiempo real del vehículo al procesar vectores de cercanía de forma independiente y modular.
* **`calcular_ruta_optima` y `ajustar_velocidad_vehiculo`**: Dividen la planificación macroscópica (rutas) de la microscópica (velocidad y tráfico), reduciendo la latencia de procesamiento crítico en el hardware del vehículo.

#### 4. Optimización de Producción (Fábrica)
* **`monitorear_estado_maquinas` y `planificar_mantenimiento_preventivo`**: Monitorean el ciclo de vida de los equipos mediante funciones puras que evitan cálculos redundantes de desgaste.
* **`analizar_rendimiento_produccion` y `ajustar_programacion_produccion`**: Facilitan la toma de decisiones gerenciales automatizadas basadas en indicadores OEE procesados modularmente.

#### 5. Riego Automatizado (Agricultura)
* **`leer_sensores_humedad_suelo` y `consultar_prevision_meteorologica`**: Centralizan las entradas de datos externos (IoT y APIs meteorológicas).
* **`calcular_cantidad_riego` y `controlar_valvulas_riego`**: Optimizan el consumo hídrico aplicando algoritmos condicionales estrictos que impiden el desperdicio de agua y reducen el consumo energético de las bombas hidráulicas.

## Instrucciones de Ejecución
Asegúrate de tener instalado Python 3.x. Puedes importar las funciones en tu script principal (`main.py`) para realizar pruebas unitarias o simulaciones de los sistemas.
