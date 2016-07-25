from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import csv
import time

geolocator = Nominatim()
csvFileName = input("insert the file name you want to scan(whiteout the csv extension)")
separator = input("are the rows sepparated by , or ;?")

with open(csvFileName + '.csv', 'r') as in_file:
    reader = csv.reader(in_file, delimiter= separator, quotechar=' ')
    out_file = open(csvFileName + '-out.csv', 'w', newline='')#creates new file with original filename + -out ending
    broken_address = open(csvFileName + '-unknown.csv', 'w', newline='')
    writer = csv.writer(out_file)
    broken = csv.writer(broken_address)
    for row in reader:
        mch_code = row[0]
        adress1 = row[3]#takes the address
        adress2 = row[5]#takes the area name
        try:
            locaiton = geolocator.geocode(adress1 + " " + adress2, timeout=10) #optional prints out into console what its doing
        except TimeoutError:
            locaiton = geolocator.geocode(adress1 + " " + adress2, timeout=10)
        if locaiton is not None and locaiton.longitude is not None and locaiton.latitude is not None:  #if geopy doesn't get long + lat about an address
            print(adress1 + " " + adress2 + " ", locaiton.latitude, locaiton.longitude)
            row.append(locaiton.latitude)
            row.append(locaiton.longitude)
            writer.writerow(row)
            time.sleep(1)	#optional so it doesn't overflood. If not many addresses you can remove it
        elif locaiton is None:
            broken.writerow(row)
            time.sleep(1)
