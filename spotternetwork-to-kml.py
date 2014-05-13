# Transform a SpotterNetwork Position History CSV to a KML
# Joe Moore / May 2014 
# Under MIT License - See https://github.com/wxjoe/misc/blob/master/LICENSE
#######################
# How to use: Just run in the same directory as your positions.csv downloaded from SpotterNetwork
# Produces 'sn.kml' in the same directory. 
#######################
def num_true(num):
    if num == 1:
        return 'On'
    else:
        return 'Off'

raw = open('positions.csv','r') # input file
kml = open('sn.kml','w') # output file
report_at, lat, lon, elev, mph, heading, active, gps = [], [], [], [], [], [], [], []
print(str(raw.readline()))
for i in raw:
    line = i.split(',')
    report_at.append(line[0].strip('"'))
    lat.append(float(line[1]))
    lon.append(float(line[2]))
    elev.append(float(line[3]))
    mph.append(str(line[4]))
    heading.append(str(line[5]))
    active.append(num_true(int(line[6])))
    gps.append(num_true(int(line[7])))
    
#### Now time to output the KML! First we need header stuff
kml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
kml.write('  <Document>\n')

for x in range(len(report_at)):
    kml.write('    <Placemark>\n')
    kml.write('      <name>'+str(report_at[x])+'</name>\n')
    kml.write('      <description>Speed: '+str(mph[x])+'mph\n')
    kml.write('        Heading: '+str(heading[x])+' degrees\n')
    kml.write('        Active: '+str(active[x])+'\n')
    kml.write('        GPS: '+str(gps[x])+'</description>\n')
    kml.write('      <Point>\n')
    kml.write('        <coordinates>'+str(lon[x])+','+str(lat[x])+',0</coordinates>\n')
    kml.write('      </Point>\n')
    kml.write('    </Placemark>\n')
    
kml.write('  </Document>')    
kml.write('</kml>')
    
raw.close()
kml.close()
