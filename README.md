# EmpatIA

## Descripción
EmpatIA es un proyecto de [breve descripción del proyecto]. En esta sección, se incluyen los componentes de la API y otros aspectos del proyecto.

Este repositorio tiene dos carpetas principales:

- **`api/`**: Contiene la API que está siendo desarrollada con FastAPI.
- **`proyecto/`**: Contiene la lógica y componentes generales del proyecto.

## Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.12 o superior
- pip (gestor de paquetes de Python)

## Instrucciones de uso

### Instalación de dependencias

#### Paso 1: Crear un entorno virtual

Para trabajar con el proyecto, es **recomendado usar un entorno virtual** para evitar conflictos con otras dependencias del sistema. Para crear uno:

1. Abre una terminal en la carpeta del proyecto.
2. Crea un entorno virtual:

    ```bash
    python3 -m venv venv
    ```

3. Activa el entorno virtual:
   
   - En **Ubuntu/macOS**:

     ```bash
     source venv/bin/activate
     ```

   - En **Windows**:

     ```bash
     venv\Scripts\activate
     ```

#### Paso 2: Instalar las dependencias

Con el entorno virtual activado, instala todas las dependencias necesarias para el proyecto:

```bash
pip install -r requirements.txt
