import requests
from requests_kerberos import HTTPKerberosAuth,DISABLED
from xsdata.formats.dataclass.serializers import XmlSerializer

from energymateo.wind_solar_com_layer import WindSolarComLayer
from energymateo.wind_solar_com_layer import WindSolarComLayerType
from energymateo.wind_facility_met_data import WindFacilityMetData
from energymateo.wind_facility_data import WindFacilityDataType
from energymateo.error_alert import ErrorAlert

BASE_URL="https://egpna-pi-web.enelint.global/PIwebapi/elements?path=\\\\egpna-pi-af\\North America Markets\\GRBC-Grizzly Bear Creek\\"
WEBID_URL="https://egpna-pi-web.enelint.global/PIwebapi/"
MET_TOWER_SET_1=f'{BASE_URL}GRBC-Met Tower-Set1&selectedFields=WebId'
MET_TOWER_SET_2=f'{BASE_URL}GRBC-Met Tower-Set2&selectedFields=WebId'
POWER_DATA=f'{BASE_URL}GRBC-PowerData&selectedFields=WebId'
FACILITY_DATA_V136=f'{BASE_URL}GRBC-FacilityData-V136&selectedFields=WebId'
FACILITY_DATA_V150=f'{BASE_URL}GRBC-FacilityData-V150&selectedFields=WebId'

def main():
    print (MET_TOWER_SET_1)
    kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)

    data_set_1=requests.get(url=MET_TOWER_SET_1, auth=kerberos_auth).json()
    GETVALUE_URL=f'{WEBID_URL}streamsets/{data_set_1["WebId"]}/value?selectedFields=Items.Name;Items.Value.Value'
    print(GETVALUE_URL)
    data_met_Tower_set1=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
    print(data_met_Tower_set1)

    n=WindSolarComLayerType.ByDateNpositionNfacility()

    wind_facility_dt=WindFacilityDataType.facility=data_met_Tower_set1['Items'][11]['Value']['Value']
    n.wind_facility_data=wind_facility_dt
    xml_data=WindSolarComLayer([n])
    serializer = XmlSerializer()
   

   
    output = serializer.render(xml_data)
    print(output)



if __name__ == "__main__":
    main()