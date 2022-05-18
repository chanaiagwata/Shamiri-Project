import os

class Config:

    '''
    General configuration parent class
    '''
    SECRET_KEY = 'krisistall'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/shamiri'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
