#!/usr/bin/env python

# https://www.youtube.com/watch?v=Srvt_6up-0o : url de prueba

# importamos la libreria subprocess para controlar la ejecución de comandos manualmente
import subprocess

dependencies = {
    "yt-dlp": False,
    "nodejs": False,
    "ffmpeg": False
}

def ytdlp_available():
    module_status = False

    try:
        # Ejecutamos el proceso para verificar si existe la librería en el sistema
        result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)

        if result.returncode == 0:
            module_status = True

    except FileNotFoundError:
        print("[*] yt-dlp no está disponible en el sistema.") 
        print("[*] Ejecuta: yt-dlp --version") 
        print("[*] Si falla:\n - activa tu entorno virtual\n - reinstala dependencias\n - revisa installation.md")

    return module_status

def nodejs_availabe():
    nodejs_status = False

    try: 
        # Ejecutamos el proceso para verificar si existe el paquete nodejs en el sistema
        result = subprocess.run(["node", "--version"], stdout=subprocess.PIPE, text=True)

        if result.returncode == 0:
            nodejs_status = True

    except FileNotFoundError:
        print("[*] nodejs no está disponible en el sistema.") 
        print("[*] Ejecuta: node --version") 
        print("[*] Si falla:\n - activa tu entorno virtual\n - reinstala dependencias\n - revisa installation.md")
        
    
    return nodejs_status

def ffmpeg_available():
    
    ffmpeg_status = False
    
    try: 
        # Ejecutamos el proceso para verificar si existe el paquete ffmepeg en el sistema
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, text=True)

        if result.returncode == 0:
            ffmpeg_status = True

    except FileNotFoundError:
        print("[*] ffmpeg no está disponible en el sistema.") 
        print("[*] Ejecuta: ffmpeg -version") 
        print("[*] Si falla:\n - activa tu entorno virtual\n - reinstala dependencias\n - revisa installation.md")    
        
    return ffmpeg_status

def get_url():
    
    while True:
        # Obtenemos la url del video que el usuario quiere extraerle el audio
        url = input("Ingresa la URL del video de YouTube al cual deseas descargar el audio: "). strip()
    
        # Si la url no está vacía la retornamos 
        if url:
            return url

        # Mostramos el mensaje para que el usuario verifique        
        print("No escribiste nada o solo pusiste espacios.")


def download_audio(url):

    progress_previous = 0

    # Ejecutamos el comando de descarga
    result = subprocess.Popen(["yt-dlp", "-x", "--audio-format", "mp3", "--audio-quality", "5", url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Leemos linea por linea el proceso (liberando el buffering del sistema)
    for line in result.stdout:
        #print(line)

        if "error" in line.lower():
            print(line.strip())

        contains_percent = "%" in line

        if line.startswith("[download]") and contains_percent:
            # Separamos para obtener los valores indivualmente y obtenemos lo que nos interesa,  el valor del porcentaje de descarga con [1]
            progress_percent = line.split()[1]

            # Limpiar el dato que nos interesa y lo cambiamos a float
            progress_current = float(progress_percent.replace("%", ""))
            
            # Validamos que solo mostremos unicamente cuando el progreso actual sea distinto del previous(early-return)
            if progress_current != progress_previous:
                # Asignamos el progreso actual para que sea el previo en la siguiente iteracion
                progress_previous = progress_current

                # Mostramos el porcentaje de descarga
                print(f"Descargando: {progress_current}")


    result.wait()
    return result.returncode


def main():

    is_ytdlp_installed = ytdlp_available() 
    is_nodejs_installed = nodejs_availabe()
    is_ffmpeg_installed = ffmpeg_available()

    dependencies["yt-dlp"] = is_ytdlp_installed
    dependencies["nodejs"] = is_nodejs_installed
    dependencies["ffmpeg"] = is_ffmpeg_installed

    # Validamos que todas las dependencias están instalada correctamente
    if all(dependencies.values()):

        # Obtenemos la url y se la pasamos al descargador
        url = get_url()

        # Descargamos el audio
        download_result = download_audio(url)

        if download_result == 0:
            print("Audio extraido exitosamente")
        else:
            print("No se pudo descargar el audio. Verifica la URL o revisa el mensaje mostrado.")
    else:
        print("No se puede iniciar el programa. Revisa las dependencias faltantes.")
    


if __name__ == "__main__":
    main()

# https://www.youtube.com/watch?v=Srvt_6up-0o