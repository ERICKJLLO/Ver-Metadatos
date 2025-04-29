# Ver Metadatos de Imágenes

Este script permite extraer y visualizar los metadatos de una imagen, incluyendo información GPS si está disponible.

## Requisitos

- Python 3.x
- Biblioteca `Pillow` (instalable con `pip install pillow`)

## Uso

1. Asegúrate de tener instalada la biblioteca `Pillow`.
2. Coloca la imagen de la que deseas extraer los metadatos en una ubicación accesible.
3. Modifica la línea final del script para incluir la ruta de tu imagen:

   ```python
   ver_metadatos(r"ruta\a\la\foto.jpg")
   ```

   Reemplaza `"ruta\a\la\foto.jpg"` con la ruta real de tu archivo de imagen.

4. Ejecuta el script:

   ```bash
   python metadatos.py
   ```

## Funcionalidades

- **Extracción de metadatos EXIF**: Muestra todos los metadatos legibles de la imagen.
- **Procesamiento de coordenadas GPS**: Convierte las coordenadas GPS a un formato de grados decimales si están disponibles.

## Notas

- Si la imagen no contiene metadatos, el script mostrará un mensaje indicando que no hay metadatos disponibles.
- Los valores binarios o demasiado largos no se mostrarán para evitar problemas de legibilidad.

## Ejemplo de Salida

```
Make: Canon
Model: Canon EOS 80D
DateTime: 2023:03:15 14:23:45
GPSInfo: 40.7128, -74.0060
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
