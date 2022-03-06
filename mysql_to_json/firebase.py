import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Fetch the service account key JSON file contents
cred_obj = credentials.Certificate('midnight-special-video-firebase-adminsdk-2u8hm-3e2b786550.json')

# Initialize the app with a service account, granting admin privileges
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://midnight-special-video.firebaseio.com'
})

ref = db.reference("/video")

with open("video_json.json", "r",encoding='utf-8') as f:
	file_contents = json.load(f)
ref.set(file_contents)

