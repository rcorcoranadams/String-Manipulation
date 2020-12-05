# Rachel Corcoran-Adams
# September 25, 2020
# This code extracts the latitude and longitude from the URL: https://www.google.com/maps/@42.2509428,-71.8249939,17z
# The output is a text that reads:
  # Latitude: 42.2509428
  # Longitude: -71.8249939

# This line imports the library re
import re
# This line shows the url that the information will be taken from 
url = 'https://www.google.com/maps/@42.2509428,-71.8249939,17z'
# This line imports the string using tuple packing 
latitude, longitude = re.search(r'@(.*?),(.*?),', url).groups()

# This lines print the outputs to mimic the desired one
print("Latitude: "+ latitude)
print("Longitude: "+ longitude)
