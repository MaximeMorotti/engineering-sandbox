# front-end part
import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. UI SCAFFOLDING (Configuration de la page) ---
st.set_page_config(page_title="Dashboard for Scientist", page_icon="📊", layout="wide")

st.title("🧪 Bio-Math Data Explorer")
st.sidebar.header("Configuration")

# --- 2. UPLOADER INTERFACE ---
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lecture du fichier
    df = pd.read_csv(uploaded_file)
    st.success("Fichier chargé avec succès !")

    # --- 3. LAYOUT DESIGN (Tabs) ---
    tab1, tab2, tab3 = st.tabs(
        ["📄 Aperçu des données", "🔢 Statistiques", "📈 Graphiques"]
    )

    with tab1:
        st.subheader("Data Head")
        # Affiche les 10 premières lignes
        st.dataframe(df.head(10))

    with tab2:
        st.subheader("Résumé Mathématique")
        # Génère les stats descriptives (Mean, Std, etc.)
        st.write(df.describe())

    with tab3:
        st.subheader("Visualisations Interactives")

        # Sidebar pour les réglages des graphiques
        st.sidebar.divider()
        st.sidebar.subheader("Réglages des graphiques")

        # Détection des colonnes numériques pour le plotting
        num_cols = df.select_dtypes(include=["number"]).columns.tolist()

        if len(num_cols) >= 1:
            col_x = st.sidebar.selectbox("Variable X (Distribution)", num_cols)

            # Exemple de plot (Intégration future pour Personne A)
            fig = px.histogram(df, x=col_x, title=f"Distribution de {col_x}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Aucune colonne numérique détectée pour les graphiques.")

else:
    st.info(
        "👋 Bienvenue ! Veuillez uploader un fichier CSV dans la barre latérale pour commencer l'analyse."
    )
    # Image ou message de bienvenue
