from sqlite3 import Cursor
from modulesPackage.connection import myCursor


class Admin:
    def getAllPlaces():
        query = "select * from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllEvents():
        query = "select * from event"
        myCursor.execute(query)
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllArticles():
        query = "select * from article"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllAdvtOffers():
        query = "select * from advert_offer"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllGuides():
        query = "select * from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllResidents():
        query = "select * from resident"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllFeedbacks():
        query = "select * from feedback"
        myCursor.execute(query).fetchall
        result = myCursor.fetchall()
        return result

    def getCount():
        count = {}
        query = "select count(gno) from guide"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['guide'] = result[0][0]

        query = "select count(rno) from resident"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['resident'] = result[0][0]

        query = "select count(pno) from place"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['place'] = result[0][0]

        query = "select count(eno) from event"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['event'] = result[0][0]

        query = "select count(ano) from article"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['article'] = result[0][0]

        query = "select count(oano) from advert_offer"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['offers'] = result[0][0]
        return count
