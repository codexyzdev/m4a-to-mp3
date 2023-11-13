from pydub import AudioSegment
import os

# Antes de la importación de pydub
os.environ["PATH"] += os.pathsep + r"C:\Ffmpeg\bin"

from pydub import AudioSegment

def convertir_m4a_a_mp3(archivo_m4a, carpeta_salida):
    # Cargar el archivo M4A
    audio = AudioSegment.from_file(archivo_m4a, format="m4a")

    # Crear la ruta de salida para el archivo MP3
    nombre_archivo = os.path.splitext(os.path.basename(archivo_m4a))[0]
    ruta_salida = os.path.join(carpeta_salida, f"{nombre_archivo}.mp3")

    # Convertir y guardar el archivo MP3
    audio.export(ruta_salida, format="mp3")
    print(f"Convertido: {ruta_salida}")


def batch_convertir_m4a_a_mp3(carpeta_entrada, carpeta_salida):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener la lista de archivos M4A en la carpeta de entrada
    archivos_m4a = [f for f in os.listdir(
        carpeta_entrada) if f.endswith(".m4a")]

    # Convertir cada archivo M4A a MP3
    for archivo_m4a in archivos_m4a:
        ruta_m4a = os.path.join(carpeta_entrada, archivo_m4a)
        convertir_m4a_a_mp3(ruta_m4a, carpeta_salida)


# Rutas de entrada y salida
carpeta_entrada = "./m4a"
carpeta_salida = "./mp3"

# Convertir archivos en lote
batch_convertir_m4a_a_mp3(carpeta_entrada, carpeta_salida)
