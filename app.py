# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:59:04 2024

@author: jperezr
"""

import streamlit as st

def main():
    st.title('Quesos de Tlaxcala, Tlax.')
    st.subheader('Precios')

    precios = {
       "Queso Oaxaca 1K": 150,
       "Queso Oaxaca 1/2 k": 80,
       "Queso Panela 1K": 150,
       "Queso Panela 1/2 K": 80,
       "Queso Botanero 1K": 200,
       "Queso Botanero 1/2 k": 100,
       "Requeson 1kg": 100,
       "Requeson 1/2 K": 60,
       "Queso Fresco redondo 3 piezas": 120,
       "Tlacoyos de requeson con chicharron 1 docena": 100,
       "Tlacoyos solo de requeson 1 docena": 100,
       "Tlacoyos solo de chicharrón 1 docena": 100
   }

    for producto, precio in precios.items():
        st.header(f"{producto}: ${precio}")
        
    # Incluir imágenes
    st.image("1.jpg", caption="Queso Oaxaca, directamente de Santa Isabel Tetlatlahuca,Tlaxcala", use_column_width=True)
    st.image("2.jpg", caption="Requesón, directamente de Santa Isabel Tetlatlahuca,Tlaxcala", use_column_width=True)
    st.image("3.jpg", caption="Queso Botanero, directamente de Santa Isabel Tetlatlahuca,Tlaxcala", use_column_width=True)    
    st.image("4.jpg", caption="Tlacoyos estilo, Nanacamilpa, Tlaxcala", use_column_width=True)  

    st.sidebar.title("Informes")
    st.sidebar.write("**Sra. Rafaela Alvarado Elizalde**")
    st.sidebar.write("**WhatsApp: +52 24 6159 3018**") 
    st.sidebar.markdown("---")
    st.sidebar.title("Entregas")
    st.sidebar.markdown("**CALLE: TAMAUlIPAS 39. ÁLVARO OBREGÓN. PROGRESO TIZAPAN. C.P 01080. CDMX**")
    st.sidebar.markdown("---")
    
    st.sidebar.write("**© 2024 Quesos de Tlaxcala, Tlax. Todos los derechos reservados.**")

    # Enlace a Google Maps con la dirección especificada
    st.subheader("")
    map_link = "[Ver en Google Maps](https://www.google.com/maps/place/Calle+Tamaulipas+39,+Progreso+Tizapan,+01080+Ciudad+de+México,+CDMX)"
    
    # Mostrar el enlace en la aplicación
    st.markdown(map_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
