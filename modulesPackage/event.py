from modulesPackage.connection import mydb,myCursor
import datetime
import calendar
from math import ceil
import geopy.distance


class Event:

    def __init__(self, username, ename, venue, edate, etime, poster, organizer, location):
        query = "insert into event (username,ename,venue,edate,etime,poster,organizer,elocation) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        mdate = Event.formatDate(edate)
        val = (username, ename, venue, mdate,
               etime, poster, organizer, location)
        myCursor.execute(query, val)
        mydb.commit()


    def getAllEvents():
        query = "select * from event"
        myCursor.execute(query)
        res = myCursor.fetchall()
        return res

    def formatDate(edate):
        datem = datetime.datetime.strptime(edate, "%Y-%m-%d")
        mon = calendar.month_name[datem.month]
        mdate = str(datem.day)+" "+str(mon)+", "+str(datem.year)
        return mdate

    def getResidentsEvents(username):
        query = f"select * from event where username='{username}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def deleteEvent(eno):
        query = f"delete from event where eno={eno}"
        myCursor.execute(query)
        mydb.commit()

    def getDistanceOfLocation(guideLocation, eventLocation):
        # place location
        lat1 = float(eventLocation.split(',')[0])
        lon1 = float(eventLocation.split(',')[1])
        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance

    def getGuideEvents(guideLocation):
        places = []
        query = f"select * from event"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if Event.getDistanceOfLocation(guideLocation, res[8]) < 3:
                places.append(res)
        return places
