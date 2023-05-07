import requests
from requests_kerberos import HTTPKerberosAuth,DISABLED
from xsdata.formats.dataclass.serializers import XmlSerializer


from energymateo.wind_solar_com_layer import WindSolarComLayer
from energymateo.wind_solar_com_layer import WindSolarComLayerType
from energymateo.wind_facility_met_data import TimeStampsActivity, TimeStampsSource, WindFacilityMetData, WindFacilityMetDataType
from energymateo.wind_facility_data import WindFacilityData, WindFacilityDataType
from energymateo.power_data import PowerData,PowerDataType
from energymateo.gross_real_power_capability_data import GrossRealPowerCapabilityDataType
from energymateo.error_alert import ErrorAlert

import json
import xml.etree.ElementTree as ET
from dataclasses import asdict
from datetime import datetime

BASE_URL="https://egpna-pi-web.enelint.global/PIwebapi/elements?path=\\\\egpna-pi-af\\North America Markets\\GRBC-Grizzly Bear Creek\\"
WEBID_URL="https://egpna-pi-web.enelint.global/PIwebapi/"
MET_TOWER_SET_1=f'{BASE_URL}GRBC-Met Tower-Set1&selectedFields=WebId'
MET_TOWER_SET_2=f'{BASE_URL}GRBC-Met Tower-Set2&selectedFields=WebId'
POWER_DATA=f'{BASE_URL}GRBC-PowerData&selectedFields=WebId'
FACILITY_DATA_V136=f'{BASE_URL}GRBC-FacilityData-V136&selectedFields=WebId'
FACILITY_DATA_V150=f'{BASE_URL}GRBC-FacilityData-V150&selectedFields=WebId'

class EnergyMeteoETL:
  def __init__(self, config):
    self.facility_name = config['facilityName']
    self.base_url = config['baseURL']
    self.credentials = config['credentials']
    self.power_data = config['powerData']
    self.met_towers = []
    self.etl()
  
  def authenticate(self):
    #PI kerberos authentication
    self.kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)

  def extract(self):
    #Extract raw PI data
    pass
  def transform(self):
    #transform data
    pass
  def load(self):
    #load data
    pass
    
  def etl(self):
    extract();
    
    

