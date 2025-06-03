# 🧠 Guía de instalación y uso del proyecto

Este proyecto requiere un entorno virtual y ciertas dependencias para funcionar correctamente. A continuación se detallan los pasos necesarios para prepararlo desde cero.

---

## ⚙️ Crear el entorno virtual

Ejecutar en la raíz del proyecto:

```bash
python -m venv venv
```

---

## ▶️ Activar el entorno virtual

### En **Windows**:

```bash
venv\Scripts\activate
```

### En **macOS / Linux**:

```bash
source venv/bin/activate
```

Una vez activado, el prompt mostrará algo como:

```
(venv) C:\ruta\al\proyecto>
```

---

## 📦 Instalar dependencias

Con el entorno virtual activo, instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Probar el script de importación

Si querés probar el proceso completo de importación de datos desde los XML, seguí estos pasos:

---

## 🧹 Limpiar tablas existentes

Para eliminar las tablas previas (si las hay), ejecutar:

```bash
python scripts/reset_tablas.py
```

---

## 📥 Importar todos los datos

Ejecutar el importador general de datos XML:

```bash
python scripts/importar_todo.py
```

---

## ✅ ¡Listo!
