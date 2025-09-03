import base64
from google import genai
from google.genai import types
import json

# ---------------------------
# Prompt para análisis JSON
# ---------------------------
PROMPT_JSON = """
Eres Lumis, un asistente que da retroalimentación positiva y fácil de entender.
Analiza las respuestas del Daily Survey y genera un resumen en JSON con 3 secciones.
El lenguaje debe ser claro, cercano, motivador y breve (máx. 2-3 frases por ítem). 
No uses palabras técnicas como "ideación", "síntomas leves", ni diagnósticos clínicos.
Habla de bienestar, hábitos, emociones y consejos simples.

{
  "recommendations": [
    "Recomendación práctica y fácil de aplicar en el día.",
    "Otra recomendación breve y positiva.",
    "Tercera recomendación motivadora."
  ],
  "tip_of_the_day": "Un párrafo muy breve con un consejo positivo y motivador (máx. 2 frases).",
  "insights": [
    { "title": "Tu Progreso", "description": "Texto breve sobre un avance positivo." },
    { "title": "Lo que se Nota", "description": "Texto corto sobre un patrón o estado emocional." },
    { "title": "Consejo", "description": "Recomendación sencilla y motivadora." }
  ]
}

⚠ Reglas estrictas:
1. Devuelve SOLO un JSON válido.
2. No agregues explicaciones ni texto fuera del JSON.
"""


# ---------------------------
# Función que genera la impresión JSON
# ---------------------------
def generar_impresion_json(doc_content: str):
    if not doc_content:
        doc_content = ""  # 🔥 evita None

    client = genai.Client(api_key="AIzaSyDXk9qCZubVpMYphD1Fv1ldB7cSZGRdWLQ")

    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=PROMPT_JSON)]),
        types.Content(role="user", parts=[types.Part.from_text( 
            text=f"Texto a analizar (impresión del documento):\n{str(doc_content)}"
        )])
    ]

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=[]
    )

    resultado = ""
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=contents,
        config=config
    )
    for chunk in stream:
        if chunk.text:  # 👈 evita None
            resultado += chunk.text

    # 🔥 Limpieza por si el modelo devuelve bloque de código Markdown
    clean_result = resultado.strip()
    if clean_result.startswith("```"):
        clean_result = clean_result.strip("`").strip()
        if clean_result.lower().startswith("json"):
            clean_result = clean_result[4:].strip()

    # 🔥 Validar JSON
    try:
        parsed = json.loads(clean_result)
    except Exception:
        raise ValueError(f"El modelo no devolvió JSON válido: {resultado}")

    return parsed  # 👈 devuelve dict listo para tu API
