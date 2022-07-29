import json
import os
from flask import Flask, redirect, render_template, request, session
from modulesPackage import guide, resident, event, place, article,advert_offers,admin
import geocoder
from datetime import date


app = Flask(__name__)
app.secret_key = 'super_secret_key'

app.config['PLACE_UPLOAD_FOLDER'] = 'static/images/places'
app.config['EVENT_UPLOAD_FOLDER'] = 'static/images/events'
app.config['ARTICLE_UPLOAD_FOLDER'] = 'static/images/articles'
app.config['GUIDE_UPLOAD_FOLDER'] = 'static/images/guide'
app.config['OFFER_UPLOAD_FOLDER'] = 'static/images/offers'
with open('./placeTypes.json') as fp:
    placeTypes = json.load(fp)["placeTypes"]


def currentLocation():
    # manual location 
    # latlng = [18.465171, 73.833144]
    # return latlng

    # automatic location 
    g = geocoder.ip('me')
    return g.latlng


events = event.Event.getAllEvents()
localGuide = guide.Guide.getLocalGuide(currentLocation())
allOffersAdverts = advert_offers.OfferAdvert.getAllOffers()

@app.route('/')
def home():
    events = event.Event.getAllEvents()
    localGuide = guide.Guide.getLocalGuide(currentLocation())
    page = "residents/dashboard"
    return render_template("index.html", events=events, page=page,localGuide=localGuide,allOffersAdverts=allOffersAdverts)



# =============Resident registartion=================
@app.route('/addResident', methods=['POST', 'GET'])
def addResident():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('regEmail')
        mobile = request.form.get('mobile')
        password = request.form.get('regCPassword')
        rlocation = request.form.get('latitude')+","+request.form.get('longitude')
        
        status = resident.Resident.checkAlreadyExistsResident(email)
        if status:
            return render_template("index.html", accountExistsStatus=True, events=events,localGuide=localGuide)
        else:
            resident.Resident(name, email, mobile, password,rlocation)
            return render_template("index.html", registerSuccessStatus=True, events=events,localGuide=localGuide)


def checkValidUser():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('loginpassword')
        validStatus = resident.Resident.checkValidResident(email, password)
        if validStatus:
            session['username'] = email
            session['name'] = resident.Resident.getName(session['username'])[0][0]
            return True
        else:
            return False


@app.route("/addPlace", methods=['POST', 'GET'])
def addPlace():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            pname = request.form.get('pname')
            ptype = request.form.get('ptype')
            description = request.form.get('description')
            mobileno = request.form.get('mobileno')
            plocation = request.form.get('latitude')+","+request.form.get('longitude')

            # file uploading
            f = request.files['file']
            photo = f.filename
            if photo == "":
                photo="defaultplace.jpg"
            else:
                f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    app.config['PLACE_UPLOAD_FOLDER'], f.filename))
            place.Place(username, pname, ptype, description,
                        mobileno, photo, plocation)
            return redirect('/residents/dashboard')

        return render_template("residents/addPlace.html", events=events, placeTypes=placeTypes,localGuide=localGuide,username=session['name'])

    return render_template('index.html', page="addPlace", login=True, events=events,localGuide=localGuide)


@app.route("/addEvent", methods=['POST', 'GET'])
def addEvent():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            ename = request.form.get('ename')
            venue = request.form.get('venue')
            edate = request.form.get('edate')
            etime = request.form.get('etime')
            organizer = request.form.get('organizer')
            elocation = request.form.get('latitude')+","+request.form.get('longitude')

            # file uploading
            f = request.files['file']
            poster = f.filename
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                   app.config['EVENT_UPLOAD_FOLDER'], f.filename))

            event.Event(username, ename, venue, edate, etime,
                        poster, organizer, elocation)
            global events
            events = event.Event.getAllEvents()
            return redirect('/residents/dashboard')

        return render_template("residents/addEvent.html", events=events,localGuide=localGuide,username=session['name'])

    return render_template('index.html', page="addPlace", login=True, events=events,localGuide=localGuide)


