from textwrap import dedent


class HTMLTemplates:
    INDEX_HTML = dedent("""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Generador de Perfiles - Inicio</title>
                <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
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
        <html lang=\"es\">
        <head>
            <meta charset=\"utf-8\">
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
            <title>Genera tu perfil</title>
            <link rel=\"icon\" href=\"/static/favicon.ico\" type=\"image/x-icon\">
            <link rel=\"stylesheet\" href=\"/static/style.css\">
        </head>
        <body>
            <div class=\"container\">
                <h1>Generador de Perfiles</h1>
                <form action=\"/tarjeta\" method=\"get\">
                    <div class=\"form-group\">
                        <label for=\"nombre\">Nombre:</label>
                        <input id=\"nombre\" name=\"nombre\" required>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"apellido\">Apellido:</label>
                        <input id=\"apellido\" name=\"apellido\" required>      
                    </div>
                    <div class=\"form-group\">
                        <label for=\"edad\">Edad:</label>
                        <input id=\"edad\" name=\"edad\" type=\"number\" required>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"profesion\">Profesión:</label>
                        <input id=\"profesion\" name=\"profesion\" required>
                    </div>
                    <div class=\"form-group\">
                        <label>Habilidades:</label>
                        <div style=\"display: flex; gap: 10px; margin-bottom: 10px;\">
                            <input name=\"habilidad1\" placeholder=\"Habilidad 1\" required style=\"flex: 2;\">
                            <input name=\"porcentaje1\" type=\"number\" min=\"0\" max=\"100\" placeholder=\"%\" required style=\"flex: 1; width: 60px;\">
                        </div>
                        <div style=\"display: flex; gap: 10px; margin-bottom: 10px;\">
                            <input name=\"habilidad2\" placeholder=\"Habilidad 2\" required style=\"flex: 2;\">
                            <input name=\"porcentaje2\" type=\"number\" min=\"0\" max=\"100\" placeholder=\"%\" required style=\"flex: 1; width: 60px;\">
                        </div>
                        <div style=\"display: flex; gap: 10px;\">
                            <input name=\"habilidad3\" placeholder=\"Habilidad 3\" required style=\"flex: 2;\">
                            <input name=\"porcentaje3\" type=\"number\" min=\"0\" max=\"100\" placeholder=\"%\" required style=\"flex: 1; width: 60px;\">
                        </div>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"foto_url\">URL de foto:</label>
                        <input id=\"foto_url\" name=\"foto_url\" type=\"url\" required>
                    </div>
                    <div class=\"form-group\">
                        <label>Redes Sociales:</label>
                        <div style=\"display: flex; gap: 10px; margin-bottom: 10px;\">
                            <input name=\"red_social1\" placeholder=\"Red Social 1\" required style=\"flex: 2;\">
                        </div>
                        <div style=\"display: flex; gap: 10px;\">
                            <input name=\"red_social2\" placeholder=\"Red Social 2\" required style=\"flex: 2;\">
                        </div>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"color_fondo\">Color de fondo:</label>
                        <input id=\"color_fondo\" name=\"color_fondo\" type=\"color\" value=\"#ffffff\" required>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"color_texto\">Color de texto:</label>
                        <input id=\"color_texto\" name=\"color_texto\" type=\"color\" value=\"#000000\" required>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"estilo_fuente\">Estilo de fuente:</label>
                        <select id=\"estilo_fuente\" name=\"estilo_fuente\">
                            <option value=\"Arial\">Arial</option>
                            <option value=\"Helvetica\">Helvetica</option>
                            <option value=\"Times New Roman\">Times New Roman</option>
                        </select>
                    </div>
                    <div class=\"form-group\">
                        <label for=\"plantilla\">Diseño de plantilla:</label>
                        <select id=\"plantilla\" name=\"plantilla\">
                            <option value=\"1\">Plantilla 1</option>
                            <option value=\"2\">Plantilla 2</option>
                            <option value=\"3\">Plantilla 3</option>
                        </select>
                    </div>
                    <button type=\"submit\">Crear Perfil</button>
                </form>
                <p style="text-align: center; margin-top: 2rem;">
                    <a href="/" class="btn secondary">← Volver al inicio</a>
                </p>
            </div>
        </body>
        </html>
    """
                       )

    CARD_TEMPLATE_1 = dedent("""
            <!DOCTYPE html>
            <html lang=\"es\">
            <head>
                <meta charset=\"utf-8\">
                <title>Perfil de {nombre}</title>
                <link rel=\"icon\" href=\"/static/favicon.ico\" type=\"image/x-icon\">
                <link rel=\"stylesheet\" href=\"/static/style.css\">
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
                <div class=\"profile-card\">
                    <img src=\"{foto_url}\" alt=\"{nombre}\" class=\"profile-image\">
                    <h1>{nombre} {apellido}</h1>
                    <p>Edad: {edad} años</p>
                    <p>Profesión: {profesion}</p>

                    <h2>Habilidades</h2>
                    <div class=\"skills\">
                        <p>{habilidad1} - {porcentaje1}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje1}%\"></div></div>
                        <p>{habilidad2} - {porcentaje2}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje2}%\"></div></div>
                        <p>{habilidad3} - {porcentaje3}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje3}%\"></div></div>
                    </div>

                    <h2>Redes Sociales</h2>
                    <p><a href=\"{red_social1}\">Red Social 1</a></p>
                    <p><a href=\"{red_social2}\">Red Social 2</a></p>

                        <p>__COMPARTIR_PERFIL__</p>
                    </div>
                    
                </div>
                <div style="margin-top: 1rem; text-align: center;">
                        <a href="/" class="btn secondary">Volver al inicio</a>
                </div>
                </div>
            </body>
            </html>
        """
                             )

    CARD_TEMPLATE_2 = dedent("""
            <!DOCTYPE html>
            <html lang=\"es\">
            <head>
                <meta charset=\"utf-8\">
                <title>Perfil de {nombre}</title>
                <link rel=\"icon\" href=\"/static/favicon.ico\" type=\"image/x-icon\">                
                <link rel=\"stylesheet\" href=\"/static/style.css\">
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
                <div class=\"profile-card\">
                    <img src=\"{foto_url}\" alt=\"{nombre}\" class=\"profile-image\">
                    <h1 style=\"text-transform: uppercase;\">{nombre} {apellido}</h1>
                    <p><strong>Edad:</strong> {edad} años | <strong>Profesión:</strong> {profesion}</p>

                    <h2>HABILIDADES</h2>
                    <div class=\"skills\" style=\"width: 100%;\">
                        <p>{habilidad1} - {porcentaje1}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje1}%\"></div></div>
                        <p>{habilidad2} - {porcentaje2}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje2}%\"></div></div>
                        <p>{habilidad3} - {porcentaje3}%</p>
                        <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje3}%\"></div></div>
                    </div>

                    <h2>CONTACTO</h2>
                    <div style=\"display: flex; justify-content: space-around; width: 100%;\">
                        <a href=\"{red_social1}\" target=\"_blank\">Red Social 1</a>
                        <a href=\"{red_social2}\" target=\"_blank\">Red Social 2</a>
                    </div>
                        <p>__COMPARTIR_PERFIL__</p>
                    </div>
                    
                </div>
                <div style="margin-top: 1rem; text-align: center;">
                        <a href="/" class="btn secondary">Volver al inicio</a>
                </div>
            </body>
            </html>
        """
                             )

    CARD_TEMPLATE_3 = dedent("""
            <!DOCTYPE html>
            <html lang=\"es\">
            <head>
                <meta charset=\"utf-8\">
                <title>Perfil de {nombre}</title>
                <link rel=\"icon\" href=\"/static/favicon.ico\" type=\"image/x-icon\">
                <link rel=\"stylesheet\" href=\"/static/style.css\">
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
                <div class=\"profile-card\">
                    <div class=\"header\">
                        <h1>{nombre} {apellido}</h1>
                        <p>{profesion}</p>
                    </div>

                    <div class=\"content\">
                        <img src=\"{foto_url}\" alt=\"{nombre}\" class=\"profile-image\">
                        <p>Edad: {edad} años</p>

                        <h3>Mis Habilidades</h3>
                        <div class=\"skills\">
                            <p>{habilidad1} - {porcentaje1}%</p>
                            <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje1}%\"></div></div>
                            <p>{habilidad2} - {porcentaje2}%</p>
                            <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje2}%\"></div></div>
                            <p>{habilidad3} - {porcentaje3}%</p>
                            <div class=\"skill-bar\"><div class=\"skill-progress\" style=\"width: {porcentaje3}%\"></div></div>
                        </div>

                        <div class=\"social-links\">
                            <a href=\"{red_social1}\" target=\"_blank\">Red Social 1</a>
                            <a href=\"{red_social2}\" target=\"_blank\">Red Social 2</a>
                        </div>
                        <p>__COMPARTIR_PERFIL__</p>
                    </div>
                    
                </div>
                <div style="margin-top: 1rem; text-align: center;">
                        <a href="/" class="btn secondary">Volver al inicio</a>
                </div>
            </body>
            </html>
        """
                             )

    PERFILES_LIST_HTML = dedent("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Perfiles Guardados</title>
            <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
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
                <a href="/crear" class="btn">Crear Nuevo Perfil</a> <a href="/" class="btn secondary">Volver al inicio</a>
                <h2>Lista de Perfiles</h2>
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
                <a href="/perfil/{id}" class="btn secondary" style="margin-right: 10px;">Ver Perfil</a>
                <a href="#" class="btn delete" onclick="eliminarPerfil('{id}'); return false;">Eliminar</a>
            </div>
        </div>
        <script>
            function eliminarPerfil(id) {{
                if (confirm('¿Estás seguro de eliminar este perfil?')) {{
                    fetch('/eliminar/' + id, {{ method: 'POST' }})
                        .then(response => {{
                            if (response.ok) {{
                                alert('Perfil eliminado correctamente');
                                window.location.reload();
                            }} else {{
                                alert('Error al eliminar el perfil');
                            }}
                        }})
                        .catch(err => {{
                            alert('Error de conexión');
                            console.error(err);
                        }});
                }}
            }}
        </script>
    """)

