from scraping.idealista_scrapper import idealista_scraper
import pandas as pd

def main():
    all_data = idealista_scraper()

    df = pd.DataFrame(all_data)
    df.to_csv('data/alquileres.csv', index=False)
    print("Datos guardados en data/alquileres.csv")

if __name__ == "__main__":
    main()