@app.route("/addArticle", methods=['POST', 'GET'])
def addArticle():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            atitle = request.form.get('title')
            article_content = request.form.get('article_content')
            alocation = str(currentLocation()[0])+","+str(currentLocation()[1])
            # current date
            today = date.today()
            publishdate = today.strftime("%d %B, %Y")
            # file uploading
            f = request.files['file']
            photo = f.filename
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                   app.config['ARTICLE_UPLOAD_FOLDER'], f.filename))

            article.Article(username, atitle, article_content,
                            photo, publishdate, alocation)
            return redirect('/residents/dashboard')

        return render_template("residents/addArticle.html",events=events,localGuide=localGuide,username=session['name'])
    return render_template('index.html', page="addPlace", login=True, events=events,localGuide=localGuide)


@app.route('/addOffer',methods=['POST','GET'])
def addOffer():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            title = request.form.get('title')
            cnt = request.form.get('cnt')
            content=""
            for i in range(1,int(cnt)):
                contentName = "content"+str(i)
                content+=request.form.get(contentName)+","
                
            olocation = request.form.get('latitude')+","+request.form.get('longitude')

            # file uploading
            f = request.files['file']
            photo = f.filename
            if photo == "":
                photo="offerdefault.jpg"
            else:
                f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    app.config['OFFER_UPLOAD_FOLDER'], f.filename))

            advert_offers.OfferAdvert(username,title,content,photo,olocation)
            allOffersAdverts = advert_offers.OfferAdvert.getAllOffers()
            return redirect('/residents/dashboard')

        return render_template("residents/addAdvertOffer.html",events=events,localGuide=localGuide,username=session['name'])
    return render_template('index.html', page="addAdvertOffer", login=True, events=events,localGuide=localGuide)

@app.route('/addAdvertisement',methods=['POST','GET'])
def addAdvertisement():
    if 'username' in session:
        if request.method == 'POST':
            username = session['username']
            title = ""
            content=""
            latlng = currentLocation()
            olocation = str(latlng[0])+","+str(latlng[1])

            # file uploading
            f = request.files['file']
            photo = f.filename
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                   app.config['OFFER_UPLOAD_FOLDER'], f.filename))

            advert_offers.OfferAdvert(username,title,content,photo,olocation)
            return redirect('/residents/dashboard')

        return render_template("residents/addAdvertOffer.html",events=events,localGuide=localGuide,username=session['name'])
    return render_template('index.html', page="addAdvertOffer", login=True, events=events,localGuide=localGuide)


@app.route('/residents/dashboard', methods=['POST', 'GET'])
def residentsDashboard():
    if 'username' in session:
        username = session['username']
        residentDetails = resident.Resident.getResident(username)
        count = resident.Resident.getCount(username)
        return render_template("residents/dashboard.html", events=events, residentDetails=residentDetails,localGuide=localGuide,username=session['name'],count=count)
    elif checkValidUser():
            username = session['username']
            residentDetails = resident.Resident.getResident(username)
            count = resident.Resident.getCount(username)
            return render_template("residents/dashboard.html", events=events, residentDetails=residentDetails,localGuide=localGuide,username=session['name'],count=count)
    else:
        return render_template("index.html", loginStatus=True, events=events,localGuide=localGuide)



@app.route('/residents/places')
def residentsPlaces():
    if 'username' in session:
        username = session['username']
        allPlaces = place.Place.getResidentsPlaces(username)
        return render_template('residents/places.html', allPlaces=allPlaces, events=events,localGuide=localGuide,username=session['name'])
    return redirect('/')


@app.route('/residents/events')
def residentsEvents():
    if 'username' in session:
        username = session['username']
        allEvents = event.Event.getResidentsEvents(username)
        return render_template('residents/events.html', allEvents=allEvents, events=events,localGuide=localGuide,username=session['name'])
    return redirect('/')


@app.route('/residents/articles')
def residentsArticles():
    if 'username' in session:
        username = session['username']
        allArticles = article.Article.getResidentsArticles(username)
        return render_template('residents/articles.html', allArticles=allArticles, events=events,localGuide=localGuide,username=session['name'])
    return redirect('/')

@app.route('/residents/advertOffers')
def advertOffers():
    username = session['username']
    allOffers = advert_offers.OfferAdvert.getAllResidentOffers(username)
    return render_template('residents/advertOffers.html',allOffers=allOffers, events=events,localGuide=localGuide,username=session['name'])

