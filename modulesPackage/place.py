from modulesPackage.connection import mydb

class Place:
    def __init__(self,username,pname,ptype,description,mobileno,photo,plocation):
        myCursor = mydb.cursor()
        query = "insert into place(username,pname,type,description,mobileno,photos,plocation) values(?,?,?,?,?,?,?)"
        val = (username,pname,ptype,description,mobileno,photo,plocation)
        myCursor.execute(query,val)
        mydb.commit()
        print("place insrted")
    
    # for getting all places information 
    def getAllPlaces():
        mycursor = mydb.cursor()
        query = "select * from place"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    # get residents added places information 
    def getResidentsPlaces(username):
        mycursor = mydb.cursor()
        query = f"select * from place where username='{username}'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    def getGuidePlaces(town):
        mycursor = mydb.cursor()
        query = f"select * from place where town='{town}'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    
    
    def getPlacesByType(ptype):
        myCursor = mydb.cursor()
        query = f"select * from place where type='{ptype}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
        