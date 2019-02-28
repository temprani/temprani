#app.config.update(dict(
#     SECRET_KEY='very secret key',
#     SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class BaseConfig(object):
    SECRET_KEY = 'makesure to set a very key'

class DevelopmentConfig(BaseConfig):
    DEBUG =True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
    pass    

class TestingConfig(BaseConfig):
    pass

configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}
