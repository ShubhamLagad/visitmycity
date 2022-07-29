from modulesPackage.connection import mydb, myCursor
from math import ceil
import geopy.distance


class OfferAdvert:
    def __init__(self, username, title, content, image, olocation):
        query = "insert into advert_offer(username,title,content,image,olocation)values(?,?,?,?,?)"
        val = (username, title, content, image, olocation)
        myCursor.execute(query, val)
        mydb.commit()

    def getAllResidentOffers(username):
        query = f"select * from advert_offer where username='{username}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def deleteAdvtOffer(oano):
        query = f"delete from advert_offer where oano={oano}"
        myCursor.execute(query)
        mydb.commit()

    def getDistanceOfLocation(guideLocation, offerLocation):
        # resident location
        lat1 = float(offerLocation.split(',')[0])
        lon1 = float(offerLocation.split(',')[1])
        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance

    def getGuideAdvertOffer(guideLocation):
        offers = []
        query = f"select * from advert_offer"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if OfferAdvert.getDistanceOfLocation(guideLocation, res[5]) < 5:
                offers.append(res)
        return offers

    def getAllOffers():
        query = f"select * from advert_offer"
        myCursor.execute(query)
        return myCursor.fetchall()
