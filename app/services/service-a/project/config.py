# project/config.py


import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb://service-a-db:27017/data"
    REDIS_URL = 'redis://redis:6379/0'


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG_TB_ENABLED = True
    # MONGO_URI = os.environ.get('DEV_URI')

class ProductionConfig(BaseConfig):
    # MONGO_URI = os.environ.get('PROD_URI')
    """Production configuration"""
