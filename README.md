# M4A to MP3 Converter

Este script de Python convierte archivos M4A a MP3 en lote utilizando la biblioteca Pydub y requiere la instalación de ffmpeg.

## Requisitos

- Python 3.x
- ffmpeg: Asegúrate de que ffmpeg esté instalado y añadido al PATH. Puedes descargarlo desde [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html).
- Pydub: Puedes instalarlo ejecutando `pip install pydub`

## Estructura del Proyecto

- `main.py`: Script principal que realiza la conversión en lote.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `.gitignore`: Configuración para ignorar archivos y directorios específicos al usar Git.
- `m4a/`: Carpeta de entrada que contiene archivos M4A que se convertirán.
- `mp3/`: Carpeta de salida donde se guardarán los archivos MP3 convertidos.

## Uso

1. Clona el repositorio:

    ```bash
    git clone https://github.com/coding938/m4a-to-mp3.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd m4a-to-mp3
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas basados en Unix
    # o
    venv\Scripts\activate  # Para Windows
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Ejecuta el script para convertir archivos M4A a MP3:

    ```bash
    python main.py
    ```

El script buscará archivos M4A en la carpeta `m4a/` y los convertirá, guardando los archivos MP3 resultantes en la carpeta `mp3/`.

## Contribuciones

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, por favor, crea un problema o envía una solicitud de extracción.

## Licencia
