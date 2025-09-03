from fastapi import APIRouter, HTTPException , Body 
from googleapiclient.errors import HttpError
from config.Google.google_cloud import docs_service, drive_service
from services.LuminisIA.dailySurvey import generar_impresion_clinica
from services.LuminisIA.analyzeDaily import generar_impresion_json
google_docs = APIRouter()

ROOT_FOLDER_ID = "1RWq3RMGJyckA1T0ggq8dMH4k_sFdJDdv"

# ---------------- Leer contenido de un documento ----------------
@google_docs.post(
    "/docs/read-daily/{doc_id}", 
    tags=["GoogleDocs"], 
    description="Lee un Google Doc, genera una impresión clínica con el Daily Survey y reemplaza el contenido del documento"
)
def read_doc_and_generate_daily(doc_id: str, usuario_json: dict = Body(...)):
    try:
        # --- Leer Google Doc ---
        doc = docs_service.documents().get(documentId=doc_id).execute()
        content_list = []
        for el in doc['body']['content']:
            if 'paragraph' in el:
                for e in el['paragraph']['elements']:
                    if 'textRun' in e:
                        content_list.append(e['textRun']['content'])
        doc_content = "".join(content_list)

        # --- Generar nueva impresión clínica ---
        impresion = generar_impresion_clinica(usuario_json, doc_content)

        # --- Reemplazar el contenido del documento ---
        # 1. Borrar todo lo viejo
        end_index = doc.get("body").get("content")[-1]["endIndex"]

        requests = [
            {
                "deleteContentRange": {
                    "range": {
                        "startIndex": 1,
                        "endIndex": end_index - 1   # 👈 borrar todo menos el último marcador
                    }
                }
            },
            {
                "insertText": {
                    "location": {"index": 1},
                    "text": impresion
                }
            }
        ]

        docs_service.documents().batchUpdate(
            documentId=doc_id, body={"requests": requests}
        ).execute()

        return {
            "documentId": doc_id,
            "impresion_clinica": impresion,
            "message": "✅ Documento actualizado con la nueva impresión clínica"
        }

    except HttpError as e:
        raise HTTPException(status_code=404, detail=f"Error al leer el documento: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


# ---------------- Nueva función: Solo analiza y devuelve JSON ----------------
@google_docs.post(
    "/docs/analyze-daily/{doc_id}",
    tags=["GoogleDocs"],
    description="Lee un Google Doc, analiza su contenido con Lumis y devuelve recomendaciones en formato JSON"
)
def analyze_doc_and_generate_json(doc_id: str):
    try:
        # --- Leer Google Doc ---
        doc = docs_service.documents().get(documentId=doc_id).execute()
        content_list = []
        for el in doc['body']['content']:
            if 'paragraph' in el:
                for e in el['paragraph']['elements']:
                    if 'textRun' in e:
                        content_list.append(e['textRun']['content'])
        doc_content = "".join(content_list)

        # --- Llamar a Lumis IA (usa PROMPT_JSON dentro de la función) ---
        impresion_json = generar_impresion_json(doc_content)

        return {
            "documentId": doc_id,
            "impresion_json": impresion_json,
            "message": "✅ Análisis completado y devuelto en formato JSON"
        }

    except HttpError as e:
        raise HTTPException(status_code=404, detail=f"Error al leer el documento: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
