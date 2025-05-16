import json
from pathlib import Path

class PerfilManager:
    FILE_PATH = Path(__file__).parent / "perfiles.json"

    @staticmethod
    def guardar_perfil(perfil_id, datos):
        perfiles = PerfilManager.cargar_perfiles()
        perfiles[perfil_id] = datos
        with open(PerfilManager.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(perfiles, f, indent=2)

    @staticmethod
    def cargar_perfiles():
        if not PerfilManager.FILE_PATH.exists():
            return {}
        with open(PerfilManager.FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def eliminar_perfil(perfil_id):
        perfiles = PerfilManager.cargar_perfiles()
        if perfil_id in perfiles:
            del perfiles[perfil_id]
            with open(PerfilManager.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(perfiles, f, indent=2)
            return True
        return False
