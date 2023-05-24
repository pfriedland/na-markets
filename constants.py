import os
ENERGY_MATEO_USER=os.getenv("ENERGY_MATEO_USER", default="")
ENERGY_MATEO_PWD=os.getenv("ENERGY_MATEO_PWD", default="")
CONFIG_FILENAME=os.getenv("NA_MARKETS_AESO_CONFIG_FILE", default="config.json")
OPENSSL_CONF=os.getenv("OPENSSL_CONF", default="openssl.cnf")


TOWER_DATA=os.getenv("TOWER_DATA", default="metTowers")
POWER_DATA=os.getenv("POWER_DATA", default="powerData")
TOWER_POSITION=os.getenv("TOWER_POSITION", default="PositionID")
TOWER_UID=os.getenv("TOWER_POSITION", default="MeteorologicalTowerUniqueID")
TOWER_TEMP=os.getenv("TOWER_TEMP", default="AmbientTemperature")
TOWER_PRESSURE=os.getenv("TOWER_PRESSURE", default="BarometricPressure")
TOWER_DEW=os.getenv("TOWER_DEW", default="DewPoint")
TOWER_WIND=os.getenv("TOWER_WIND", default="WindSpeed")
TOWER_DIR=os.getenv("TOWER_DIRECTION", default="WindDirection")
TOWER_HUMID=os.getenv("TOWER_HUMID", default="RelativeHumidity")
TOWER_PRECIP=os.getenv("TOWER_PRECIP", default="Precipitation")
TOWER_ICEUP=os.getenv("TOWER_ICEUP", default="IceUpParameter")
TOWER_FACILITY=os.getenv("TOWER_FACILITY", default="Facility")

POWER_POSITION=os.getenv("POWER_POSITION", default="PositionID")
POWER_REAL_LIMIT=os.getenv("POWER_LIMIT", default="RealPowerLimit")
POWER_NET=os.getenv("POWER_NET", default="NetToGrid")
POWER_GROSS=os.getenv("POWER_GROSS", default="GrossRealPowerCapability")
POWER_FACILITY=os.getenv("POWER_FACILITY", default="Facility")

