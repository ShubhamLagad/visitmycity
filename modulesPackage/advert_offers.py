from modulesPackage.connection import mydb

class OfferAdvert:
    def __init__(self,username,title,heading,content,image,olocation):
        myCursor = mydb.cursor()
        query = "insert into advert_offer(username,title,heading,content,image,olocation)values(?,?,?,?,?,?)"
        val = (username,title,heading,content,image,olocation)
        myCursor.execute(query,val)
        mydb.commit()
        
    def getAllResidentOffers(username):
        mycursor = mydb.cursor()
        query = f"select * from advert_offer where username='{username}'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result