def main():
  #  print (MET_TOWER_SET_1)

    #Webapi to get MET1
    data_set_1=requests.get(url=MET_TOWER_SET_1, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_1["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
   # print(GETVALUE_URL)
    data_met_Tower_set1=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
   # print(data_met_Tower_set1)

    #Webapi to get MET2
    data_set_2=requests.get(url=MET_TOWER_SET_2, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_2["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
   # print(GETVALUE_URL)
    data_met_Tower_set2=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
   # print(data_met_Tower_set2)

    #Webapi to get PowerData
    data_set_3=requests.get(url=POWER_DATA, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_3["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
   # print(GETVALUE_URL)
    power_dt=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
   # print(power_dt)

    #Webapi to get V136 TurbineData
    data_set_4=requests.get(url=FACILITY_DATA_V136, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_4["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
   # print(GETVALUE_URL)
    V136_dt=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
   # print(V136_dt)

    #Webapi to get V150 TurbineData
    data_set_5=requests.get(url=FACILITY_DATA_V150, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_5["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
   # print(GETVALUE_URL)
    V150_dt=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
   # print(V150_dt)


    com_layer=WindSolarComLayer()
    com_layer.access_key=""
    
    # create a <ns0:ByDateNPositionNFacility> 
    n=WindSolarComLayerType.ByDateNpositionNfacility()
    com_layer.by_date_nposition_nfacility=n



    # set the facility name
    wind_facility_dt=WindFacilityData.facility=data_met_Tower_set1['Items'][11]['Value']['Value']
    n.wind_facility_data=wind_facility_dt



    wf_met_dt_arr = [] 
    
    tower1 = WindFacilityMetData()
    tower1.met_tower_data=WindFacilityMetDataType.MetTowerData(
        meteorological_tower_unique_id=data_met_Tower_set1['Items'][6]['Value']['Value'],
            ambient_temperature=data_met_Tower_set1["Items"][14]["Value"]["Value"],
            barometric_pressure=data_met_Tower_set1["Items"][13]["Value"]["Value"],
            dew_point=data_met_Tower_set1["Items"][12]["Value"]["Value"],
            wind_speed=data_met_Tower_set1["Items"][0]["Value"]["Value"],
            wind_direction=data_met_Tower_set1["Items"][1]["Value"]["Value"],
            relative_humidity=data_met_Tower_set1["Items"][3]["Value"]["Value"],
            precipitation=data_met_Tower_set1["Items"][4]["Value"]["Value"],
            iceup_parameter=data_met_Tower_set1["Items"][10]["Value"]["Value"]
        )
    wf_met_dt_arr.append(tower1)
    tower2 = WindFacilityMetData()
    tower2.met_tower_data=WindFacilityMetDataType.MetTowerData(
        meteorological_tower_unique_id=data_met_Tower_set2['Items'][6]['Value']['Value'],
            ambient_temperature=data_met_Tower_set2["Items"][14]["Value"]["Value"],
            barometric_pressure=data_met_Tower_set2["Items"][13]["Value"]["Value"],
            dew_point=data_met_Tower_set2["Items"][12]["Value"]["Value"],
            wind_speed=data_met_Tower_set2["Items"][0]["Value"]["Value"],
            wind_direction=data_met_Tower_set2["Items"][1]["Value"]["Value"],
            relative_humidity=data_met_Tower_set2["Items"][3]["Value"]["Value"],
            precipitation=data_met_Tower_set2["Items"][4]["Value"]["Value"],
            iceup_parameter=data_met_Tower_set2["Items"][10]["Value"]["Value"]
    )

    wf_met_dt_arr.append(tower2)


    # set the array of met tower data (not individual towers)
    n.wind_facility_met_data=wf_met_dt_arr
    #com_layer.wind_facility_met_data=wind_facility_met_data
    serializer = XmlSerializer()
    output = serializer.render(com_layer)
    print(output)

    
"""
    #Put MET1 data to WindSolarComSchema
    m1=WindSolarComLayerType.ByDateNpositionNfacility()
    met_tower_dt1=[WindFacilityMetDataType.MetTowerData(meteorological_tower_unique_id=data_met_Tower_set1['Items'][6]['Value']['Value'],
            ambient_temperature=data_met_Tower_set1["Items"][14]["Value"]["Value"],
            barometric_pressure=data_met_Tower_set1["Items"][13]["Value"]["Value"],
            dew_point=data_met_Tower_set1["Items"][12]["Value"]["Value"],
            wind_speed=data_met_Tower_set1["Items"][0]["Value"]["Value"],
            wind_direction=data_met_Tower_set1["Items"][1]["Value"]["Value"],
            relative_humidity=data_met_Tower_set1["Items"][3]["Value"]["Value"],
            precipitation=data_met_Tower_set1["Items"][4]["Value"]["Value"],
            iceup_parameter=data_met_Tower_set1["Items"][10]["Value"]["Value"]
        )]
    
    output = serializer.render(met_tower_dt1)
    print(output)

    # m1.wind_facility_met_data=met_tower_dt1
    # xml_data1=WindFacilityMetData([m1])
    # serializer = XmlSerializer()
    # output1 = serializer.render(xml_data1)
    # print(output1)
    
    #Put MET2 data to WindSolarComSchema
    m2=WindSolarComLayerType.ByDateNpositionNfacility()
    met_tower_dt2=[
        WindFacilityMetDataType.MetTowerData(
            meteorological_tower_unique_id=data_met_Tower_set2['Items'][6]['Value']['Value'],
            ambient_temperature=data_met_Tower_set2["Items"][14]["Value"]["Value"],
            barometric_pressure=data_met_Tower_set2["Items"][13]["Value"]["Value"],
            dew_point=data_met_Tower_set2["Items"][12]["Value"]["Value"],
            wind_speed=data_met_Tower_set2["Items"][0]["Value"]["Value"],
            wind_direction=data_met_Tower_set2["Items"][1]["Value"]["Value"],
            relative_humidity=data_met_Tower_set2["Items"][3]["Value"]["Value"],
            precipitation=data_met_Tower_set2["Items"][4]["Value"]["Value"],
            iceup_parameter=data_met_Tower_set2["Items"][10]["Value"]["Value"]
        )
    ]
    m2.wind_facility_met_data=met_tower_dt2
    xml_data1=WindSolarComLayer([m1,m2])
    serializer = XmlSerializer() 
    # output1 = serializer.render(xml_data1)
    # print(output1)

    #Put Power data,GrossPwrCapacity,MET1,MET2 to WindSolarComSchema
    pwr=WindSolarComLayerType.ByDateNpositionNfacility()
    pwr_dt=[
        PowerDataType(
            real_power_limit=power_dt['Items'][0]['Value']['Value'],
            net_to_grid=power_dt["Items"][1]["Value"]["Value"],
            facility=data_met_Tower_set1['Items'][11]['Value']['Value'],
            position_id=(data_met_Tower_set1["Items"][5]["Value"]["Value"].split()[0]),
            sub_interval=(data_met_Tower_set1["Items"][5]["Value"]["Value"].split()[2]),
            time_stamps=[PowerDataType.TimeStamps(
            time_stamp=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        )
    ],
            ),
    ]

    gross_pwr=WindSolarComLayerType.ByDateNpositionNfacility()
    gross_pwr_dt=[
            GrossRealPowerCapabilityDataType(
            gross_real_power_capability=power_dt['Items'][2]['Value']['Value'],
            facility=data_met_Tower_set1['Items'][11]['Value']['Value'],
            time_stamps=[GrossRealPowerCapabilityDataType.TimeStamps(
            time_stamp=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        )
    ],
        )
    ]

    #Put Power data,GrossPwrCapacity,MET1,MET2 to WindSolarComSchema
    pwr.power_data=pwr_dt
    pwr.wind_facility_met_data=met_tower_dt1
    #pwr.wind_facility_met_data=met_tower_dt2
    pwr.gross_real_power_capability_data=gross_pwr_dt
    xml_data1=WindSolarComLayer([pwr,m2])
    serializer = XmlSerializer() 
    output1 = serializer.render(xml_data1)
    print(output1)



"""
if __name__ == "__main__":
    main()