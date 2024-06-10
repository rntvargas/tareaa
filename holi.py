import streamlit as st
import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def preview_data(self):
        return self.data.head(10)

    def calculate_statistics(self):
        return self.data.describe()

def main():
    st.title('Análisis de Datos con Streamlit')
    
    uploaded_file = st.file_uploader("Carga un archivo CSV", type="csv")
    if uploaded_file is not None:
        file_path = uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        handler = DataHandler(file_path)
        handler.load_data()
        
        data_preview = handler.preview_data()
        statistics = handler.calculate_statistics()
        
        st.write("Vista previa de los datos:", data_preview)
        st.write("Estadísticas descriptivas:", statistics)

if __name__ == '__main__':
    main()


