# Generador de Tarjetas Personalizadas

Este es un proyecto simple que permite a los usuarios crear tarjetas personalizadas con su nombre, una breve biografía y un color favorito.

## Descripción

El proyecto consiste en un servidor web minimalista que ofrece:
- Un formulario HTML para ingresar los datos personales
- Una página de tarjeta generada con los datos proporcionados
- Archivos estáticos (CSS, imágenes, etc.)

## Requisitos

- Python 3.x

## Cómo usar

1. Clona o descarga este repositorio

2. Ejecuta el servidor:
   ```
   python server.py
   ```

3. Abre tu navegador web y visita:
   ```
   http://localhost:8000
   ```

4. En el formulario, ingresa:
   - Tu nombre
   - Una breve biografía
   - Tu color favorito (en formato hexadecimal)

5. Haz clic en "Crear tarjeta" para ver tu tarjeta personalizada

## Estructura del proyecto

- `server.py`: El servidor web que maneja las peticiones y genera las tarjetas


## Características

- Servidor HTTP simple basado en Python
- Generación dinámica de HTML
- Sanitización de entradas para prevenir inyecciones HTML
- Diseño responsivo con CSS

## Personalización

Puedes personalizar el aspecto de las tarjetas modificando:
- Las plantillas HTML en `server.py`
