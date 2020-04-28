class DefaultConfig(object):
    ENVIRONMENT = "PRODUCTION"
    DEBUG = False


class UATConfig(DefaultConfig):
    ENVIRONMENT = "UAT"
    DEBUG = False


class DevelopConfig(DefaultConfig):
    ENVIRONMENT = "DEVELOPMENT"
    DEBUG = True
    PORT = 8888
    HOST = "localhost"


class ProductionConfig(DefaultConfig):
    ENVIRONMENT = "PRODUCTION"
    DEBUG = False
