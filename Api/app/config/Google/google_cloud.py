from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Rutas y permisos
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'service_count.json')
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents'
]

# Autenticación
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# ID de la carpeta compartida (tu carpeta)
FOLDER_ID = "18hpXEsXWTR7BkWTOXxyDHjMNheyA6KA"

# Crear servicio de Drive y Docs
drive_service = build('drive', 'v3', credentials=credentials)
docs_service = build('docs', 'v1', credentials=credentials)

# 1. Crear archivo Google Docs dentro de la carpeta compartida
file_metadata = {
    'name': 'Hola Mundo',
    'mimeType': 'application/vnd.google-apps.document',
    'parents': [FOLDER_ID]
}

file = drive_service.files().create(body=file_metadata, fields='id, webViewLink').execute()
document_id = file.get('id')

# 2. Insertar contenido en el documento
requests = [
    {
        'insertText': {
            'location': {
                'index': 1,
            },
            'text': 'Qué mrd tan fácil'
        }
    }
]

docs_service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

# 3. Mostrar URL del documento
print("✅ Documento creado exitosamente.")
print(f"🔗 Link al documento: {file.get('webViewLink')}")
