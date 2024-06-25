import requests
from bs4 import BeautifulSoup

def idealista_scraper():
     # Reemplaza con la URL real
    url = r"https://www.idealista.com/areas/alquiler-viviendas/?shape=%28%28oemcFlnne%40kp%40meV%3Fkp%40%3Fse%40%3Fmc%40%3FiR%3FeP%3F%7BZnGeuZ~kWb%60EfuCf%7Ci%40kyZ%60zF%29%29" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    properties = soup.find_all('div', class_='property')
    
    data = []
    
    for property in properties:
        title = property.find('a', class_='item-link').text.strip()
        price = property.find('span', class_='item-price').text.strip()
        location = property.find('span', class_='item-detail').text.strip()
        rooms = property.find('span', class_='icon-bedrooms').find_next_sibling('span').text.strip()
        pets_allowed = 'admite mascotas' in property.find('span', class_='item-tags').text.strip()
        url_property = property.find('a', class_='item-link')['href']
        
        # Convertir el precio a número
        price_number = int(price.split()[0].replace('.', '').replace('€', ''))
        
        # Filtrar por condiciones requeridas
        if pets_allowed and int(rooms) >= 3 and price_number <= 800:
            data.append({
                'Título': title,
                'Precio': price,
                'Ubicación': location,
                'Habitaciones': rooms,
                'url_casa':url_property
            })
    
    return data
