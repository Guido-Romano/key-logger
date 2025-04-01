# Keylogger en Python

Una herramienta desarrollada en Python para capturar y registrar las teclas presionadas por un usuario.

## Características
- Monitorea y registra todas las pulsaciones del teclado.
- Guarda el registro en un archivo de texto.
- Se ejecuta en segundo plano hasta que el usuario lo detiene manualmente (usando tecla "escape".

## Requisitos
- Python 3.x
- Librería `pynput` (puede instalarse con `pip install pynput`)

## Instalación y Uso
### Para distribuciones basadas en Debian (Parrot, Kali, etc.)
```bash
sudo apt update && sudo apt install python3 python3-pip -y
pip install pynput
python3 key-logger.py
```

### Para distribuciones basadas en Arch (Arch Linux, BlackArch, etc.)
```bash
sudo pacman -S python python-pip --noconfirm
pip install pynput
python key-logger.py
```

### Para distribuciones basadas en Red Hat (CentOS, Fedora, etc.)
```bash
sudo dnf install python3 python3-pip -y
pip install pynput
python3 key-logger.py
```

## Cómo funciona
1. El script inicia un listener que monitorea las teclas presionadas.
2. Guarda las pulsaciones en un archivo de texto (`keylog.txt`).
3. Se ejecuta en segundo plano hasta que se presiona la tecla `Escape`, momento en el que el programa finaliza y guarda el archivo.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## Agradecimientos
Gracias a la librería `pynput` por facilitar la captura de eventos del teclado en Python.
