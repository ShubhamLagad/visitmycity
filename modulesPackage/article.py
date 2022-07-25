from modulesPackage.connection import mydb

class Article:
    def __init__(self,username,	writername,article_content,photo,pdate,rating,pincode):
        myCursor = mydb.cursor()
        query = "insert into article(username,writername,article_content,photo,pdate,rating,pincode) values(?,?,?,?,?,?,?)"
        val = (username,writername,article_content,photo,pdate,rating,pincode)
        myCursor.execute(query,val)
        mydb.commit()
        print("article insrted")
        
    
    def getAllArticles():
        mycursor = mydb.cursor()
        query = "select * from article"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    def getResidentsArticles(username):
        mycursor = mydb.cursor()
        query = f"select * from article where username='{username}'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    
    def getGuideArticles(pincode):
        mycursor = mydb.cursor()
        query = f"select * from article where pincode={pincode}"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result