# perfil_manager.py
import json
from pathlib import Path

class PerfilManager:
    FILE_PATH = Path(__file__).parent.resolve() / "perfiles.json"

    @classmethod
    def cargar_perfiles(cls) -> dict:
        if cls.FILE_PATH.exists():
            with open(cls.FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    @classmethod
    def guardar_perfil(cls, perfil_id: str, datos: dict) -> None:
        perfiles = cls.cargar_perfiles()
        perfiles[perfil_id] = datos
        with open(cls.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(perfiles, f, indent=2)
