from flask import session
from modulesPackage.connection import mydb,myCursor


class Resident:

    def __init__(self, name, email, mobile, password, rlocation):
        # myCursor = mydb.cursor()
        query = "insert into resident(name,email,mobile,password,rlocation)values(?,?,?,?,?)"
        val = (name, email, mobile, password, rlocation)
        myCursor.execute(query, val)
        mydb.commit()
        
        print("resident inserted.")

    def checkAlreadyExistsResident(email):
        query = f"select * from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        if result == []:
            return False
        else:
            return True

    def checkValidResident(email, password):
        # myCursor = mydb.cursor()
        query = f"select * from resident where email='{email}' and password='{password}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        if result == []:
            return False
        else:
            return True
        

    def getResident(email):
        # myCursor = mydb.cursor()
        query = f"select * from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        return result

    def getAllResident():
        # myCursor = mydb.cursor()
        query = "select * from resident"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        return result
    
    
    def updateResident(	name,email,mobile,password,rlocation):
        oemail = session['username']
        # myCursor = mydb.cursor()
        query = f"update resident set name='{name}',email='{email}',mobile='{mobile}',password='{password}',rlocation='{rlocation}' where email='{oemail}'"
        myCursor.execute(query)
        session['username'] = email
        session['name'] = name
        mydb.commit()
        
        
    def getCount(email):
        count = {}
        # myCursor = mydb.cursor()
        query = f"select count(pno) from place where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['place']=result[0][0]
        
        
        query = f"select count(eno) from event where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['event']=result[0][0]
        
        
        query = f"select count(ano) from article where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['article']=result[0][0]
        
        
        query = f"select count(oano) from advert_offer where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['offers']=result[0][0]
        
        return count
    
    def getName(email):
        # myCursor = mydb.cursor()
        query = f"select name from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        
        return result

class Feedback:
    def __init__(self, username, email, comment):
        # myCursor = mydb.cursor()
        query = "insert into feedback(username,email,comment) values(?,?,?)"
        val = (username, email, comment)
        myCursor.execute(query, val)
        mydb.commit()
        
        print("feedback insert")
