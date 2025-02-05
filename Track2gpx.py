import json
from datetime import datetime

#read VR file
with open("./trackVR.json", mode="r", encoding="utf-8") as read_file:
    track_json = json.load(read_file)

# generate GPX
f = open("./track.gpx","w")
f.write('<?xml version="1.0"?>')
f.write('<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.0" creator="Mon Script">')
f.write('<rte><name>Vendee Globe</name>')


starting_date = 1731240000

for point in track_json['track']:
    # converting timestamp to date
    dt_point = datetime.fromtimestamp(point["ts"]/1000)

    #Calculate number of hours since departure
    time_spent = point["ts"]/1000 - starting_date
    time_spent_hours = int(time_spent / 3600)

    f.write('<rtept lat="'+ str(point["lat"]) + '" lon="' + str(point["lon"]) +'"> <time>'+ (dt_point.strftime('%Y-%m-%dT%H:%M:%S.000Z')) + '</time>,<name>T+'+str(time_spent_hours)+'</name></rtept>')

f.write('</rte></gpx>')
f.close