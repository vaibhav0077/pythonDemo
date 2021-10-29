import pyrebase

firebaseConfig={"apiKey": "AIzaSyBpmqevH_V3htkA-h1fm_y-eohSrJCl-Gw",
  "authDomain": "fir-demo-92725.firebaseapp.com",
  "projectId": "fir-demo-92725",
  "storageBucket": "fir-demo-92725.appspot.com",
  "messagingSenderId": "588334183252",
  "appId": "1:588334183252:web:d2f62acfa6bb8b82758ec1",
  "measurementId": "G-WJBBSP9M9E"
}

firebase=pyrebase.initialize_app(firebaseConfig)  

#db=firebase.database()
auth=firebase.auth()
#storage=firebase.storage()

email=input("Enter ur email: ")
password=input("Enter ur password: ")
auth.sign_in_with_email_and_password(email,password)