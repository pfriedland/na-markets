import requests
from requests_kerberos import HTTPKerberosAuth,DISABLED
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
    data_metTower_set1=requests.get(url=GETVALUE_URL, auth=kerberos_auth).json()
    print(data_metTower_set1)

if __name__ == "__main__":
    main()