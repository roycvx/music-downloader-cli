# Instalación y uso

## Requisitos previos

Antes de instalar el proyecto, asegúrate de tener instalado lo siguiente en tu sistema:

- Git
- Python **3.10 o superior**
- Node.js
- FFmpeg

Puedes verificar que todo esté correctamente instalado ejecutando estos comandos en tu terminal:

```bash
git --version
python --version
node --version
ffmpeg -version
```

Si todo está configurado correctamente, deberías obtener una salida similar a esta:

```bash
git version 2.54.0
Python 3.14.4
v24.13.1
ffmpeg version 8.0.1 Copyright (c) 2000-2025 the FFmpeg developers
```

> **Nota:** Las versiones mostradas son solo ejemplos. No es necesario que coincidan exactamente.

---

## Instalación local

### 1. Clonar el repositorio

Ejecuta el siguiente comando en el directorio donde deseas descargar el proyecto:

```bash
git clone https://github.com/roycvx/music-downloader-cli.git
```

### 2. Entrar al directorio del proyecto

```bash
cd music-downloader-cli
```

### 3. Abrir el proyecto (opcional)

Puedes abrir el proyecto con tu editor de código preferido. Por ejemplo, usando Visual Studio Code:

```bash
code .
```

### 4. Instalar dependencias

Instala las dependencias de Python:

```bash
pip install -r requirements.txt
```

Si el proyecto también utiliza dependencias de Node.js, ejecuta:

```bash
npm install
```

### 5. Ejecutar el proyecto

Inicia la aplicación con el siguiente comando:

```bash
python main.py
```

---

## Uso desde la CLI

Una vez iniciado el programa, sigue las instrucciones mostradas en la terminal para descargar o convertir música.

Ejemplo de uso:

```bash
Pega la URL del video o playlist:
https://youtube.com/watch?v=example
```