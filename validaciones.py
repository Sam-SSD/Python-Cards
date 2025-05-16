from urllib.parse import urlparse
import logging

logger = logging.getLogger(__name__)

def es_entero_entre(valor, min_v, max_v):
    try:
        return min_v <= int(valor) <= max_v
    except (ValueError, TypeError):
        return False

def es_url_valida(url: str) -> bool:
    try:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])
    except:
        return False

def validar_datos(datos: dict) -> bool:
    obligatorios = ['nombre', 'apellido', 'profesion', 'edad']
    for campo in obligatorios:
        if not datos.get(campo):
            logger.warning(f"Campo obligatorio faltante: {campo}")
            return False

    if not es_entero_entre(datos['edad'], 0, 150):
        logger.warning(f"Edad inválida: {datos['edad']}")
        return False

    if not es_url_valida(datos.get('foto_url', '')):
        logger.warning(f"URL de foto inválida: {datos.get('foto_url', '')}")
        return False

    for i in range(1, 4):
        habilidad = datos.get(f"habilidad{i}")
        porcentaje = datos.get(f"porcentaje{i}")
        if not habilidad:
            logger.warning(f"Habilidad {i} faltante")
            return False
        if not es_entero_entre(porcentaje, 0, 100):
            logger.warning(f"Porcentaje {i} inválido: {porcentaje}")
            return False

    return True
