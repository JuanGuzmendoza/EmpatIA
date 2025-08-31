from fastapi import APIRouter, HTTPException
from config.Google.google_cloud import docs_service, drive_service

google_docs = APIRouter()

ROOT_FOLDER_ID = "1RWq3RMGJyckA1T0ggq8dMH4k_sFdJDdv"

# ---------------- Crear documento ----------------
@google_docs.post("/docs/create/{doc_number}", tags=["GoogleDocs"])
def create_doc(doc_number: int):
    title = f"{doc_number}"

    # 1️⃣ Crear documento en Google Docs
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]

    try:
        # 2️⃣ Mover documento a la carpeta deseada
        drive_service.files().update(
            fileId=doc_id,
            addParents=ROOT_FOLDER_ID,
            removeParents="root",
            supportsAllDrives=True,
            fields="id, parents"
        ).execute()

        return {"message": "Documento creado en la carpeta", "title": title, "documentId": doc_id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se pudo mover el documento: {str(e)}")


# ---------------- Leer contenido de un documento ----------------
@google_docs.get("/docs/read/{doc_id}", tags=["GoogleDocs"])
def read_doc(doc_id: str):
    try:
        doc = docs_service.documents().get(documentId=doc_id).execute()
        content_list = []
        for el in doc['body']['content']:
            if 'paragraph' in el:
                for e in el['paragraph']['elements']:
                    if 'textRun' in e:
                        content_list.append(e['textRun']['content'])
        content_str = "".join(content_list)
        return {"documentId": doc_id, "content": content_str}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Documento no encontrado: {str(e)}")


# ---------------- Actualizar contenido de un documento ----------------
@google_docs.put("/docs/update/{doc_id}", tags=["GoogleDocs"])
def update_doc(doc_id: str, new_content: str):
    try:
        requests = [
            {"deleteContentRange": {"range": {"startIndex": 1, "endIndex": 1000000}}},  # Borra contenido existente
            {"insertText": {"location": {"index": 1}, "text": new_content}}
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
        return {"message": "Documento actualizado", "documentId": doc_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se pudo actualizar: {str(e)}")
