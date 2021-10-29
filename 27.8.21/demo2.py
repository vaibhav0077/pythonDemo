import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBO98ocIy6MeUYiHkiweqpdnYx-HRwbpbo",
  'authDomain': "demo1-aa391.firebaseapp.com",
  'projectId': "demo1-aa391",
  'storageBucket': "demo1-aa391.appspot.com",
  'messagingSenderId': "166422767471",
  'appId': "1:166422767471:web:b9eba338fa13fabc642a9a",
  'measurementId': "G-EHFDGE8Q7Y"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()
auth = firebase.auth()
# storage = firebase.storage()

email = input("Enter Your Email : ")
password = input("Enter Your Password : ")

auth.sign_in_with_email_and_password(email, password)