@app.route('/updateResident',methods=['POST','GET'])
def updateResident():
    if request.method == 'POST':
        name  = request.form.get('rname')
        email  = request.form.get('remail')
        mobile  = request.form.get('rmobile')
        password  = request.form.get('rpassword')
        rlocation  = request.form.get('latitude')+","+request.form.get('longitude')
        resident.Resident.updateResident(name,email,mobile,password,rlocation)
        return redirect('residents/dashboard')
        


@app.route("/findNearby")
def findNearby():

    return render_template("findNearby.html", placeTypes=placeTypes,events=events,localGuide=localGuide)


@app.route("/places/<string:placeType>")
def findPlace(placeType):
    places = place.Place.getPlacesByType(placeType)
    return render_template("place.html", places=places, events=events,localGuide=localGuide)


@app.route('/feedback', methods=['POST', 'GET'])
def feddback():
    if request.method == 'POST':
        username = request.form.get('feedbackName')
        email = request.form.get('feedbackEmail')
        comment = request.form.get('feedbackComment')
        resident.Feedback(username, email, comment)
    return render_template('index.html',localfeedback=True, events=events,localGuide=localGuide)


# ============Guide routes=========
# ======Guide registartion=========
@app.route('/addGuide', methods=['POST', 'GET'])
def addGuide():
    if request.method == 'POST':
        email = request.form.get('gEmail')
        gname = request.form.get('gname')
        gmobile = request.form.get('gmobile')
        gpassword = request.form.get('gCPassword')
        newGuidelocation = str(request.form.get('glatitude'))+","+str(request.form.get('glongitude'))
        if guide.Guide.checkAlreadyExistsGuide(email,newGuidelocation):
            return render_template("index.html",events=events,localGuide=localGuide,guideAccountExistsStatus=True)
        else:
            f = request.files['photo']
            photo = f.filename
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    app.config['GUIDE_UPLOAD_FOLDER'], f.filename))
            guide.Guide(email, gpassword, gmobile, gname,newGuidelocation, photo)
            localGuide = guide.Guide.getLocalGuide(currentLocation())
            return render_template("index.html",events=events,localGuide=localGuide,registerSuccessStatus=True)


@app.route('/guide/dashboard', methods=['POST', 'GET'])
def guideDashboard():
    if request.method == 'POST':
        username = request.form.get('guideUsername')
        password = request.form.get('guidePassword')

        if guide.Guide.checkValidGuide(username, password):
            session['guideusername'] = username
            guideDetails = guide.Guide.getGuide(username)
            return render_template('guide/dashboard.html', guideDetails=guideDetails)
        else:
            return render_template("index.html", loginStatus=True, events=events,localGuide=localGuide)
            
    else:
        if 'guideusername' in session:
            guideDetails = guide.Guide.getGuide(session['guideusername'])
            return render_template('guide/dashboard.html', guideDetails=guideDetails)
            
    return redirect('/')


@app.route('/guide/residents')
def viewResidents():
    if 'guideusername' in session:
        guideLocation = guide.Guide.getLocation(session['guideusername'])[0][0]
        allResidents = resident.Resident.getGuideResident(guideLocation)
        return render_template('guide/residents.html', allResidents=allResidents)
    else:
        return redirect('/')


@app.route('/guide/places')
def viewPlaces():
    if 'guideusername' in session:
        guideLocation = guide.Guide.getLocation(session['guideusername'])[0][0]
        allPlaces = place.Place.getGuidePlaces(guideLocation)
        return render_template('guide/places.html', allPlaces=allPlaces)
    else:
        return redirect('/')


@app.route('/guide/events')
def viewEvents():
    if 'guideusername' in session:
        guideLocation = guide.Guide.getLocation(session['guideusername'])[0][0]
        allEvents = event.Event.getGuideEvents(guideLocation)
        return render_template('guide/events.html', allEvents=allEvents)
    else:
        return redirect('/')


@app.route('/guide/articles')
def viewArticles():
    if 'guideusername' in session:
        guideLocation = guide.Guide.getLocation(session['guideusername'])[0][0]
        allArticles = article.Article.getGuideArticles(guideLocation)
        return render_template('guide/articles.html', allArticles=allArticles)
    else:
        return redirect('/')


    
