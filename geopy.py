# Using geopy, getting co-ordinates of places from addresses

from geopy.geocoders import Nominatim
geolocator = Nominatim()
address=input("Input your home address : ")
location = geolocator.geocode(address)
if location:
    lat=location.latitude
    lon=location.longitude
else:
    lat=None
    lon=None
print(lat,lon)

