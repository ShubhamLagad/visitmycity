from modulesPackage.connection import mydb,myCursor
import geopy.distance
from math import ceil


class Guide:

    def __init__(self, email, password, gmobile, gname, glocation, photo):
        # myCursor = mydb.cursor()
        query = 'insert into guide(email,password,mobile,gname,glocation,photo) values(?,?,?,?,?,?)'
        val = (email, password, gmobile, gname, glocation, photo)
        myCursor.execute(query, val)
       
        mydb.commit()

    def getDistanceOfLocation(guideLocation, latlng):

        # manual current location
        lat1 = latlng[0]
        lon1 = latlng[1]

        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])

        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        # print("distance is : ", distance)
        return distance

    def checkAlreadyExistsGuide(email,glocation):
        # mycursor = mydb.cursor()
        query = f"select glocation,email from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
       
        for res in result:
            if res[1]==email:
                return True
            elif Guide.getDistanceOfLocation(res[0],glocation)<4:
                return True
            else:
                return False

    def checkValidGuide(email, password):
        # mycursor = mydb.cursor()
        query = f"select * from guide where email='{email}' and password='{password}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
       
        if result == []:
            return False
        else:
            return True

    def getAllGuides():
        # mycursor = mydb.cursor()
        query = "select * from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
       
        return result

    def getGuide(email):
        # mycursor = mydb.cursor()
        query = f"select * from guide where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
       
        return result

    def getLocalGuide(latlng):
        # mycursor = mydb.cursor()
        query = "select * from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if Guide.getDistanceOfLocation(res[5], latlng) < 3:
                return res
        return None
