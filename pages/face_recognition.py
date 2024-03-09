import streamlit as st
import face_recognition

st.markdown("# Face Recognition️")
st.sidebar.markdown("# Face Recognition")

picture1 = st.camera_input("Take a picture 1")
picture2 = st.camera_input("Take a picture 2")

if picture1 and picture2 is not None:
    # st.image(picture1)
    # Carga la imagen del archivo y la convierte en un arreglo de características faciales
    image_of_person = face_recognition.load_image_file(picture1)
    person_face_encoding = face_recognition.face_encodings(image_of_person)[0]

    # Carga una segunda imagen y la convierte en un arreglo de características para comparar
    unknown_image = face_recognition.load_image_file(picture2)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Compara las dos caras y devuelve True si coinciden
    results = face_recognition.compare_faces([person_face_encoding], unknown_face_encoding)

    if results[0]:
        st.text("Es la misma persona.")
    else:
        st.text("No es la misma persona.")
