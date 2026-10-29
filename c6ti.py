"""
Autor: Rod Muñoz
Tema: Funciones y Procedimientos (Parte 1)
Descripción: Implementación modular para resolver 5 problemas del mundo real 
utilizando funciones y procedimientos reutilizables, con ejemplos de ejecución.
"""

# =====================================================================
# PROBLEMA 1: Control de Temperatura en un Edificio Inteligente
# =====================================================================

def leer_sensores_temperatura(zona_id):
    """Simula la lectura de datos de sensores de temperatura y condiciones de una zona."""
    print(f"[Sensor] Leyendo datos de la zona {zona_id}...")
    return {"temperatura_actual": 24.5, "ocupacion": True, "clima_exterior": "caluroso"}

def calcular_temperatura_optima(hora, ocupacion, clima_externo):
    """Calcula la temperatura ideal basada en heurísticas de ahorro energético."""
    if not ocupacion:
        return 28.0  # Modo ahorro si no hay nadie
    if 8 <= hora <= 18:
        return 21.5  # Confort laboral diurno
    return 24.0      # Horario nocturno

def enviar_senal_climatizacion(zona_id, temperatura_objetivo, temperatura_actual):
    """Procedimiento que envía señales al sistema de calefacción/refrigeración."""
    if temperatura_actual < temperatura_objetivo:
        print(f"-> Zona {zona_id}: Activando CALEFACCIÓN para alcanzar {temperatura_objetivo}°C.")
    elif temperatura_actual > temperatura_objetivo:
        print(f"-> Zona {zona_id}: Activando REFRIGERACIÓN para alcanzar {temperatura_objetivo}°C.")
    else:
        print(f"-> Zona {zona_id}: Temperatura estable. Sin cambios necesarios.")

def registrar_analizar_consumo(zona_id, energia_consumida_kwh):
    """Registra y analiza métricas del consumo energético por zona."""
    costo_estimado = energia_consumida_kwh * 0.12 # Tarifa por kWh
    print(f"[Reporte Energía] Zona {zona_id} consumió {energia_consumida_kwh} kWh (Costo: ${costo_estimado:.2f}).")
    return {"zona": zona_id, "kwh": energia_consumida_kwh, "costo": costo_estimado}


# =====================================================================
# PROBLEMA 2: Gestión de Inventario en un Almacén
# =====================================================================

def registrar_entrada(inventario, producto_id, cantidad):
    """Registra la entrada de nuevos productos al stock actual."""
    if producto_id in inventario:
        inventario[producto_id]["stock"] += cantidad
    else:
        inventario[producto_id] = {"stock": cantidad, "minimo": 10}
    print(f"[Inventario] Ingreso exitoso: +{cantidad} unidades del producto {producto_id}.")
    return inventario

def registrar_salida(inventario, producto_id, cantidad):
    """Registra la salida o despacho de productos del almacén."""
    if producto_id in inventario and inventario[producto_id]["stock"] >= cantidad:
        inventario[producto_id]["stock"] -= cantidad
        print(f"[Inventario] Despacho exitoso: -{cantidad} unidades del producto {producto_id}.")
    else:
        print(f"[Inventario] Error: Stock insuficiente o producto {producto_id} no encontrado.")
    return inventario

def calcular_nivel_optimo_inventario(demanda_historica_promedio, dias_entrega):
    """Calcula el stock de seguridad y el nivel óptimo de inventario."""
    stock_seguridad = demanda_historica_promedio * 2
    nivel_optimo = (demanda_historica_promedio * dias_entrega) + stock_seguridad
    return nivel_optimo

def generar_alertas_reabastecimiento(inventario):
    """Analiza el inventario actual y genera alertas si el stock está por debajo del mínimo."""
    alertas = []
    for prod_id, datos in inventario.items():
        if datos["stock"] <= datos["minimo"]:
            alertas.append(f"ALERTA: El producto {prod_id} requiere reabastecimiento (Stock: {datos['stock']}).")
    return alertas


# =====================================================================
# PROBLEMA 3: Sistema de Navegación para un Vehículo Autónomo
# =====================================================================

def leer_sensores_proximidad():
    """Lee matrices de cámaras y LiDAR para capturar distancias de objetos cercanos."""
    return {"frontal": 15.5, "lateral_izq": 3.0, "lateral_der": 2.8, "trasero": 10.0}

def calcular_ruta_optima(origen, destino):
    """Calcula la ruta geoespacial óptima minimizando tráfico y distancia."""
    print(f"[Navegación] Calculando la ruta más eficiente de '{origen}' a '{destino}'...")
    return ["Punto A", "Punto B", "Destino"]

def detectar_y_evitar_obstaculos(datos_sensores):
    """Evalúa los datos de los sensores para determinar si es necesario evadir un obstáculo."""
    if datos_sensores["frontal"] < 5.0:
        print("[Alerta] ¡Obstáculo detectado a corta distancia! Iniciando maniobra evasiva.")
        return "Frenado de emergencia / Giro"
    print("[Navegación] Trayectoria frontal libre.")
    return "Trayectoria libre"

def ajustar_velocidad_vehiculo(condiciones_trafico):
    """Ajusta dinámicamente la velocidad del vehículo autónomo según el tráfico."""
    velocidades = {"fluido": 80, "moderado": 50, "congestionado": 20}
    vel_asignada = velocidades.get(condiciones_trafico, 60)
    print(f"[Control Velocidad] Velocidad ajustada a {vel_asignada} km/h por tráfico '{condiciones_trafico}'.")
    return vel_asignada


