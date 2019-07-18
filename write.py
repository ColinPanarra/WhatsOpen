import pyrebase
config = {
  "apiKey": "AIzaSyDy5fNFeHg7U_mHnds3YmXT_jjIdAFLs98",
  "authDomain": "whatsopen-6eacf.firebaseapp.com",
  "databaseURL": "https://whatsopen-6eacf.firebaseio.com",
  "storageBucket": "gs://whatsopen-6eacf.appspot.com",
  "projectId": "whatsopen-6eacf",
  #"servceAccount": "C://Users/colin/OneDrive/Desktop/peronal/WhatsOpen/whatsopen-93023321f37f.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("ColinPanarra@gmail.com", "neatoburrito")
#APIkey AIzaSyDy5fNFeHg7U_mHnds3YmXT_jjIdAFLs98
#link https://whatsopen-6eacf.firebaseio.com/
db = firebase.database();

montys = {"name": "montys", "location": "upper campus"}
db.child("stores").child("montys").set(montys, user['idToken'])

openStores = db.child("stores").get(user['idToken']).val();
print(openStores);

#test comment!
