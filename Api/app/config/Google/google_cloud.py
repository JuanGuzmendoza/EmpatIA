from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# ---------------- Credenciales ----------------
CLIENT_ID = "555554215317-dq8qrikftndl1ho2cm2r6i8cld22qpca.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//04OeAPQNBemsZCgYIARAAGAQSNwF-L9Irh03GfDEQbgcE0kttR7Glr3OjAaxawh9uutJCMePtC39KLNYrKRYvu_fbiMt7kqSm7o0"
ROOT_FOLDER_ID = "1RWq3RMGJyckA1T0ggq8dMH4k_sFdJDdv"

creds = Credentials(
    None,
    refresh_token=REFRESH_TOKEN,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    token_uri="https://oauth2.googleapis.com/token"
)

drive_service = build("drive", "v3", credentials=creds)
docs_service = build("docs", "v1", credentials=creds)

# ---------------- Crear carpeta ----------------
folder_name = "CRUD_Carpeta"
results = drive_service.files().list(
    q=f"'{ROOT_FOLDER_ID}' in parents and name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",
    fields="files(id, name)"
).execute()
files = results.get("files", [])
if files:
    folder_id = files[0]["id"]
    print(f"[INFO] Carpeta ya existe: {folder_name} (ID: {folder_id})")
else:
    folder_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [ROOT_FOLDER_ID]
    }
    folder = drive_service.files().create(body=folder_metadata, fields="id").execute()
    folder_id = folder.get("id")
    print(f"[CREADO] Carpeta: {folder_name} (ID: {folder_id})")

# ---------------- Crear documento ----------------
doc_title = "CRUD_Documento"
doc = docs_service.documents().create(body={"title": doc_title}).execute()
doc_id = doc["documentId"]
# Mover a la carpeta
drive_service.files().update(
    fileId=doc_id,
    addParents=folder_id,
    removeParents="root",
    fields="id, parents"
).execute()
# Insertar texto inicial
requests = [{"insertText": {"location": {"index": 1}, "text": "Contenido inicial desde Python CRUD"}}]
docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
print(f"[CREADO] Documento: {doc_title} (ID: {doc_id}) dentro de carpeta {folder_name}")

# ---------------- Leer contenido de la carpeta ----------------
print("\n[INFO] Archivos dentro de la carpeta:")
items = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name, mimeType)").execute()
for item in items.get("files", []):
    print(f"- {item['name']} ({item['mimeType']})")

# ---------------- Actualizar documento y carpeta ----------------
# Cambiar nombre de carpeta
drive_service.files().update(fileId=folder_id, body={"name": "CRUD_Carpeta_Renombrada"}).execute()
print(f"\n[ACTUALIZADO] Carpeta renombrada a CRUD_Carpeta_Renombrada")
# Agregar más texto al documento
more_text = "\nTexto agregado después de crear el documento."
docs_service.documents().batchUpdate(documentId=doc_id, body={"requests":[{"insertText":{"location":{"index":2}, "text":more_text}}]}).execute()
print(f"[ACTUALIZADO] Documento actualizado con más texto")

# ---------------- Eliminar documento y carpeta ----------------
# drive_service.files().delete(fileId=doc_id).execute()
# drive_service.files().delete(fileId=folder_id).execute()
# print("\n[ELIMINADO] Documento y carpeta eliminados")
