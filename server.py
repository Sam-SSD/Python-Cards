from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as up
import html
from pathlib import Path
from typing import Dict
import logging
import json
import uuid
from validaciones import validar_datos

# Configuración básica
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from perfil_manager import PerfilManager
from templates import HTMLTemplates

class ServerConfig:
    PORT = 8000
    ROOT = Path(__file__).parent.resolve()
    DEFAULT_VALUES = {
        "nombre": "Anónim@", "apellido": "", "edad": "",
        "profesion": "", "habilidad1": "", "habilidad2": "", "habilidad3": "",
        "porcentaje1": "70", "porcentaje2": "80", "porcentaje3": "90",
        "foto_url": "", "red_social1": "", "red_social2": "",
        "color_fondo": "#ffffff", "color_texto": "#000000",
        "estilo_fuente": "Arial", "plantilla": "1"
    }

SHARE_LINK_HTML = (
    '<p><a href="/">← Crear otro perfil</a> | '
    '<a href="/perfiles">Ver todos los perfiles</a> | '
    '<button onclick="navigator.clipboard.writeText(window.location.href);">Copiar enlace</button></p>'
)

PLANTILLAS = {
    "1": HTMLTemplates.CARD_TEMPLATE_1,
    "2": HTMLTemplates.CARD_TEMPLATE_2,
    "3": HTMLTemplates.CARD_TEMPLATE_3
}

class TarjetaHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        if path.startswith("/static/"):
            return str(ServerConfig.ROOT / "static" / path.split("/")[-1])
        return super().translate_path(path)

    def do_GET(self) -> None:
        try:
            parsed = up.urlparse(self.path)
            logger.info(f"Petición recibida: {self.path}")

            if parsed.path == "/":
                self._send_html(HTMLTemplates.INDEX_HTML)
            elif parsed.path == "/crear":
                self._send_html(HTMLTemplates.FORM_HTML)
            elif parsed.path == "/tarjeta":
                self._handle_tarjeta(parsed)
            elif parsed.path == "/perfiles":
                self._handle_perfiles_list()
            elif parsed.path.startswith("/perfil/"):
                self._handle_perfil_individual(parsed.path.split("/")[-1])
            elif parsed.path.startswith("/static/"):
                super().do_GET()
            else:
                self._send_error(404, "Ruta no encontrada")
        except Exception as e:
            logger.error(f"Error: {e}")
            self._send_error(500, "Error interno del servidor")

    def _handle_tarjeta(self, parsed) -> None:
        datos = self._parse_query_params(parsed.query)
        if not validar_datos(datos):
            self._send_error(400, "Datos inválidos")
            return

        template = PLANTILLAS.get(datos['plantilla'], HTMLTemplates.CARD_TEMPLATE_1)
        perfil_id = str(uuid.uuid4())
        PerfilManager.guardar_perfil(perfil_id, datos)

        html_content = template.format(**datos).replace(
            '<p><a href="/">← Crear otro perfil</a></p>',
            SHARE_LINK_HTML.replace("window.location.href", f"window.location.origin + '/perfil/{perfil_id}'")
        )
        self._send_html(html_content)

    def _handle_perfiles_list(self):
        try:
            perfiles = PerfilManager.cargar_perfiles()
            perfiles_items = "".join(
                HTMLTemplates.PERFIL_ITEM_HTML.format(
                    id=pid,
                    nombre=datos.get('nombre', 'Sin nombre'),
                    apellido=datos.get('apellido', ''),
                    profesion=datos.get('profesion', ''),
                    foto_url=datos.get('foto_url', '')
                ) for pid, datos in perfiles.items()
            )
            self._send_html(HTMLTemplates.PERFILES_LIST_HTML.format(
                perfiles_items=perfiles_items or "<p>No hay perfiles guardados</p>"
            ))
        except Exception as e:
            logger.error(f"Error al mostrar perfiles: {e}")
            self._send_error(500, "Error al cargar perfiles")

    def _handle_perfil_individual(self, perfil_id):
        try:
            perfiles = PerfilManager.cargar_perfiles()
            if perfil_id not in perfiles:
                self._send_error(404, "Perfil no encontrado")
                return

            datos = perfiles[perfil_id]
            plantilla = PLANTILLAS.get(datos.get('plantilla', '1'), HTMLTemplates.CARD_TEMPLATE_1)
            html_content = plantilla.format(**datos).replace(
                '<p><a href="/">← Crear otro perfil</a></p>',
                SHARE_LINK_HTML
            )
            self._send_html(html_content)
        except Exception as e:
            logger.error(f"Error al mostrar perfil: {e}")
            self._send_error(500, "Error al cargar el perfil")

    def _parse_query_params(self, query: str) -> Dict[str, str]:
        params = up.parse_qs(query)
        return {
            key: html.escape(params.get(key, [default])[0])
            for key, default in ServerConfig.DEFAULT_VALUES.items()
        }

    def _send_html(self, contenido: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(contenido.encode("utf-8"))

    def _send_error(self, code: int, message: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"<h1>Error {code}</h1><p>{message}</p>".encode("utf-8"))

    @staticmethod
    def _check_static_files():
        return (ServerConfig.ROOT / "static" / "style.css").exists()


def run_server() -> None:
    try:
        if not TarjetaHandler._check_static_files():
            logger.error("Falta el archivo CSS en static/")
            return

        server_address = ("", ServerConfig.PORT)
        with HTTPServer(server_address, TarjetaHandler) as httpd:
            logger.info(f"🚀 Servidor iniciado en http://localhost:{ServerConfig.PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n⏹️ Servidor detenido manualmente")
    except Exception as e:
        logger.error(f"Error fatal del servidor: {e}")


if __name__ == "__main__":
    run_server()
