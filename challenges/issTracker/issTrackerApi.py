url = " http://api.open-notify.org/iss-now.json"
import requests
import datetime

def main():
    """reading json from api"""
    # call the api
    resp = requests.get(url).json()
    
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    time_stamp = resp["timestamp"]
    time_stamp = datetime.datetime.fromtimestamp(time_stamp)

    print("CURRENT LOCATION OF THE ISS:")
    print ("Timestamp: " + str(time_stamp))
    print("Lon: " + str(lon))
    print("Lat: " + str(lat))
if __name__ == "__main__":
    main()
