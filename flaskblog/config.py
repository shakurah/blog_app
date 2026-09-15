import os
from dotenv import load_dotenv
load_dotenv()
print(repr(os.getenv('EMAIL_USERNAME')))
print(repr(os.getenv('APP_PASSWD')))
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = os.getenv('EMAIL_USERNAME')

    APP_PASSWORD = os.getenv('APP_PASSWD')



    