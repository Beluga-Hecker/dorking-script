# Google Dorking Script (OSINT)

Este repositorio contiene un script educativo para realizar búsquedas automatizadas mediante técnicas de **Google Dorking**, utilizadas comúnmente en tareas de inteligencia de fuentes abiertas (OSINT).

- `dorking-script.py`: Permite lanzar una búsqueda en Google con una consulta específica que puede revelar páginas de administración u otros recursos expuestos públicamente.

## ⚠️ Aviso Importante

Este script se publica **exclusivamente con fines educativos, legales y de investigación autorizada**.  
No está destinado a realizar auditorías en sistemas ajenos sin consentimiento.  
El uso inadecuado puede infringir los términos de servicio de Google o leyes locales e internacionales.

## 📚 Requisitos

- Python 3.x
- Librería:
  - `googlesearch-python`

Puedes instalar la dependencia necesaria con:

```bash
pip install googlesearch-python
```

## 🛠 Uso

1. Abre el archivo `dorking-script.py`.
2. Asegúrate de que tu consulta Dorking esté correctamente definida.
3. Ejecuta el script:

```bash
python dorking-script.py
```

Este ejemplo utiliza la siguiente consulta por defecto:

```python
query = "site:.com inurl:admin login AND user"
```

Puedes modificarla según tus necesidades y objetivos educativos.
