import logging
import requests
from constants import HEADERS, URL_PRODUCT, SENDER_EMAIL, SENDER_EMAIL_PASSWORD, RECEIVER_EMAIL
from bs4 import BeautifulSoup
import smtplib
from search_price_product import get_product_price
from send_email_module import send_email


#valor del producto que deseamos comprar, el precio del producto es menor o igual a este precio, recibimos el email con los datos del producto
BUY_PRICE=76000


   
    
def main():
    #funcion donde obtenemos el precio del producto
    price = get_product_price()
    
    if price is not None:
        
        print(price)
        
        #enviamos correo con la informacion del producto si el precio es menor o igual al establecido inicialmente
        if int(price)<= BUY_PRICE:

            send_email(price, url_product=URL_PRODUCT)
        
        
        
if __name__ == "__main__":
    main()    