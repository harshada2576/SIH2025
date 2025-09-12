from fastapi import APIRouter, Query
from deep_translator import GoogleTranslator

router = APIRouter()

@router.get("/translate")
def translate_text(text: str = Query(...), target_lang: str = "hi"):
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return {
            "original": text,
            "translated": translated,
            "target_lang": target_lang
        }
    except Exception as e:
        return {"error": str(e)}

