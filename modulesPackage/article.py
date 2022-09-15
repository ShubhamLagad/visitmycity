from modulesPackage.connection import mydb,myCursor
from math import ceil
import geopy.distance


class Article:
    def __init__(self, username, wname, title, article_content, photo, pdate, alocation):
        query = "insert into article(username,wname,title,article_content,photo,pdate,alocation) values(%s,%s,%s,%s,%s,%s,%s)"
        val = (username, wname, title, article_content, photo, pdate, alocation)
        myCursor.execute(query, val)
        mydb.commit()

    def getAllArticles():
        query = "select * from article"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getOneArticle():
        query = "select * from article where article_content!='' and photo!=''"
        myCursor.execute(query)
        result = myCursor.fetchone()
        return result

    def getResidentsArticles(username):
        query = f"select * from article where username='{username}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def deleteArticle(ano):
        query = f"delete from article where ano={ano}"
        myCursor.execute(query)
        mydb.commit()

    def getDistanceOfLocation(guideLocation, articleLocation):
        # place location
        lat1 = float(articleLocation.split(',')[0])
        lon1 = float(articleLocation.split(',')[1])
        # guide location
        lat2 = float(guideLocation.split(',')[0])
        lon2 = float(guideLocation.split(',')[1])
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        distance = ceil(geopy.distance.geodesic(coords_1, coords_2).km)
        return distance

    def getGuideArticles(guideLocation):
        places = []
        query = f"select * from article"
        myCursor.execute(query)
        result = myCursor.fetchall()
        for res in result:
            if Article.getDistanceOfLocation(guideLocation, res[7]) < 3:
                places.append(res)
        return places