# =====================================================================
# PROBLEMA 4: Optimización de la Producción en una Fábrica
# =====================================================================

def monitorear_estado_maquinas(maquina_id):
    """Monitorea variables operativas de la maquinaria industrial en tiempo real."""
    return {"id": maquina_id, "temperatura_motor": 75.0, "vibracion": "normal", "operativa": True}

def planificar_mantenimiento_preventivo(horas_uso_acumuladas):
    """Planifica alertas de mantenimiento preventivo basadas en ciclos de desgaste."""
    if horas_uso_acumuladas > 500:
        print(f"[Mantenimiento] Máquina con {horas_uso_acumuladas} hrs. Programando revisión técnica.")
        return True
    return False

def analizar_rendimiento_produccion(unidades_producidas, tiempo_operacion_horas):
    """Analiza la eficiencia global de los equipos y tasa de producción por hora."""
    tasa = unidades_producidas / max(tiempo_operacion_horas, 1)
    print(f"[Rendimiento] Tasa de producción estimada: {tasa:.2f} unidades/hora.")
    return tasa

def ajustar_programacion_produccion(demanda_mercado):
    """Ajusta líneas de ensamblaje y turnos en función de la demanda comercial."""
    if demanda_mercado > 1000:
        print("[Producción] Demanda alta detectada. Activando turno extra de manufactura.")
    else:
        print("[Producción] Demanda estable. Manteniendo programación regular.")


# =====================================================================
# PROBLEMA 5: Sistema de Riego Automatizado para Agricultura
# =====================================================================

def leer_sensores_humedad_suelo(seccion_id):
    """Lee el porcentaje de humedad actual en la tierra de una sección específica."""
    print(f"[Sensor Suelo] Leyendo humedad de la sección agrícola {seccion_id}...")
    return 32.5

def consultar_prevision_meteorologica(ubicacion):
    """Consulta servicios meteorológicos externos sobre probabilidad de lluvia próxima."""
    print(f"[Clima] Consultando pronóstico para {ubicacion}...")
    return {"probabilidad_lluvia": 10, "temperatura_ambiente": 28.0}

def calcular_cantidad_riego(humedad_suelao, pronostico_lluvia):
    """Calcula los litros exactos de agua requeridos según la sequedad del suelo y clima."""
    if pronostico_lluvia["probabilidad_lluvia"] > 60:
        print("[Riego] Alta probabilidad de lluvia detectada. Suspendiendo riego.")
        return 0.0
    if humedad_suelao < 40.0:
        litros_necesarios = (40.0 - humedad_suelao) * 50
        print(f"[Riego] Suelo seco ({humedad_suelao}%). Litros calculados: {litros_necesarios}L.")
        return litros_necesarios
    print("[Riego] Humedad óptima. No se requiere riego.")
    return 0.0

def controlar_valvulas_riego(seccion_id, litros_agua):
    """Controla la apertura y cierre físico de las electroválvulas de riego."""
    if litros_agua > 0:
        print(f"-> Válvula {seccion_id}: ABIERTA para dispensar {litros_agua} litros de agua.")
    else:
        print(f"-> Válvula {seccion_id}: CERRADA.")


# =====================================================================
# BLOQUE DE EJECUCIÓN PRINCIPAL (Para ver resultados en consola)
# =====================================================================
if __name__ == "__main__":
    print("==================================================")
    print("EJECUTANDO SIMULACIÓN DE SISTEMAS MODULARES")
    print("==================================================\n")
    
    print("--- 1. Edificio Inteligente ---")
    datos_zona = leer_sensores_temperatura("Zona-A1")
    temp_ideal = calcular_temperatura_optima(14, datos_zona["ocupacion"], datos_zona["clima_exterior"])
    enviar_senal_climatizacion("Zona-A1", temp_ideal, datos_zona["temperatura_actual"])
    registrar_analizar_consumo("Zona-A1", 15.4)
    
    print("\n--- 2. Gestión de Inventario ---")
    inventario_almacen = {}
    inventario_almacen = registrar_entrada(inventario_almacen, "P001", 8) # Deja stock por debajo del mínimo (10)
    alertas = generar_alertas_reabastecimiento(inventario_almacen)
    for alerta in alertas:
        print(alerta)
        
    print("\n--- 3. Vehículo Autónomo ---")
    sensores = leer_sensores_proximidad()
    calcular_ruta_optima("Central", "Destino Norte")
    detectar_y_evitar_obstaculos(sensores)
    ajustar_velocidad_vehiculo("moderado")
    
    print("\n--- 4. Optimización de Fábrica ---")
    monitorear_estado_maquinas("CNC-01")
    planificar_mantenimiento_preventivo(600) # Supera las 500 horas
    analizar_rendimiento_produccion(350, 7)
    ajustar_programacion_produccion(1250)
    
    print("\n--- 5. Riego Automatizado ---")
    humedad = leer_sensores_humedad_suelo("Campo-Norte")
    clima = consultar_prevision_meteorologica("Valle")
    litros = calcular_cantidad_riego(humedad, clima)
    controlar_valvulas_riego("Campo-Norte", litros)
    
    print("\n==================================================")
    print("SIMULACIÓN FINALIZADA CON ÉXITO")
    print("==================================================")