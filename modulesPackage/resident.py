from flask import session
from modulesPackage.connection import mydb, myCursor


class Resident:

    def __init__(self, name, email, mobile, password, rlocation):
        query = "insert into resident(name,email,mobile,password,rlocation)values(?,?,?,?,?)"
        val = (name, email, mobile, password, rlocation)
        myCursor.execute(query, val)
        mydb.commit()

    def checkAlreadyExistsResident(email):
        query = f"select * from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True

    def checkValidResident(email, password):
        query = f"select * from resident where email='{email}' and password='{password}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True

    def getResident(email):
        query = f"select * from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def getAllResident():
        query = "select * from resident"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def updateResident(name, email, mobile, password, rlocation):
        oemail = session['username']
        query = f"update resident set name='{name}',email='{email}',mobile='{mobile}',password='{password}',rlocation='{rlocation}' where email='{oemail}'"
        myCursor.execute(query)
        session['username'] = email
        session['name'] = name
        mydb.commit()

    def getCount(email):
        count = {}
        query = f"select count(pno) from place where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['place'] = result[0][0]

        query = f"select count(eno) from event where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['event'] = result[0][0]

        query = f"select count(ano) from article where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['article'] = result[0][0]

        query = f"select count(oano) from advert_offer where username='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        count['offers'] = result[0][0]

        return count

    def getName(email):
        query = f"select name from resident where email='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result


    def deleteResident(email):
        query = f"delete from resident where email='{email}'"
        myCursor.execute(query)
        return myCursor.execute(query)

class Feedback:
    def __init__(self, username, email, comment):
        query = "insert into feedback(username,email,comment) values(?,?,?)"
        val = (username, email, comment)
        myCursor.execute(query, val)
        mydb.commit()
        print("feedback insert")
