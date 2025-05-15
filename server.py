"""
Servidor mínimo que sirve:
  • GET / → formulario HTML
  • GET /tarjeta?... → página generada con los datos del usuario
  • Archivos dentro de /static (CSS, imágenes…)
"""

from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as up
import html
from pathlib import Path
from textwrap import dedent
from typing import Dict
import logging
import json
import uuid

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Configuración del servidor
class ServerConfig:
    PORT = 8000
    ROOT = Path(__file__).parent.resolve()
    DEFAULT_VALUES = {
        "nombre": "Anónim@",
        "apellido": "",
        "edad": "",
        "profesion": "",
        "habilidad1": "",
        "habilidad2": "",
        "habilidad3": "",
        "porcentaje1": "70",
        "porcentaje2": "80",
        "porcentaje3": "90",
        "foto_url": "",
        "red_social1": "",
        "red_social2": "",
        "color_fondo": "#ffffff",
        "color_texto": "#000000",
        "estilo_fuente": "Arial",
        "plantilla": "1"
    }


class HTMLTemplates:
    INDEX_HTML = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Generador de Perfiles - Inicio</title>
            <link rel="stylesheet" href="/static/style.css">
            <style>
                .main-menu {
                    max-width: 800px;
                    margin: 50px auto;
                    text-align: center;
                    padding: 2rem;
                }
                .menu-options {
                    display: flex;
                    justify-content: center;
                    gap: 2rem;
                    margin-top: 2rem;
                }
                .menu-option {
                    background: #007bff;
                    color: white;
                    padding: 1.5rem 3rem;
                    border-radius: 10px;
                    text-decoration: none;
                    transition: background-color 0.3s;
                }
                .menu-option:hover {
                    background: #0056b3;
                }
                h1 {
                    color: #333;
                    margin-bottom: 1.5rem;
                }
                .description {
                    color: #666;
                    margin-bottom: 2rem;
                }
            </style>
        </head>
        <body>
            <div class="main-menu">
                <h1>Bienvenido al Generador de Perfiles</h1>
                <p class="description">¿Qué deseas hacer?</p>
                <div class="menu-options">
                    <a href="/crear" class="menu-option">Crear Nuevo Perfil</a>
                    <a href="/perfiles" class="menu-option">Ver Perfiles Guardados</a>
                </div>
            </div>
        </body>
        </html>
    """)
    
    FORM_HTML = dedent("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Genera tu perfil</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Generador de Perfiles</h1>
            <form action="/tarjeta" method="get">
                <div class="form-group">
                    <label for="nombre">Nombre:</label>
                    <input id="nombre" name="nombre" required>
                </div>
                <div class="form-group">
                    <label for="apellido">Apellido:</label>
                    <input id="apellido" name="apellido" required>      
                </div>
                <div class="form-group">
                    <label for="edad">Edad:</label>
                    <input id="edad" name="edad" type="number" required>
                </div>
                <div class="form-group">
                    <label for="profesion">Profesión:</label>
                    <input id="profesion" name="profesion" required>
                </div>
                <div class="form-group">
                    <label>Habilidades:</label>
                    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
                        <input name="habilidad1" placeholder="Habilidad 1" required style="flex: 2;">
                        <input name="porcentaje1" type="number" min="0" max="100" placeholder="%" required style="flex: 1; width: 60px;">
                    </div>
                    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
                        <input name="habilidad2" placeholder="Habilidad 2" required style="flex: 2;">
                        <input name="porcentaje2" type="number" min="0" max="100" placeholder="%" required style="flex: 1; width: 60px;">
                    </div>
                    <div style="display: flex; gap: 10px;">
                        <input name="habilidad3" placeholder="Habilidad 3" required style="flex: 2;">
                        <input name="porcentaje3" type="number" min="0" max="100" placeholder="%" required style="flex: 1; width: 60px;">
                    </div>
                </div>
                <div class="form-group">
                    <label for="foto_url">URL de foto:</label>
                    <input id="foto_url" name="foto_url" type="url" required>
                </div>
                <div class="form-group">
                    <label>Redes Sociales:</label>
                    <div style="display: flex; gap: 10px; margin-bottom: 10px;">
                        <input name="red_social1" placeholder="Red Social 1" required style="flex: 2;">
                    </div>
                    <div style="display: flex; gap: 10px;">
                        <input name="red_social2" placeholder="Red Social 2" required style="flex: 2;">
                    </div>
                </div>
                <div class="form-group">
                    <label for="color_fondo">Color de fondo:</label>
                    <input id="color_fondo" name="color_fondo" type="color" value="#ffffff" required>
                </div>
                <div class="form-group">
                    <label for="color_texto">Color de texto:</label>
                    <input id="color_texto" name="color_texto" type="color" value="#000000" required>
                </div>
                <div class="form-group">
                    <label for="estilo_fuente">Estilo de fuente:</label>
                    <select id="estilo_fuente" name="estilo_fuente">
                        <option value="Arial">Arial</option>
                        <option value="Helvetica">Helvetica</option>
                        <option value="Times New Roman">Times New Roman</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="plantilla">Diseño de plantilla:</label>
                    <select id="plantilla" name="plantilla">
                        <option value="1">Plantilla 1</option>
                        <option value="2">Plantilla 2</option>
                        <option value="3">Plantilla 3</option>
                    </select>
                </div>
                <button type="submit">Crear Perfil</button>
            </form>
        </div>
    </body>
    </html>
    """)

    CARD_TEMPLATE_1 = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Perfil de {nombre}</title>
            <link rel="stylesheet" href="/static/style.css">
            <style>
                body {{ 
                    background-color: {color_fondo};
                    color: {color_texto};
                    font-family: {estilo_fuente}, sans-serif;
                }}
                .profile-card {{
                    max-width: 600px;
                    margin: 2rem auto;
                    padding: 2rem;
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                }}
                .profile-image {{
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    margin: 0 auto;
                }}
                .skill-bar {{
                    background: #f0f0f0;
                    height: 20px;
                    border-radius: 10px;
                    margin: 5px 0;
                }}
                .skill-progress {{
                    background: {color_texto};
                    height: 100%;
                    border-radius: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="profile-card">
                <img src="{foto_url}" alt="{nombre}" class="profile-image">
                <h1>{nombre} {apellido}</h1>
                <p>Edad: {edad} años</p>
                <p>Profesión: {profesion}</p>

                <h2>Habilidades</h2>
                <div class="skills">
                    <p>{habilidad1} - {porcentaje1}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje1}%"></div></div>
                    <p>{habilidad2} - {porcentaje2}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje2}%"></div></div>
                    <p>{habilidad3} - {porcentaje3}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje3}%"></div></div>
                </div>

                <h2>Redes Sociales</h2>
                <p><a href="{red_social1}">Red Social 1</a></p>
                <p><a href="{red_social2}">Red Social 2</a></p>

                <p><a href="/crear">← Crear otro perfil</a> | <a href="/">Volver al inicio</a></p>
            </div>
        </body>
        </html>
    """)

    CARD_TEMPLATE_2 = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Perfil de {nombre}</title>
            <link rel="stylesheet" href="/static/style.css">
            <style>
                body {{ 
                    background-color: {color_fondo};
                    color: {color_texto};
                    font-family: {estilo_fuente}, sans-serif;
                }}
                .profile-card {{
                    max-width: 600px;
                    margin: 2rem auto;
                    padding: 2rem;
                    background: #f8f9fa;
                    border-radius: 0;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}
                .profile-image {{
                    width: 180px;
                    height: 180px;
                    border-radius: 5px;
                    border: 5px solid {color_texto};
                }}
                .skill-bar {{
                    background: #e9ecef;
                    height: 15px;
                    border-radius: 0;
                    margin: 10px 0;
                    width: 100%;
                }}
                .skill-progress {{
                    background: linear-gradient(90deg, {color_texto}, #adb5bd);
                    height: 100%;
                }}
            </style>
        </head>
        <body>
            <div class="profile-card">
                <img src="{foto_url}" alt="{nombre}" class="profile-image">
                <h1 style="text-transform: uppercase;">{nombre} {apellido}</h1>
                <p><strong>Edad:</strong> {edad} años | <strong>Profesión:</strong> {profesion}</p>

                <h2>HABILIDADES</h2>
                <div class="skills" style="width: 100%;">
                    <p>{habilidad1} - {porcentaje1}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje1}%"></div></div>
                    <p>{habilidad2} - {porcentaje2}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje2}%"></div></div>
                    <p>{habilidad3} - {porcentaje3}%</p>
                    <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje3}%"></div></div>
                </div>

                <h2>CONTACTO</h2>
                <div style="display: flex; justify-content: space-around; width: 100%;">
                    <a href="{red_social1}" target="_blank">Red Social 1</a>
                    <a href="{red_social2}" target="_blank">Red Social 2</a>
                </div>

                <p style="margin-top: 30px;"><a href="/">← Crear otro perfil</a></p>
            </div>
        </body>
        </html>
    """)

    CARD_TEMPLATE_3 = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title>Perfil de {nombre}</title>
            <link rel="stylesheet" href="/static/style.css">
            <style>
                body {{ 
                    background-color: {color_fondo};
                    color: {color_texto};
                    font-family: {estilo_fuente}, sans-serif;
                }}
                .profile-card {{
                    max-width: 600px;
                    margin: 2rem auto;
                    padding: 0;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    box-shadow: 0 15px 30px rgba(0,0,0,0.15);
                }}
                .header {{
                    background: {color_texto};
                    color: white;
                    padding: 30px;
                    text-align: center;
                }}
                .profile-image {{
                    width: 120px;
                    height: 120px;
                    border-radius: 50%;
                    border: 4px solid white;
                    margin-top: -60px;
                    position: relative;
                    z-index: 1;
                }}
                .content {{
                    padding: 20px;
                    text-align: center;
                }}
                .skill-bar {{
                    background: #e9ecef;
                    height: 8px;
                    border-radius: 4px;
                    margin: 8px 0 20px;
                }}
                .skill-progress {{
                    background: {color_texto};
                    height: 100%;
                    border-radius: 4px;
                }}
                .social-links {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin: 20px 0;
                }}
                .social-links a {{
                    color: {color_texto};
                    text-decoration: none;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="profile-card">
                <div class="header">
                    <h1>{nombre} {apellido}</h1>
                    <p>{profesion}</p>
                </div>

                <div class="content">
                    <img src="{foto_url}" alt="{nombre}" class="profile-image">
                    <p>Edad: {edad} años</p>

                    <h3>Mis Habilidades</h3>
                    <div class="skills">
                        <p>{habilidad1} - {porcentaje1}%</p>
                        <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje1}%"></div></div>
                        <p>{habilidad2} - {porcentaje2}%</p>
                        <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje2}%"></div></div>
                        <p>{habilidad3} - {porcentaje3}%</p>
                        <div class="skill-bar"><div class="skill-progress" style="width: {porcentaje3}%"></div></div>
                    </div>

                    <div class="social-links">
                        <a href="{red_social1}" target="_blank">Red Social 1</a>
                        <a href="{red_social2}" target="_blank">Red Social 2</a>
                    </div>

                    <p><a href="/crear">← Crear otro perfil</a> | <a href="/">Volver al inicio</a></p>
                </div>
            </div>
        </body>
        </html>
    """)

    PERFILES_LIST_HTML = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Perfiles Guardados</title>
            <link rel="stylesheet" href="/static/style.css">
            <style>
                .perfiles-lista {{
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 2rem;
                }}
                .perfil-item {{
                    background: white;
                    padding: 1rem;
                    margin-bottom: 1rem;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    display: flex;
                    align-items: center;
                }}
                .perfil-item img {{
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    margin-right: 1rem;
                }}
                .perfil-item h3 {{
                    margin: 0;
                }}
                .perfil-actions {{
                    margin-left: auto;
                }}
            </style>
        </head>
        <body>
            <div class="perfiles-lista">
                <h1>Perfiles Guardados</h1>
                <a href="/crear" class="btn">Crear Nuevo Perfil</a> | <a href="/" class="btn">Volver al inicio</a>
                
                {perfiles_items}
                
            </div>
        </body>
        </html>
    """)

    PERFIL_ITEM_HTML = dedent("""
        <div class="perfil-item">
            <img src="{foto_url}" alt="{nombre}">
            <div>
                <h3>{nombre} {apellido}</h3>
                <p>{profesion}</p>
            </div>
            <div class="perfil-actions">
                <a href="/perfil/{id}">Ver Perfil</a>
            </div>
        </div>
    """)


class TarjetaHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        # Manejar archivos estáticos
        if path.startswith("/static/"):
            static_file = ServerConfig.ROOT / "static" / path.split("/")[-1]
            logger.info(f"Buscando archivo estático: {static_file}")
            return str(static_file)
        return super().translate_path(path)

    def do_GET(self) -> None:
        try:
            parsed = up.urlparse(self.path)

            # Agregamos log para debugging
            logger.info(f"Petición recibida: {self.path}")

            if parsed.path == "/":
                # Ahora mostramos el índice en la ruta principal
                self._send_html(HTMLTemplates.INDEX_HTML)
            elif parsed.path == "/crear":
                # La ruta para crear perfiles ahora es /crear
                self._handle_home()
            elif parsed.path == "/tarjeta":
                self._handle_tarjeta(parsed)
            elif parsed.path == "/perfiles":
                self._handle_perfiles_list()
            elif parsed.path.startswith("/perfil/"):
                perfil_id = parsed.path.split("/")[-1]
                self._handle_perfil_individual(perfil_id)
            elif parsed.path.startswith("/static/"):
                super().do_GET()
            else:
                super().do_GET()

        except Exception as e:
            logger.error(f"Error procesando la petición: {str(e)}")
            self._send_error(500, "Error interno del servidor")

    def _handle_home(self) -> None:
        self._send_html(HTMLTemplates.FORM_HTML)

    def _handle_tarjeta(self, parsed) -> None:
        datos = self._parse_query_params(parsed.query)

        # Validación básica de datos
        if not self._validar_datos(datos):
            self._send_error(400, "Datos inválidos")
            return

        # Seleccionar plantilla según la elección del usuario
        template = getattr(HTMLTemplates, f"CARD_TEMPLATE_{datos['plantilla']}",
                           HTMLTemplates.CARD_TEMPLATE_1)

        # Generar ID único para el perfil
        perfil_id = self._generar_id_unico()

        # Guardar el perfil
        self._guardar_perfil(perfil_id, datos)

        # Modificar la plantilla para agregar el enlace de compartir
        html_content = template.format(**datos)
        html_content = html_content.replace(
            '<p><a href="/">← Crear otro perfil</a></p>',
            f'<p><a href="/">← Crear otro perfil</a> | '
            f'<a href="/perfiles">Ver todos los perfiles</a> | '
            f'<button onclick="navigator.clipboard.writeText(window.location.origin + \'/perfil/{perfil_id}\');">'
            f'Copiar enlace al perfil</button></p>'
        )

        # Enviar la respuesta
        self._send_html(html_content)

    def _parse_query_params(self, query: str) -> Dict[str, str]:
        params = up.parse_qs(query)
        return {
            key: html.escape(params.get(key, [default])[0])
            for key, default in ServerConfig.DEFAULT_VALUES.items()
        }

    def _validar_datos(self, datos):
        """Validación básica de los datos del formulario"""
        try:
            if not datos['nombre'] or not datos['apellido']:
                return False
            edad = int(datos['edad'])
            if edad < 0 or edad > 150:
                return False
            if not datos['profesion']:
                return False
            if not all([datos['habilidad1'], datos['habilidad2'], datos['habilidad3']]):
                return False
            # Validar porcentajes
            for i in range(1, 4):
                porcentaje = int(datos[f'porcentaje{i}'])
                if porcentaje < 0 or porcentaje > 100:
                    return False
            return True
        except ValueError:
            return False

    def _generar_id_unico(self):
        return str(uuid.uuid4())

    def _guardar_perfil(self, perfil_id, datos):
        """Guarda el perfil en un archivo JSON"""
        perfiles_file = ServerConfig.ROOT / "perfiles.json"
        try:
            if perfiles_file.exists():
                with open(perfiles_file, 'r') as f:
                    perfiles = json.load(f)
            else:
                perfiles = {}

            perfiles[perfil_id] = datos

            with open(perfiles_file, 'w') as f:
                json.dump(perfiles, f, indent=2)

        except Exception as e:
            logger.error(f"Error al guardar perfil: {str(e)}")

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

    def _check_static_files(self):
        css_path = ServerConfig.ROOT / "static" / "style.css"
        if not css_path.exists():
            logger.error(f"¡Archivo CSS no encontrado en {css_path}!")
            return False
        return True

    def _handle_perfiles_list(self):
        """Mostrar la lista de perfiles guardados"""
        try:
            perfiles_file = ServerConfig.ROOT / "perfiles.json"
            if perfiles_file.exists():
                with open(perfiles_file, 'r') as f:
                    perfiles = json.load(f)

                perfiles_items = ""
                for perfil_id, datos in perfiles.items():
                    perfiles_items += HTMLTemplates.PERFIL_ITEM_HTML.format(
                        id=perfil_id,
                        nombre=datos.get('nombre', 'Sin nombre'),
                        apellido=datos.get('apellido', ''),
                        profesion=datos.get('profesion', 'Sin profesión'),
                        foto_url=datos.get('foto_url', '')
                    )

                html_content = HTMLTemplates.PERFILES_LIST_HTML.format(
                    perfiles_items=perfiles_items if perfiles_items else "<p>No hay perfiles guardados</p>"
                )
                self._send_html(html_content)
            else:
                self._send_html(HTMLTemplates.PERFILES_LIST_HTML.format(
                    perfiles_items="<p>No hay perfiles guardados</p>"
                ))
        except Exception as e:
            logger.error(f"Error al mostrar perfiles: {str(e)}")
            self._send_error(500, "Error al cargar los perfiles")

    def _handle_perfil_individual(self, perfil_id):
        """Mostrar un perfil específico basado en su ID"""
        try:
            perfiles_file = ServerConfig.ROOT / "perfiles.json"
            if perfiles_file.exists():
                with open(perfiles_file, 'r') as f:
                    perfiles = json.load(f)

                if perfil_id in perfiles:
                    datos = perfiles[perfil_id]
                    plantilla = getattr(HTMLTemplates, f"CARD_TEMPLATE_{datos.get('plantilla', '1')}",
                                        HTMLTemplates.CARD_TEMPLATE_1)

                    # Modifica la plantilla para agregar botón de compartir
                    html_content = plantilla.format(**datos)
                    html_content = html_content.replace(
                        '<p><a href="/">← Crear otro perfil</a></p>',
                        f'<p><a href="/">← Crear otro perfil</a> | '
                        f'<a href="/perfiles">Ver todos los perfiles</a> | '
                        f'<button onclick="navigator.clipboard.writeText(window.location.href);">'
                        f'Copiar enlace</button></p>'
                    )
                    self._send_html(html_content)
                else:
                    self._send_error(404, "Perfil no encontrado")
            else:
                self._send_error(404, "No hay perfiles guardados")
        except Exception as e:
            logger.error(f"Error al mostrar perfil {perfil_id}: {str(e)}")
            self._send_error(500, "Error al cargar el perfil")


def run_server() -> None:
    try:
        handler = TarjetaHandler
        # Verificar archivos estáticos antes de iniciar el servidor
        if not TarjetaHandler._check_static_files(None):
            logger.error("Faltan archivos estáticos necesarios.")
            return

        server_address = ("", ServerConfig.PORT)
        with HTTPServer(server_address, handler) as httpd:
            logger.info(f"🚀 Servidor iniciado en http://localhost:{ServerConfig.PORT}")
            logger.info(f"Directorio raíz: {ServerConfig.ROOT}")
            logger.info(f"Directorio static: {ServerConfig.ROOT / 'static'}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n⏹️ Servidor detenido")
    except Exception as e:
        logger.error(f"Error fatal del servidor: {str(e)}")


if __name__ == "__main__":
    run_server()
