import logging
import requests
from constants import HEADERS, URL_PRODUCT
from bs4 import BeautifulSoup




def get_product_price():
    """
    Obtiene el precio de un producto desde amazon.jp utilizando web scraping.
    Retorna el precio del producto si se encuentra, o None si hay un error.
    """
    
    
    #los headers, son los encabezados que el navegador web envia al entrar en amazon, al agregarlos en headers simulamos un navegador web
    # https://myhttpheader.com/

    try:
        #get request a la pag que deseo hacer web scraping
        response=requests.get(URL_PRODUCT, headers=HEADERS)


        # Lanzar excepción si hay un error en la respuesta HTTP
        response.raise_for_status()  
        
        
        # Imprimo el código de estado de la respuesta HTTP
        print("HTTP Status Code:", response.status_code)
    
    
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
            
            # Encontrar el elemento HTML que contiene el precio del producto
            price=soup.find("span", class_="a-offscreen").get_text()
            
            
            #imprimiendo el precio
            print(price)
            
            
            # global price_without_simbol
            
            
            #eliminando el simbolo de precio 
            price_without_simbol=price.strip("￥")
            
            
            #eliminando la coma ','
            price_without_simbol= price_without_simbol.replace(",", "") 
            
                       
            
            print(f"the amazon product price is {price_without_simbol}")
            
            return  price_without_simbol
                   
        
        except AttributeError:
        
            logging.error("Couldn't find the specified  information  on the page.")

