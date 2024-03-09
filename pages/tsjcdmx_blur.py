import streamlit as st
import io
from google.cloud import storage

st.markdown("# TSJCDMX Blur")
st.sidebar.markdown("# TSJCDMX Blur")

# Credenciales de Cloud Storage
bucket_name = "x"
credentials_path = '/Users/thom/Downloads/nuu-test-env-key.json'

# Inicializar el cliente de Cloud Storage
client = storage.Client.from_service_account_json(credentials_path)

# Obtener el bucket
bucket = client.bucket(bucket_name)

# Obtener una lista de los archivos del bucket
blobs = bucket.list_blobs()

# Lista para almacenar los nombres de los archivos
nombres_archivos = []

# Recorrer los archivos y agregar sus nombres a la lista
for blob in blobs:
  nombres_archivos.append(blob.name)

# Seleccionar un archivo de la lista desplegable
archivo_seleccionado = st.selectbox("Selecciona un video", nombres_archivos)

accion = st.radio("Elige el tipo de desenfoque:", ["Ocultar", "Difuminar"])
tipo = st.checkbox("Desenfoque solo de rostros")

# Mostrar un indicador de progreso
with st.spinner("Cargando video..."):
  # Descargar el video seleccionado a memoria
  video_bytes = io.BytesIO()
  bucket.blob(archivo_seleccionado).download_to_file(video_bytes)

# Bandera para controlar la reproducción
video_playing = False

def reproducir_video():
  global video_playing

  if not video_playing:
    video_playing = True
    st.video(video_bytes)

# Botón para reproducir el video
boton_reproducir = st.button("Reproducir video")

if boton_reproducir:
  reproducir_video()
