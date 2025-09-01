from config.Google.google_cloud import docs_service, drive_service
from fastapi import HTTPException
from services.LuminisIA.createDoc import generar_impresion_clinica

ROOT_FOLDER_ID = "1RWq3RMGJyckA1T0ggq8dMH4k_sFdJDdv"

def createDocIaFirstTime(doc_number: int, inscripcion_data: dict):
    title = f"{doc_number}"
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc.get("documentId")

    try:
        drive_service.files().update(
            fileId=doc_id,
            addParents=ROOT_FOLDER_ID,
            removeParents="root",
            supportsAllDrives=True,
            fields="id, parents"
        ).execute()

        impresion_clinica = generar_impresion_clinica(inscripcion_data)

        requests = [{"insertText": {"location": {"index": 1}, "text": impresion_clinica}}]
        docs_service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()

        return {"message": "Documento creado y actualizado con IA", "title": title, "documentId": doc_id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"No se pudo crear/actualizar el documento: {str(e)}")