@app.route('/guide/advtOffer')
def viewAdvtOffer():
    if 'guideusername' in session:
        guideLocation = guide.Guide.getLocation(session['guideusername'])[0][0]
        allAdvtOffer = advert_offers.OfferAdvert.getGuideAdvertOffer(guideLocation)
        return render_template('guide/advtOffer.html', allAdvtOffer=allAdvtOffer)
    else:
        return redirect('/') 
    



@app.route('/admin/dashboard',methods=['POST','GET'])
def adminDashboard():
    if request.method == 'POST':
        username = request.form.get('adminUsername')
        password = request.form.get('adminPassword')
        if username=='admin@gmail.com' and password=='admin@123':
            session['adminusername'] = username
            count = admin.Admin.getCount()
            return render_template('admin/dashboard.html',count=count)
        
    if 'adminusername' in session:
        count = admin.Admin.getCount()
        return render_template('admin/dashboard.html',count=count)
    else:
        return redirect('/')



@app.route('/admin/articles')
def allArticles():
    if 'adminusername' in session:
        allArticles = admin.Admin.getAllArticles()
        return render_template('admin/articles.html', allArticles=allArticles)
    else:
        return redirect('/') 
    
    
    
@app.route('/admin/places')
def allPlaces():
    if 'adminusername' in session:
        allPlaces = admin.Admin.getAllPlaces()
        return render_template('admin/places.html', allPlaces=allPlaces)
    else:
        return redirect('/') 
    
    
@app.route('/admin/events')
def allEvents():
    if 'adminusername' in session:
        allEvents = admin.Admin.getAllEvents()
        return render_template('admin/events.html', allEvents=allEvents)
    else:
        return redirect('/') 
    
    
@app.route('/admin/advtOffer')
def allAdvtOffer():
    if 'adminusername' in session:
        allAdvtOffer = admin.Admin.getAllAdvtOffers()
        return render_template('admin/advtOffer.html', allAdvtOffer=allAdvtOffer)
    else:
        return redirect('/') 
    
    
@app.route('/admin/feedbacks')
def allFeedbacks():
    if 'adminusername' in session:
        allFeedbacks = admin.Admin.getAllFeedbacks()
        return render_template('admin/feedbacks.html', allFeedbacks=allFeedbacks)
    else:
        return redirect('/') 
    
    
@app.route('/admin/residents')
def allResidents():
    if 'adminusername' in session:
        allResidents = admin.Admin.getAllResidents()
        return render_template('admin/residents.html', allResidents=allResidents)
    else:
        return redirect('/') 
    
    
@app.route('/admin/guides')
def allGuides():
    if 'adminusername' in session:
        allGuides = admin.Admin.getAllGuides()
        return render_template('admin/guides.html', allGuides=allGuides)
    else:
        return redirect('/') 
    

@app.route('/delete/resident/<string:email>',methods=['GET'])
def deleteResident(email):
    if 'adminusername' in session:
        resident.Resident.deleteResident(email)
    return redirect('/admin/residents')

@app.route('/delete/guide/<string:email>',methods=['GET'])
def deleteGuide(email):
    if 'adminusername' in session:
        guide.Guide.deleteGuide(email)
    return redirect('/admin/guides')

@app.route('/delete/article/<string:ano>',methods=['GET'])
def deleteArticle(ano):
    if 'adminusername' in session:
        article.Article.deleteArticle(ano)
    return redirect('/admin/articles')

@app.route('/delete/event/<string:eno>',methods=['GET'])
def deleteEvent(eno):
    if 'adminusername' in session:
        event.Event.deleteEvent(eno)
    return redirect('/admin/events')

@app.route('/delete/place/<string:pno>',methods=['GET'])
def deletePlace(pno):
    if 'adminusername' in session:
        place.Place.deletePlace(pno)
    return redirect('/admin/places')

@app.route('/delete/advtoffer/<string:oano>',methods=['GET'])
def deleteOffers(oano):
    if 'adminusername' in session:
        advert_offers.OfferAdvert.deleteAdvtOffer(oano)
    return redirect('/admin/advtOffer')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
