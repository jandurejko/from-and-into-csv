from geopy.geocoders import Nominatim
import csv
import time

geolocator = Nominatim()
csvFileName = 'fail' #file name into the ' '

with open(csvFileName + '.csv', 'r') as in_file:
    reader = csv.reader(in_file)
    out_file = open(csvFileName + '-out' + '.csv', 'w', newline='')#creates new file with original filename + -out ending
    writer = csv.writer(out_file)
    for row in reader:
        adress1 = row[3]#takes the address
        adress2 = row[5]#takes the area name
        locaiton = geolocator.geocode(adress1 + " " + adress2)#optional prints out into console what its doing
        if locaiton is not None and locaiton.longitude is not None and locaiton.latitude is not None:  #if geopy doesn't get long + lat about an address
            print(adress1 + " " + adress2 + " ", locaiton.latitude, locaiton.longitude)
            row.append(locaiton.latitude)
            row.append(locaiton.longitude)
            writer.writerow(row)
            time.sleep(0.5)#optional so it doesn't overflood. If not many addresses you can remove it
