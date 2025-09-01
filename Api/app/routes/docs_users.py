from fastapi import APIRouter, HTTPException
from config.Google.google_cloud import docs_service, drive_service
google_docs = APIRouter()

ROOT_FOLDER_ID = "1RWq3RMGJyckA1T0ggq8dMH4k_sFdJDdv"

# ---------------- Leer contenido de un documento ----------------
@google_docs.get("/docs/read/{doc_id}", tags=["GoogleDocs"] , description="Read content of a Google Doc by its ID")
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





