import streamlit as st


st.markdown("""#Démonstration d'affichage de données""")

st.markdown("Connexion API et téléchargement des données")

choice = st.selectbox("Choissisez une région :",
             ("Hauts-de-France", "Corse", "Île-de-France"))


st.markdown(choice)

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values[0])
