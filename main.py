import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
import urllib.parse
import backoff
from requests_kerberos import HTTPKerberosAuth,DISABLED
from xsdata.formats.dataclass.serializers import XmlSerializer

from constants import ENERGY_MATEO_USER, ENERGY_MATEO_PWD, CONFIG_FILENAME
from constants import TOWER_DATA, POWER_DATA
from constants import TOWER_UID, TOWER_TEMP,TOWER_PRESSURE
from constants import TOWER_DEW,TOWER_WIND,TOWER_DIR,TOWER_HUMID
from constants import TOWER_PRECIP,TOWER_ICEUP,TOWER_POSITION
from constants import POWER_GROSS, POWER_POSITION
from constants import POWER_NET, POWER_REAL_LIMIT

from energymateo.wind_solar_com_layer import WindSolarComLayer
from energymateo.wind_solar_com_layer import WindSolarComLayerType
from energymateo.wind_facility_met_data import TimeStampsActivity, TimeStampsSource, WindFacilityMetData, WindFacilityMetDataType
from energymateo.wind_facility_data import WindFacilityData, WindFacilityDataType
from energymateo.power_data import PowerData,PowerDataType
from energymateo.gross_real_power_capability_data import GrossRealPowerCapabilityDataType, GrossRealPowerCapabilityDataType
from energymateo.error_alert import ErrorAlert, ErrorAlertType

from energymateo.wind_facility_met_data import (
    TimeStampsActivity,
    TimeStampsSource,
)

from utilities.config_parser import ConfigParser

import json

from dataclasses import asdict
from datetime import datetime

