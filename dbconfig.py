import os
import pyrebase
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

config = {
"apiKey": os.environ.get("APIKEY"),
"authDomain": os.environ.get("AUTHDOMAIN"),
"databaseURL": os.environ.get("DATABASEURL"),
"projectId": os.environ.get("PROJECTID"),
"storageBucket": os.environ.get("STORAGEBUCKET"),
"messagingSenderId": os.environ.get("MESSAGINGSENDERID"),
"appId": os.environ.get("APPID"),
"measurementId": os.environ.get("MEASUREMENTID")
}

firebase = pyrebase.initialize_app(config)

# auth = firebase.auth()

# # Log the user in
# user = auth.sign_in_with_email_and_password(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
# print(user)
# Get a reference to the database service
db = firebase.database()