# Organizador de archivos

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/UI-Tkinter-FFD43B)](https://docs.python.org/3/library/tkinter.html)
[![MIT](https://img.shields.io/badge/Licencia-MIT-green)](LICENSE)

[Español](#español) · [English](#english)

---

## Español

### Índice

- [Descripción](#descripción)
- [Características](#características)
- [Cómo funciona](#cómo-funciona)
- [Categorías](#categorías)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Uso](#uso)
- [Licencia](#licencia)

### Descripción

Aplicación de escritorio en **Python** con interfaz **Tkinter** que ordena una carpeta llena de archivos en subcarpetas por tipo: imágenes, documentos, audio, vídeo y demás. Pensada para dejar limpia la carpeta de descargas en un par de clics, sin renombrar nada.

### Características

- **Interfaz sencilla**: eliges la carpeta, previsualizas y ejecutas.
- **Clasificación por categorías** definidas en `categories.py`.
- **Vista previa** del movimiento antes de tocar ningún archivo.
- **Copia de seguridad opcional** antes de mover nada.
- **Archivos ocultos**: incluir o excluir según el caso.
- **Conflictos de nombre**: si ya existe un archivo con ese nombre, añade un sufijo numerado en lugar de sobrescribirlo.
- **Barra de progreso y resumen** final con lo que se movió y lo que se omitió.

### Cómo funciona

1. Seleccionas la carpeta de origen.
2. La app recorre solo el primer nivel (no entra en subcarpetas) y agrupa por extensión.
3. Con **Vista previa** ves qué irá a dónde sin mover nada.
4. Si activas la copia de seguridad, se crea una carpeta aparte con los archivos antes de moverlos.
5. Al ejecutar, cada archivo se mueve a `categoria/` y se registra el resultado.

### Categorías

Las categorías y sus extensiones viven en `categories.py`, en un diccionario fácil de editar:

```python
CATEGORIAS = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    # …
}
```

Añadir una categoría es añadir una clave y su lista de extensiones; no hay que tocar el resto del código.

### Estructura del proyecto

```text
Organizador_archivos/
├── main.py          # Punto de entrada
├── gui.py           # Interfaz Tkinter
├── organizer.py     # Lógica de clasificación y movimiento
├── categories.py    # Categorías y extensiones
├── utils.py         # Utilidades (nombres, copias, formato)
├── LICENSE
└── README.md
```

### Requisitos

- **Python 3.8 o superior**.
- **Tkinter**, incluido en la instalación estándar de Python (en algunas distribuciones Linux hay que instalar `python3-tk`).

No hay dependencias externas que instalar.

### Uso

```bash
git clone https://github.com/alberto2005-coder/Organizador_archivos.git
cd Organizador_archivos
python main.py
```

1. Pulsa **Seleccionar carpeta** y elige el directorio.
2. Revisa la vista previa y ajusta las opciones (copia de seguridad, archivos ocultos).
3. Pulsa **Organizar** y espera al resumen.

> [!WARNING]
> La operación **mueve** archivos. Prueba primero con una carpeta de ejemplo o activa la copia de seguridad; deshacer no está automatizado.

### Licencia

**MIT** — consulta [LICENSE](LICENSE).

---

## English

### Table of contents

- [Overview](#overview)
- [Features](#features)
- [How it works](#how-it-works)
- [Categories](#categories)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

### Overview

A **Python** desktop app with a **Tkinter** interface that sorts a messy folder into per-type subfolders: images, documents, audio, video and more. It is meant to clean the downloads folder in a couple of clicks without renaming anything.

### Features

- **Simple UI**: pick a folder, preview, run.
- **Category-based sorting** defined in `categories.py`.
- **Preview** of the moves before touching any file.
- **Optional backup** before moving anything.
- **Hidden files**: include or skip them as needed.
- **Name conflicts**: if a file with that name exists, a numbered suffix is added instead of overwriting.
- **Progress bar and final summary** listing what moved and what was skipped.

### How it works

1. Select the source folder.
2. The app scans only the top level (no recursion) and groups by extension.
3. **Preview** shows what will go where without moving anything.
4. With the backup option on, files are copied to a separate folder before moving.
5. On run, each file moves to `category/` and the result is logged.

### Categories

Categories and their extensions live in `categories.py`, in an easy-to-edit dictionary:

```python
CATEGORIAS = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    # …
}
```

Adding a category means adding a key and its extension list; nothing else changes.

### Project structure

```text
Organizador_archivos/
├── main.py          # Entry point
├── gui.py           # Tkinter interface
├── organizer.py     # Sorting and move logic
├── categories.py    # Categories and extensions
├── utils.py         # Helpers (names, backups, formatting)
├── LICENSE
└── README.md
```

### Requirements

- **Python 3.8 or later**.
- **Tkinter**, bundled with standard Python (some Linux distributions need `python3-tk`).

No third-party packages to install.

### Usage

```bash
git clone https://github.com/alberto2005-coder/Organizador_archivos.git
cd Organizador_archivos
python main.py
```

1. Click **Select folder** and choose the directory.
2. Review the preview and adjust options (backup, hidden files).
3. Click **Organize** and read the summary.

> [!WARNING]
> The operation **moves** files. Try it on a sample folder first or enable the backup; undo is not automated.

### License

**MIT** — see [LICENSE](LICENSE).