class EnergyMeteoETL:
  # purpose of class is to 
  def __init__(self, config, user=ENERGY_MATEO_USER, pwd=ENERGY_MATEO_PWD):
    self.user = user
    self.pwd = pwd
    self.config = config
    self.af_base_uri = config['AF_BaseUri'] # PI AF base URL
    self.af_database = config['AF_Database']
    self.webIdUrl = config['WebIdUrl']
    self.base_url = f"{self.webIdUrl}{self.af_base_uri}{self.af_database}"
    self.by_date_nposition_nfacility_arr = []
    self.wind_solar_com = WindSolarComLayer()
    self.by_date_nposition_nfacility_arr.append(WindSolarComLayerType.ByDateNpositionNfacility())
    self.by_date_nposition_nfacility_arr.append(WindSolarComLayerType.ByDateNpositionNfacility())
    self.by_date_nposition_nfacility_arr.append(WindSolarComLayerType.ByDateNpositionNfacility())
    self.wind_solar_com.by_date_nposition_nfacility = self.by_date_nposition_nfacility_arr

    self.extract()
  def get_position(self, value) -> list:
    arr = []
    arr = value.split(' ')
    return arr
  
  @backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError,
                       requests.exceptions.RequestException), 
                       max_time=40)
  def get_request(self, request_url) -> dict:
    return requests.get(url=request_url, auth=self.kerberos_auth).json()
  @backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError,
                       requests.exceptions.RequestException), 
                       max_time=20)
  def post_request(self, post_url, data, user=ENERGY_MATEO_PWD, pwd=ENERGY_MATEO_USER) -> dict:
    return requests.post(url=post_url, data=data,
                         auth = HTTPBasicAuth(ENERGY_MATEO_USER, 
                                              ENERGY_MATEO_PWD), verify=False)

    

  def authenticate(self):
    #PI kerberos authentication
    self.kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)

  def extract(self):

    #Extract raw PI data
    self.authenticate()
    # loop through plants as they are defined in the external JSON config file
    extracted_data = {}
    extracted_data["plants"]= []
    for plant in self.config["plants"]:
      plant_data = {}
      extracted_data["plants"].append(plant_data)
      
      facility_name = plant['AF_FacilityName'] # wind / solar plant from config
      plant_data["facilityName"] = facility_name
      plant_data["metTowers"]= []
      # loop through met towers
      for tower in plant["WebIdMeta"]["MetTowers"]: # from config

        #Webapi to get met tower webId
        get_webId_url = f"{self.base_url}\\{facility_name}\\{tower}"
        data_set = self.get_request(get_webId_url)

        # webapi to get met tower data
        get_value_url=f'{self.webIdUrl}/streamsets/{data_set["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
        tower_data = self.get_request(get_value_url)
        #print(get_value_url)
        
        plant_data[TOWER_DATA].append(tower_data)

      #Webapi to get PowerData
      if "PowerData" in plant["WebIdMeta"]:
        get_webId_url = f"{self.base_url}\\{facility_name}\\{plant['WebIdMeta']['PowerData']}"  
        # web api to get power webId
        data_set=self.get_request(get_webId_url)
        get_value_url=f'{self.webIdUrl}/streamsets/{data_set["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
        power_data=self.get_request(get_value_url)
        plant_data[POWER_DATA] = power_data # from AF
        
    self.transform(extracted_data)




  def get_timestamps(self, type, now_8601) -> list:
    # take 8601 UTC string timestamp and return list of type.TimeStamps()
    # assume the PROCESS and SEND are the same time
   
      time_arr=[]
      ts = type.TimeStamps()
      ts.time_stamp = now_8601
      ts.activity = TimeStampsActivity.PROCESS
      ts.source = TimeStampsSource.WIND_FACILITY
      time_arr.append(ts)

      ts = type.TimeStamps()
      ts.time_stamp = now_8601
      ts.activity = TimeStampsActivity.SEND
      ts.source = TimeStampsSource.WIND_FACILITY
      time_arr.append(ts)
      return time_arr

  def convert_array_to_dict(self, data) :
    # helper function to abstract PI WebAPI array position to attributeName
    res_dict = {}
    for value in data:
        res_dict[value["Name"]] = value["Value"]["Value"]
    return res_dict
  
  def transform(self, data={}):
    #transform data; take PI data and turn into XML using xsd-generated Python classes
    for plant in data['plants']: # config
      self.wind_solar_com.by_date_nposition_nfacility[0].access_key=""


      # get the current time

      now_8601 = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
      now_8601_nosep=datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

      # set the facility name, transaction_id

      metFacility = WindFacilityMetData(
            transaction_id=f"{now_8601_nosep}.{plant['facilityName']}.MET",
        facility=plant["facilityName"]
      )
      metFacility.time_stamps = self.get_timestamps(WindFacilityMetData, now_8601)

      
      self.wind_solar_com.by_date_nposition_nfacility[0].wind_facility_met_data = metFacility
      wf_dt_arr = [] 
      position = []
      # loop through the met towers
      for tower in plant[TOWER_DATA]: # from AF data
        
        items = self.convert_array_to_dict(tower["Items"])
        position = self.get_position(items[TOWER_POSITION])
       
        metFacility.position_id = position[0]
        metFacility.sub_interval = position[2]
        
        metFacility.met_tower_data=WindFacilityMetDataType.MetTowerData(
        meteorological_tower_unique_id=items[TOWER_UID],
            ambient_temperature=items[TOWER_TEMP],
            barometric_pressure=items[TOWER_PRESSURE],
            dew_point=items[TOWER_DEW],
            wind_speed=items[TOWER_WIND],
            wind_direction=items[TOWER_DIR],
            relative_humidity=items[TOWER_HUMID],
            precipitation=items[TOWER_PRECIP],
            iceup_parameter=items[TOWER_ICEUP],

        )
        wf_dt_arr.append(metFacility.met_tower_data)
      # set the array of met tower data (not individual towers)
      metFacility.met_tower_data = wf_dt_arr

      # create PowerData object
      
      n1=self.wind_solar_com.by_date_nposition_nfacility[1]    
      n1.power_data = PowerData(
        transaction_id=f"{now_8601_nosep}.{plant['facilityName']}.PWR",
      )

      position = self.get_position(items[POWER_POSITION])
      n1.power_data.facility = plant['facilityName']
      n1.power_data.position_id = position[0]
      n1.power_data.sub_interval = position[2]
      n1.power_data.time_stamps = self.get_timestamps(PowerDataType, now_8601=now_8601)
      items = self.convert_array_to_dict(plant[POWER_DATA]["Items"])
      n1.power_data.net_to_grid = items[POWER_NET]
      n1.power_data.real_power_limit = items[POWER_NET]

      # create Gross power object
      n2=self.wind_solar_com.by_date_nposition_nfacility[2]    
      n2.gross_real_power_capability_data = GrossRealPowerCapabilityDataType(
      )
  
      n2.gross_real_power_capability_data.time_stamps = self.get_timestamps(GrossRealPowerCapabilityDataType, now_8601=now_8601)    
      n2.gross_real_power_capability_data.gross_real_power_capability = items[POWER_GROSS]

      # for each plant, load the results to weather forecast service
      self.load(self.wind_solar_com)

  def load(self, com_layer):
    #transform Python data classes to XML
    serializer = XmlSerializer()
    output = serializer.render(com_layer)
    status = self.post_request(self.config["EnergyMateoUrl"], data=output)
    print (status)
    
    

def main():
  import traceback
  try:
    config = ConfigParser(CONFIG_FILENAME).parse()
    etl = EnergyMeteoETL(config)
  except Exception as e:
     traceback.print_exc()


if __name__ == "__main__":
    main()
