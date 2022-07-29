from flask import session
from modulesPackage.connection import mydb,myCursor
import geopy.distance
from math import ceil


class Guide:

    def __init__(self, email, password, gmobile, gname, glocation, photo):
        query = 'insert into guide(email,password,mobile,gname,glocation,photo) values(?,?,?,?,?,?)'
        val = (email, password, gmobile, gname, glocation, photo)
        myCursor.execute(query, val)
        mydb.commit()
        
    def updateGuide(email, password, mobile, gname, photo):
        query = f"update guide set email='{email}',password='{password}',mobile='{mobile}',gname='{gname}',photo='{photo}'"
        session['guideusername'] = email
        myCursor = mydb.cursor()
        myCursor.execute(query)
        mydb.commit()

    def getDistanceOfLocation(guideLocation, currentLocation):
        # manual current location
        lat1 = currentLocation[0]
        lon1 = currentLocation[1]

        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])

        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance
    
    
    def getNewGuideDistanceOfLocation(guideLocation, newGuideLocation):
        # new guide location
        lat1 = float(newGuideLocation.split(',')[0])
        lon1 = float(newGuideLocation.split(',')[1])
        # old guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])

        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance


    def checkAlreadyExistsGuide(email,newGuideLocation):
        query = f"select glocation,email from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if res[1]==email:
                return True
            elif Guide.getNewGuideDistanceOfLocation(res[0],newGuideLocation)<4:
                return True
        else:
            return False

    def checkValidGuide(email, password):
        query = f"select * from guide where email='{email}' and password='{password}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True


    def getAllGuides():
        query = "select * from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getGuide(email):
        query = f"select * from guide where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getLocalGuide(latlng):
        query = "select * from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if Guide.getDistanceOfLocation(res[5], latlng) < 3:
                return res
        return None
    
    
    def deleteGuide(email):
        query = f"delete from guide where email='{email}'"
        myCursor.execute(query)
        mydb.commit()
        
        
    def getLocation(email):
        query = f"select glocation from guide where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
