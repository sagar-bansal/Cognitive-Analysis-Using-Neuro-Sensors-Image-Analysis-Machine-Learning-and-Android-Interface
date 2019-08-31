
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("hci-emotion-recognizer-firebase-adminsdk-pv65c-fa76b7ec23.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://hci-emotion-recognizer.firebaseio.com'
})

ref = db.reference('emotions')

print(ref.get())
users_ref = ref.child('users')
users_ref.set({
    
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing',
    
    'gracehop': 'dsds',
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'

})
