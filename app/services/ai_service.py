from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() # Cargando variables de entorno

OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPEN_AI_KEY)

def generate_summary(session_notes: str):
    """
    Genera un resumen inteligente de una sesión de estudio utilizando OpenAI.

    Args:
        session_notes (str): Notas o descripción de la sesión.

    Returns:
        str: Resumen generado por la IA.
    """
    system_prompt = """
    Eres un asistente de estudio inteligente. Tu tarea es tomar la descripción 
    de una sesión de estudio y generar un resumen claro, conciso y organizado. 
    Tu resumen debe incluir:
    1. Temas principales abordados
    2. Conceptos clave aprendidos
    3. Posibles errores o dudas del estudiante
    4. Recomendaciones para reforzar o continuar en la siguiente sesión
    """
    
    user_prompt = f"""
    Aquí está la descripción de mi sesión de estudio:
    "{session_notes}"
    Genera un resumen siguiendo las instrucciones del sistema.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content