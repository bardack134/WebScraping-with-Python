import logging
import requests
from constants import HEADERS, URL_PRODUCT
from bs4 import BeautifulSoup


def get_product_price():
    #los headers, son los encabezados que el navegador web envia al entrar en amazon, al agregarlos en headers simulamos un navegador web
    # https://myhttpheader.com/

    try:
        #get request a la pag que deseo hacer web scraping
        response=requests.get(URL_PRODUCT, headers=HEADERS)


        # Lanzar excepción si hay un error en la respuesta HTTP
        response.raise_for_status()  
        
        
        # Imprimo el código de estado de la respuesta HTTP
        print(response.status_code)
    
    
    # Manejar errores relacionados con la solicitud HTTP    
    except requests.exceptions.RequestException as err:
        
        logging.error("Error during the http request ")
        logging.error(err)
        
        
    except Exception as err:
        
        # Manejar cualquier otro error inesperado
        logging.error("There was an ambiguous exception that occurred while handling your request.")
        logging.error(err) 
        
        
    #codigo que corre si no hubieron excepciones
    else:
            
        #guardando la informacion de la pag web
        response_html=response.text 


        #creanndo objeto de la clase beautifulsoup para web scrapping
        soup = BeautifulSoup(response_html, 'html.parser')


        #si la pag no tiene el elemento que estoy buscando fallara, por lo que usamos "errors handling" 
        try:
            price=soup.find("span", class_="a-offscreen").get_text()
            
            #imprimiendo el precio
            print(price)
            
            
            #eliminando el simbolo de precio 
            price_without_simbol=price.strip("￥")
            
            
            print(price_without_simbol)
        
        
        except AttributeError:
        
            logging.error("Couldn't find the specified  information  on the page.")


def main():
    price = get_product_price()
    if price is not None:
        print(price)

if __name__ == "__main__":
    main()    