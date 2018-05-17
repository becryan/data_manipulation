import urllib 
import json
import datetime

import pgdb


htmltext = urllib.urlopen("http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json").read()
data=json.loads(htmltext)

#print data

print data["observations"]["data"][0]["apparent_t"]
app_t=data["observations"]["data"][0]["apparent_t"]
curr_t=data["observations"]["data"][0]["air_temp"]
utc=data["observations"]["data"][0]["aifstime_utc"]

#parse the date::
#("%Y%m%d%H%M%S")

new=datetime.datetime.strptime(utc,"%Y%m%d%H%M%S")
 
print new

        

    #for apparent_temp,current_temp,n in cur.fetchall() :
     #   print apparent_temp, current_temp, n

        
        
db = pgdb.connect( host='localhost', user='postgres', password='postgres', database='weather' )


cursor=db.cursor();

try:
    cursor.execute( "insert into weather_time(datetime,apparent_temp,current_temp) values(%s,%s,%s)",(new,app_t,curr_t) )
    db.commit()
except:
    db.rollback()

db.close();









