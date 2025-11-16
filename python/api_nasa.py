import requests 
import os 
os.system('clear')
def get_nasa_data(api_key):
    print("COMET INFORMACION")
    url="https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"
    response=requests.get(url)
    response.raise_for_status()
    data=response.json()
    print(data)
API_KEY_NASA='vM6cdiceGBtK9Q2aVo9KLgGkb6AJoKT098FXo2Vr'
get_nasa_data(API_KEY_NASA)    