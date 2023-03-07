#Python project that prompts the user for a location and displays the current time in that location using the Google Maps API and Google Time Zone API.

#Here's an outline of the project:

#Import the necessary modules, including requests and datetime.

#Prompt the user for a location input.

#Use the Google Maps API to retrieve the latitude and longitude coordinates of the location.

#Use the Google Time Zone API to retrieve the time zone information for the location, based on its latitude and longitude.

#Convert the current time in the time zone to the local time and display it to the user.

#coding:
import requests
from datetime import datetime

# Google API key for Maps and Time Zone APIs
api_key = "YOUR_API_KEY_HERE"

# Function to get the latitude and longitude of a location
def get_location_coords(location):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
    response = requests.get(url).json()
    lat = response["results"][0]["geometry"]["location"]["lat"]
    lng = response["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

# Function to get the time zone of a location
def get_location_timezone(location):
    lat, lng = get_location_coords(location)
    url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lng}&timestamp=0&key={api_key}"
    response = requests.get(url).json()
    timezone = response["timeZoneId"]
    return timezone

# Function to get the current time in a location
def get_location_time(location):
    timezone = get_location_timezone(location)
    dt = datetime.utcnow()
    utc_offset = datetime.now().astimezone().utcoffset().total_seconds() / 3600
    local_time = dt + timedelta(seconds=utc_offset)  # Convert UTC time to local time
    location_time = local_time.astimezone(timezone(timezone))
    return location_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

# Main program loop
def main():
    location = input("Please enter a location: ")
    location_time = get_location_time(location)
    print(f"The current time in {location} is {location_time}")

if __name__ == "__main__":
    main()

#This program prompts the user for a location, retrieves the latitude and longitude coordinates using the Google Maps API, and then uses the Google Time Zone API to determine the time zone for that location. 
# It then calculates the current time in that time zone and displays it to the user.

#Note that you will need to replace "YOUR_API_KEY_HERE" with your actual Google API key for the program to work properly.
