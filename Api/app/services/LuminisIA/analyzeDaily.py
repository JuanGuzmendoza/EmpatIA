import base64
from google import genai
from google.genai import types
import json

# ---------------------------
# Prompt para análisis JSON
# ---------------------------
PROMPT_JSON = """
You are Lumis, an assistant giving positive and easy-to-understand feedback.
Analyze the Daily Survey responses and generate a summary in JSON with 3 sections.
The language must be clear, friendly, motivating, and brief (max 2-3 sentences per item).
Do NOT use technical words like "ideation", "mild symptoms", or clinical diagnoses.
Talk about wellbeing, habits, emotions, and simple advice.

{
  "recommendations": [
    "Practical recommendation that is easy to apply today.",
    "Another brief and positive recommendation.",
    "Third motivating recommendation."
  ],
  "tip_of_the_day": "A very short paragraph with a positive and motivating tip (max 2 sentences).",
  "insights": [
    { "title": "Your Progress", "description": "Brief text about a positive improvement." },
    { "title": "What Stands Out", "description": "Short text about an emotional pattern or state." },
    { "title": "Advice", "description": "Simple and motivating recommendation." }
  ]
}

⚠ Strict rules:
1. Return ONLY a valid JSON.
2. Do not add explanations or text outside the JSON.
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
