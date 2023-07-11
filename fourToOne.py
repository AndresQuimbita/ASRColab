import os
import soundfile as sf

def convertir_audio_mono_carpeta(carpeta_entrada, carpeta_salida):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener la lista de archivos en la carpeta de entrada
    archivos = os.listdir(carpeta_entrada)

    for archivo in archivos:
        # Verificar si el archivo es un archivo .wav
        if archivo.endswith(".wav"):
            # Obtener la ruta completa de entrada y salida
            ruta_entrada = os.path.join(carpeta_entrada, archivo)
            ruta_salida = os.path.join(carpeta_salida, archivo)

            # Cargar el audio de entrada
            audio, samplerate = sf.read(ruta_entrada)

            # Verificar si el audio ya es mono
            if audio.shape[1] == 1:
                print(f"El archivo {archivo} ya es mono. Se copiará sin cambios.")
                os.system(f"cp {ruta_entrada} {ruta_salida}")
                continue

            # Convertir el audio a mono
            audio_mono = audio[:, 0]

            # Guardar el audio convertido en formato .wav
            sf.write(ruta_salida, audio_mono, samplerate)


carpeta_entrada = "/home/cslab03/Downloads/wav_separate_sounds/ov1s3_wav"
carpeta_salida = "/home/cslab03/Documents/ASRColab/ASRColab/wav_separate_sounds_mono/ov1s3_wav"
convertir_audio_mono_carpeta(carpeta_entrada, carpeta_salida)
