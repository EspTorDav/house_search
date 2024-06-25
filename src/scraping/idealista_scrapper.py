import requests
from bs4 import BeautifulSoup

def idealista_scraper():
    # URL de Idealista para alquiler de viviendas
    url = r"https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_850,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,jardin/?shape=%28%28oemcFlnne%40kp%40meV%3Fkp%40%3Fse%40%3Fmc%40%3FiR%3FeP%3F%7BZnGeuZ~kWb%60EfuCf%7Ci%40kyZ%60zF%29%29&ordenado-por=precios-asc"
    
    # Definir el encabezado User-Agent de Opera GX en Windows 11
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203"
    )

    headers = {
        "User-Agent": user_agent
    }

    response = requests.get(url, headers=headers)
    
    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todos los elementos relevantes de la propiedad
        properties = soup.find_all('div', class_='item-info-container')
        
        # Lista para almacenar los datos de las propiedades filtradas
        data = []
        
        # Iterar sobre cada propiedad encontrada
        for property in properties:
            title_elem = property.find('a', class_='item-link')
            title = title_elem.text.strip()
            price_text = property.find('span', class_='item-price').text.strip()
            url_property = title_elem['href']
            full_url = f"https://www.idealista.com{url_property}"


            # Convertir el precio a número
            try:
                price_number = int(price_text.replace('€', '').replace('.', '').replace('/', '').replace('mes','').strip())
            except ValueError:
                price_number = None

            # Filtrar por condiciones requeridas (precio menor de 850 € y habitaciones entre 2 y 3)
            if price_number is not None and price_number < 850:
                data.append({
                 'Titulo': title ,
                 'Precio': price_number ,
                 'URL': full_url 
            })
    
        return data
    
    else:
        print(f"No se pudo acceder a la página: {url}")
        print(f"Código de estado HTTP: {response.status_code}")
        print(f"Mensaje de error: {response.reason}")
        return None

