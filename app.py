from application import create_app
from os import getenv
from config import UATConfig, DevelopConfig, ProductionConfig
import ipdb

configuration = ProductionConfig
environment = getenv("ENV") or "PRODUCTION"

if environment == "DEVELOPMENT":
    configuration = DevelopConfig
elif environment == "UAT":
    configuration = UATConfig

app = create_app(configuration)
if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"], threaded=True)
