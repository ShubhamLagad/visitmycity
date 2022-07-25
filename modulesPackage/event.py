from modulesPackage.connection import mydb,myCursor
import datetime
import calendar


class Event:

    def __init__(self,username,ename,venue,edate,etime,poster,organizer,location):
        # myCursor = mydb.cursor()
        query = "insert into event (username,ename,venue,edate,etime,poster,organizer,elocation) values(?,?,?,?,?,?,?,?)"
        
        mdate = Event.formatDate(edate)
        
        val = (username,ename,venue,mdate,etime,poster,organizer,location)
        myCursor.execute(query,val)
        mydb.commit()
        
        print("event inserted")


    def getAllEvents():
        # myCursor = mydb.cursor()
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
        # mycursor = mydb.cursor()
        query = f"select * from event where username='{username}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        return result
    
    # get guide events 
    def getGuideEvents(town):
        # mycursor = mydb.cursor()
        query = f"select * from event where town='{town}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        return result
    