import csv
import requests
from bs4 import BeautifulSoup

# URL de la página que deseas raspar
url = 'https://www.elcomercio.com/ultima-hora/'

# Obtener el HTML
resultado_obtenido = requests.get(url)
html_obtenido = resultado_obtenido.text


#Parsear HTML
soup = BeautifulSoup(html_obtenido, "html.parser")
primer_h2= soup.find('h2')

#encontrar todas los links
contenedorNoticias =  soup.find_all('h4')

# Abrir archivo CSV en modo escritura
with open('WebScraping.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Crear un escritor CSV
    writer = csv.writer(csvfile)
    
    # Escribir encabezados
    writer.writerow(['Título', 'Contenido'])
    
    for contenedorNoticias in contenedorNoticias:
        linksNoticias= contenedorNoticias.find('a')
        if linksNoticias:
            url_noticia = linksNoticias.get('href')
            resultado_noticia = requests.get(url_noticia)
            html_Noticia = resultado_noticia.text
            soup_noticia= BeautifulSoup(html_Noticia, "html.parser")
            TituloNoticia= soup_noticia.find('h1')
            ContenidoNoticia= soup_noticia.find_all('p')
            
            # Escribir título y contenido de la noticia en el archivo CSV
            writer.writerow([TituloNoticia.text.strip(), '\n'.join([p.text.strip() for p in ContenidoNoticia])])
    
    print('Se creo el archivo')

        
            
    
    

