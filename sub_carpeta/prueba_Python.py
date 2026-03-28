from time import time

def vender_boletos ( cantidad ) :
    global boletos_disponibles
    # Simula latencia de I/O en consulta de base de datos
    temp = boletos_disponibles
    time.sleep (0.0001)
    boletos_disponibles = temp - cantidad
# Tarea : Instanciar m ́u ltiples hilos que ejecuten esta funci  ́on
# de forma concurrente . Verificar inconsistencia en el resultado final .

