import streamlit as st
import plotly.express as px
import pandas as pd

def calculer_emissions_voiture(distance_km, consommation_l_km, facteur_emission=2.31):
    return distance_km * consommation_l_km * facteur_emission

def calculer_emissions_avion(distance_km, facteur_emission=0.255):
    return distance_km * facteur_emission

def calculer_emissions_electricite(consommation_kwh, facteur_emission=0.233):
    return consommation_kwh * facteur_emission

# Interface utilisateur avec Streamlit
st.title("Calculateur d'émissions de CO2")

st.header("Voiture")
voiture_distance = st.number_input("Distance parcourue en voiture (km) :", min_value=0.0, step=0.1)
voiture_consommation = st.number_input("Consommation moyenne de la voiture (L/km) :", min_value=0.0, step=0.01)

st.header("Avion")
avion_distance = st.number_input("Distance parcourue en avion (km) :", min_value=0.0, step=0.1)

st.header("Électricité")
electricite_consommation = st.number_input("Consommation électrique (kWh) :", min_value=0.0, step=0.1)

if st.button("Calculer"):
    try:
        emissions_voiture = calculer_emissions_voiture(voiture_distance, voiture_consommation)
        emissions_avion = calculer_emissions_avion(avion_distance)
        emissions_electricite = calculer_emissions_electricite(electricite_consommation)

        total_emissions = emissions_voiture + emissions_avion + emissions_electricite

        st.subheader("Résultats")
        st.write(f"**Émissions de CO2 pour la voiture :** {emissions_voiture:.2f} kg")
        st.write(f"**Émissions de CO2 pour l'avion :** {emissions_avion:.2f} kg")
        st.write(f"**Émissions de CO2 pour l'électricité :** {emissions_electricite:.2f} kg")
        st.write(f"**Total des émissions de CO2 :** {total_emissions:.2f} kg")

        # Sauvegarder les résultats dans un fichier CSV
        resultats = pd.DataFrame({
            'Catégorie': ['Voiture', 'Avion', 'Électricité'],
            'Emissions (kg)': [emissions_voiture, emissions_avion, emissions_electricite]
        })
        resultats.to_csv('resultat.csv', index=False)
        st.success("Les résultats ont été sauvegardés dans 'resultat.csv'.")

        # Création d'un diagramme camembert avec Plotly Express
        fig = px.pie(resultats, values='Emissions (kg)', names='Catégorie', title="Répartition des émissions de CO2",
                     color_discrete_sequence=['#ff9999', '#66b3ff', '#99ff99'])
        st.plotly_chart(fig)

    except ValueError:
        st.error("Veuillez entrer des valeurs valides.")
