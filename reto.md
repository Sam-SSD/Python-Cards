# Reto: Generador de Perfiles Personales

## Descripción

Partiendo del generador de tarjetas básico (`server.py`), crea una versión mejorada que permita a los usuarios generar perfiles personales más completos, usando únicamente Python y HTML/CSS (sin frameworks adicionales).

## Objetivos

Extender el servidor actual para:

1. **Capturar más datos personales**:
   - Nombre y apellido
   - Edad
   - Profesión/Ocupación
   - Habilidades (al menos 3)
   - Foto de perfil (URL de imagen)
   - Redes sociales (al menos 2)
   - Color de fondo
   - Color de texto

2. **Mejorar la presentación**:
   - Crear al menos 3 plantillas diferentes de perfil para elegir
   - Permitir seleccionar entre diferentes estilos de fuente
   - Incluir una sección para mostrar las habilidades con barras de progreso
   - Añadir iconos para las redes sociales

3. **Funcionalidades adicionales**:
   - Validación básica de datos en el servidor
   - Opción para guardar el perfil generado con un ID único
   - Página para ver perfiles guardados previamente
   - Botón para compartir el perfil (generar un enlace)

## Restricciones

- Usar únicamente la biblioteca estándar de Python (como en el ejemplo original)
- No utilizar frameworks web ni bibliotecas externas
- Mantener la estructura básica del servidor HTTP actual

## Consejos

- Estudia bien el código de `server.py` para entender cómo funciona
- Organiza tu código en funciones para mantenerlo legible
- Utiliza plantillas HTML con formato de cadena como en el ejemplo original
- Para guardar perfiles, puedes usar archivos de texto o JSON

## Entregables

1. Archivo Python con el servidor extendido
2. Archivos HTML/CSS necesarios
3. README con instrucciones de uso

