import json
from pathlib import Path

# Ruta al archivo de perfiles
PERFILES_PATH = Path(__file__).parent / "perfiles.json"

def cargar_perfiles():
    """Carga y devuelve todos los perfiles desde el archivo JSON."""
    if PERFILES_PATH.exists():
        try:
            with open(PERFILES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def guardar_perfil(perfil_id, datos):
    """Guarda un perfil individual dentro del archivo JSON."""
    perfiles = cargar_perfiles()
    perfiles[perfil_id] = datos
    with open(PERFILES_PATH, "w", encoding="utf-8") as f:
        json.dump(perfiles, f, indent=2)
