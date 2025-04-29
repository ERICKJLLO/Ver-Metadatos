from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def convertir_a_grados_decimales(valor):
    """Convierte coordenadas GPS en formato de grados, minutos y segundos a grados decimales."""
    grados, minutos, segundos = valor
    return grados + (minutos / 60.0) + (segundos / 3600.0)

def procesar_gps(gps_data):
    """Procesa los datos GPS y los convierte a un formato de grados decimales."""
    if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
        latitud = convertir_a_grados_decimales(gps_data['GPSLatitude'])
        longitud = convertir_a_grados_decimales(gps_data['GPSLongitude'])

        # Ajusta según la dirección (Norte/Sur, Este/Oeste)
        if gps_data.get('GPSLatitudeRef') == 'S':
            latitud = -latitud
        if gps_data.get('GPSLongitudeRef') == 'W':
            longitud = -longitud

        return f"{latitud}, {longitud}"
    return "Coordenadas GPS no disponibles"

def es_dato_legible(valor):
    """Determina si un valor de metadato es legible (no binario ni demasiado largo)."""
    if isinstance(valor, bytes):
        return False
    if isinstance(valor, str) and len(valor) > 100:
        return False
    return True

def ver_metadatos(foto):
    imagen = Image.open(foto)
    exif_data = imagen._getexif()
    
    if not exif_data:
        print("No hay metadatos.")
        return

    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == 'GPSInfo':
            gps_data = {}
            for t in value:
                sub_tag = GPSTAGS.get(t, t)
                gps_data[sub_tag] = value[t]
            coordenadas = procesar_gps(gps_data)
            print(f"{tag}: {coordenadas}")
        elif es_dato_legible(value):
            print(f"{tag}: {value}")

# Uso:
ver_metadatos(r"ruta\a\la\foto.jpg")
# Asegúrate de reemplazar "ruta\a\la\foto.jpg" con la ruta real de tu imagen.
