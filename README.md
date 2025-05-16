# 🧑‍💻 Generador de Perfiles Personales

### 📘 English version

[Click here to see the README in English](README_EN.md)

---

![Banner](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python) ![Estado](https://img.shields.io/badge/Proyecto-Completo-success)  
**Versión mejorada del generador de tarjetas, ahora con perfiles personalizables, plantillas visuales y gestión de datos.**

---

## 🎯 Descripción

Este proyecto permite generar perfiles personales interactivos con diseño visual atractivo y múltiples plantillas. El sistema está desarrollado usando únicamente Python, HTML y CSS sin frameworks adicionales.

---

## 🛠️ Funcionalidades

✅ Formulario interactivo para ingresar datos del perfil  
✅ 3 plantillas de diseño visual para elegir  
✅ Personalización de colores, fuentes y fondo  
✅ Vista previa con barras de habilidades animadas  
✅ Enlace compartible para cada perfil  
✅ Listado dinámico de perfiles creados  
✅ Eliminación de perfiles con confirmación  
✅ Estilo visual adaptable y responsive

---

## 🧩 Bonus Implementados

- ✅ Guardado de perfiles con UUID en archivo JSON
- ✅ Vista individual de perfiles (`/perfil/<id>`)
- ✅ Eliminación directa desde la lista
- ✅ Botón para copiar enlace del perfil
- ✅ Feedback visual con alertas

---

## 📂 Estructura del Proyecto

```
📁 /static
    └── style.css
    └── favicon.ico
📄 templates.html
📄 server.py
📄 perfil_manager.py
📄 storage.py
📄 validaciones.py
📄 perfiles.json
```

---

## 🚀 Instrucciones para Ejecutar

1. Asegúrate de tener **Python 3.10 o superior** instalado.
2. Clona este repositorio desde GitHub:

   ```bash
   git clone https://github.com/Sam-SSD/Python-Cards.git
   ```

3. Navega al directorio del proyecto:

   ```bash
   cd Python-Cards
   ```

4. Ejecuta el sistema desde el archivo principal:

   ```bash
   python server.py
   ```
5. Abre tu navegador y visita la URL:

   ```bash
    http://localhost:8000
    ```

6. ¡Listo! Ahora puedes crear y gestionar tus perfiles personales.
---

## 📸 Vista Previa

| Formulario | Tarjeta 1 | Tarjeta 2 | Listado |
|-----------|-----------|-----------|---------|
| ![form](https://imgur.com/formulario.png) | ![card1](https://imgur.com/card1.png) | ![card2](https://imgur.com/card2.png) | ![listado](https://imgur.com/listado.png) |

---
