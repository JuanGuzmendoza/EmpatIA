# EmpatIA

## Descripción

EmpatIA es un proyecto de [breve descripción del proyecto]. Este proyecto incluye una API desarrollada con FastAPI y componentes de IA para [describir la funcionalidad principal].

Este repositorio tiene dos carpetas principales:

*   **Api/**: Contiene la API desarrollada con FastAPI.
*   **proyecto/**: Contiene la lógica y componentes generales del proyecto.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

*   Python 3.12 o superior
*   pip (gestor de paquetes de Python)

## Instrucciones de uso

### 1️⃣ Crear un entorno virtual

Se recomienda crear el entorno virtual en la raíz del proyecto, donde se encuentra este README.

### Crear un entorno virtual

codeBash

`   python3 -m venv venv   `

*   **Activar el entorno virtual:**
    
    *   codeBashsource venv/bin/activate
        
    *   codePowershellvenv\\Scripts\\activate
        

### 2️⃣ Instalar dependencias

Con el entorno virtual activado, ve a la carpeta Api/ y ejecuta:

codeBash

`   cd Api  pip install -r requirements.txt   `

### 3️⃣ Levantar el servidor

Dentro de la carpeta Api/, ejecuta uvicorn para iniciar la API:

*   codeBashuvicorn main:app --reload --host 0.0.0.0 --port 8000

    

Después de esto, tu API debería estar corriendo en: http://127.0.0.1:8000