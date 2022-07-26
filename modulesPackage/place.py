from modulesPackage.connection import mydb,myCursor
from math import ceil
import geopy.distance
class Place:
    def __init__(self,username,pname,ptype,description,mobileno,photo,plocation):
        query = "insert into place(username,pname,type,description,mobileno,photos,plocation) values(%s,%s,%s,%s,%s,%s,%s)"
        val = (username,pname,ptype,description,mobileno,photo,plocation)
        myCursor.execute(query,val)
        mydb.commit()
    
    def getAllPlaces():
        query = "select * from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def getResidentsPlaces(username):
        query = f"select * from place where username='{username}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    
    def getPlacesByType(ptype):
        query = "select * from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        placeList = []
        for res in result:
            typeList = res[3].split(',')
            if ptype in typeList:
                placeList.append(res)
        return placeList
    
    
    def deletePlace(pno):
        query = f"delete from place where pno={pno}"
        myCursor.execute(query)
        mydb.commit()
      

    def getDistanceOfLocation(guideLocation, placeLocation):
        # place location
        lat1 = float(placeLocation.split(',')[0])
        lon1 = float(placeLocation.split(',')[1])
        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance
        
    def getGuidePlaces(guideLocation):
        places=[]
        query = f"select * from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if Place.getDistanceOfLocation(guideLocation, res[7])<3:
                places.append(res)
        return places
    
    
    
    def getDistanceOfPlace(currentLocation, placeLocation):
        # current location
        lat1 = currentLocation[0]
        lon1 = currentLocation[1]
        # place location
        lat2 = float(placeLocation.split(',')[0])
        lon2 = float(placeLocation.split(',')[1])
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance
    
    
    def getPlacesByDistance(distance,placeType,currentLocation):
        places=[]
        query = "select * from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            typeList = res[3].split(',')
            if placeType in typeList:
                if Place.getDistanceOfPlace(currentLocation, res[7])<int(distance):
                    places.append(res)
        return places
    