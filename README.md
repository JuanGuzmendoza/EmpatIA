# EmpatIA

## Descripción

EmpatIA es un proyecto que integra una API desarrollada con FastAPI y componentes de inteligencia artificial para el análisis y gestión de documentos y encuestas. El objetivo principal es facilitar la interacción y procesamiento de datos mediante IA.

## Estructura del repositorio

- **Api/**: Contiene la API principal desarrollada con FastAPI, incluyendo rutas, servicios y configuración.
- **proyecto/**: Incluye la lógica y componentes generales del proyecto fuera de la API.
- **docs/**: Documentación y archivos relacionados con la base de datos.

## Requisitos

- **Python**: 3.12
- **pip**: Gestor de paquetes de Python

## Instrucciones de uso

### 1️⃣ Crear un entorno virtual

Ubícate en la raíz del proyecto (donde está este README).

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Ubuntu/Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Instalar dependencias

Con el entorno virtual activado, entra a la carpeta `Api` y ejecuta:

```bash
cd Api
pip install -r requirements.txt
```

### 3️⃣ Levantar el servidor

Dentro de la carpeta `Api`, ejecuta el siguiente comando para iniciar la API con Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

Si tienes dudas o problemas, revisa la documentación en la carpeta `docs/` o contacta al equipo de desarrollo.