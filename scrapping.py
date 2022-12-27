# Importar las librerías necesarias
import requests
from bs4 import BeautifulSoup

# Enviar una solicitud a la página web y obtener el código HTML
url = 'https://www.elportaldemusica.es/lists/top-100-canciones/2022/1'
page = requests.get(url)
html = page.text

# Crear un objeto BeautifulSoup a partir del código HTML
soup = BeautifulSoup(html, 'html.parser')


# Buscar la información deseada en el código HTML
elementos_1 = soup.find_all('div', class_='name')  # Busca todos los elementos div con la clase 'nombre-de-la-clase' en la página
elementos_2 = soup.find_all('div', class_='related')  # Busca todos los elementos div con el id 'id-del-elemento' en la página

# Guardar los resultados en un archivo de texto
with open('resultados.txt', 'w') as f:
    for elemento in elementos_1:
        f.write(elemento.text)
    for elemento in elementos_2:
        f.write(elemento.text)
    print("Lista creada con extio")
    
