import time

def tarea_larga():
    for i in range(10):
        # Simulamos una tarea que tarda en realizarse
        time.sleep(0.5)
        # Actualizamos la barra de progreso
        print(str(i), end="\r", flush=True)

tarea_larga()
