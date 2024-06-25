import csv
from scraping.idealista_scrapper import idealista_scraper

def main():
    # Scraping de datos desde Idealista.
    all_data = idealista_scraper()
    
    # Ruta donde se guardará el archivo CSV
    csv_path = 'data/alquileres.csv'
    
    # Abrir el archivo CSV en modo escritura con utf-8 encoding
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        # Definir los nombres de las columnas
        fieldnames = ['Titulo', 'Precio', 'URL']
        
        # Crear el escritor CSV con el delimitador especificado
        writer = csv.writer(file, delimiter=',')
        
        # Escribir el encabezado
        writer.writerow(fieldnames)
        
        # Escribir cada fila de datos
        for data_row in all_data:
            writer.writerow([data_row['Titulo'], data_row['Precio'], data_row['URL']])
    
    print(f"Datos guardados en {csv_path}")

if __name__ == "__main__":
    main()

