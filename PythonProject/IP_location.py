import requests

def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/').json()
    print(f"City: {response.get('city')}")
    print(f"Region: {response.get('region')}")
    print(f"Map: https://www.google.com/maps/?q={response.get('latitude')},{response.get('longitude')}")

# Example use
get_location("192.168.31.43")