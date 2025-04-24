import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



st.set_page_config(page_title="Graphique sur Papier Millimétré", layout="centered")
st.markdown("<h4>📐 🐆 🌹 Ghaydoun's Graph Paper Generator 🌹 🐆 📐</h4>", unsafe_allow_html=True)

paper_width = 30  # cm
paper_height = 20  # cm

st.sidebar.header("Paramètres")
x_values = st.sidebar.text_input("Coordonnées X (séparées par des virgules)", "1, 2, 3, 4, 5, 6, 7, 8, 9, 30")
y_values = st.sidebar.text_input("Coordonnées Y (séparées par des virgules)", "1, 2, 3, 4, 5, 6, 7, 8, 9, 20")
paper_width_adjust = st.sidebar.number_input("Largeur de l'espace de dessin (cm)", min_value=1, max_value=100, value=30)
paper_height_adjust = st.sidebar.number_input("Hauteur de l'espace de dessin (cm)", min_value=1, max_value=100, value=20)


try:
    x = list(map(float, x_values.split(",")))
    y = list(map(float, y_values.split(",")))
    if len(x) != len(y):
        st.error("Le nombre de valeurs X et Y doit être le même.")
    else:
        x_max_data = max(x)
        y_max_data = max(y)

        if paper_width_adjust == paper_width:
            echelle_x = paper_width / x_max_data if x_max_data != 0 else 1
        else:
            echelle_x = paper_width_adjust / x_max_data if x_max_data != 0 else 1

        if paper_height_adjust == paper_height:
            echelle_y = paper_height / y_max_data if y_max_data != 0 else 1
        else:
            echelle_y = paper_height_adjust / y_max_data if y_max_data != 0 else 1

        

        # Conversion des coordonnées en centimètres sur le papier
        x_scaled = [xi * echelle_x for xi in x]
        y_scaled = [yi * echelle_y for yi in y]

        fig, ax = plt.subplots(figsize=(paper_width / 2.54, paper_height / 2.54), dpi=100)
        ax.set_xlim(0, paper_width)
        ax.set_ylim(0, paper_height)
        ax.set_aspect('equal')

        # Grille tous les 1 mm (0.1 cm)
        ax.set_xticks(np.arange(0, paper_width + 0.1, 0.1), minor=True)
        ax.set_yticks(np.arange(0, paper_height + 0.1, 0.1), minor=True)
        ax.grid(which='minor', color='lightgrey', linestyle='-', linewidth=0.3)

        # Grille principale tous les 1 cm
        ax.set_xticks(np.arange(0, paper_width + 1, 1))
        ax.set_yticks(np.arange(0, paper_height + 1, 1))
        ax.grid(which='major', color='grey', linestyle='-', linewidth=0.8)

        ax.scatter(x_scaled, y_scaled, color='red', zorder=5)
        for xi, yi, orig_x, orig_y in zip(x_scaled, y_scaled, x, y):
            ax.text(xi + 0.2, yi + 0.2, f"({orig_x}, {orig_y})", fontsize=8, color='black')

        ax.set_xlabel("cm")
        ax.set_ylabel("cm")
        ax.tick_params(direction='in', length=3, width=1)
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

        st.pyplot(fig)

        st.success(f"Échelle X : 1 cm = {1/echelle_x:.4f} unité(s) → 1 unité = {echelle_x:.3f} cm")
        st.success(f"Échelle Y : 1 cm = {1/echelle_y:.4f} unité(s) → 1 unité = {echelle_y:.2f} cm")

except ValueError:
    st.error("Veuillez entrer des valeurs numériques valides.")