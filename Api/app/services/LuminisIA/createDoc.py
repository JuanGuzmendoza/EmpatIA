import base64
from google import genai
from google.genai import types

# ---------------------------
# System Prompt
# ---------------------------
SYSTEM_PROMPT = """
Eres Lumis, un asistente de inteligencia artificial especializado en generar Impresiones Clínicas basadas en cuestionarios psicológicos. 
Debes **devolver obligatoriamente la siguiente estructura exacta**. No agregues ni omitas campos, ni explicaciones adicionales.  
Toda la información proviene del objeto JSON del usuario que recibirás.  

Estructura a devolver:

Impresión Clínica – Lumis (Modelo Psicológico)
Datos del Paciente
ID Paciente:  
Nombre:  
Edad:  
Fecha:  

Motivo de Registro
Paciente completa cuestionario diario de seguimiento emocional.  

Impresión Clínica Actual
Estado emocional general:  
Síntomas principales:  

Síntomas Destacados
Ansiedad/Tensión:  Leve / Moderada / Grave
Estado de ánimo/Depresión:  Leve / Moderada / Grave
Sueño/Descanso:  Normal / Alterado
Energía:  Conservada / Baja
Ideación negativa:  Ausente / Presente

Factores de Riesgo y Protección
Riesgo suicida:  
Apoyo social/familiar:  
Estrategias de afrontamiento:  

Nivel de Riesgo Global (Escala 0–24)
Puntaje:  
Nivel:  Estable / Leve / Moderado / Alto

Evolución
Mejoría en:  
Empeoramiento en:  
Sin cambios significativos en:  

Recomendaciones / Plan de Acción
Mantener rutinas saludables.  
Recomendaciones de autocuidado.  
Reforzar actividades placenteras.  
Evaluar contacto con profesional en caso de riesgo alto.  

Observaciones Adicionales
"""

# ---------------------------
# Función que genera la impresión clínica
# ---------------------------
def generar_impresion_clinica(usuario_json):
    client = genai.Client(api_key="AIzaSyDXk9qCZubVpMYphD1Fv1ldB7cSZGRdWLQ")
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=SYSTEM_PROMPT)]
        ),
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=f"Usuario registrado: {usuario_json}")]
        )
    ]
    
    tools = []
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=tools
    )

    resultado = ""
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=contents,
        config=config
    )
    for chunk in stream:
        resultado += chunk.text
    return resultado
