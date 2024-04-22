import logging
from constants import  SENDER_EMAIL, SENDER_EMAIL_PASSWORD, RECEIVER_EMAIL
from bs4 import BeautifulSoup
import smtplib



#funcion que envia email cuando el precio del producto este en el valor especificado
def send_email(price, url_product):
    """this function send email with text and subject specified"""
    
    try:
        #creo objetoi de SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_object:
            

            #se escribe para seguridad
            smtp_object.starttls()
            
            
            #autenticacion
            smtp_object.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            
            
            SUBJECT= "amazon product"
            
            TEXT= f"price of the product now {price}\n\n the url is: {url_product}"
            
            
            #mensaje que se enviara
            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
            
            
            #datos de la persona que recibe el email
            smtp_object.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        

            print("email sent successfully")
        
    
    except smtplib.SMTPException as e:
        print("Error sending email:", e)
    
    
