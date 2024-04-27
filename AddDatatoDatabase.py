
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURl':'https://agegenderrecognition-e8bfb-default-rtdb.firebaseio.com/'
})


ref=db.reference('Students')


#add data
data={
    "03":
        {
            "Name":"Dewaan Nafiul Islam Noor",
            "Gender": "Male",
            "Age":25,
        },
    "01":
        {
            "Name": "Sazid Hasan Sarker",
            "Gender": "Male",
            "Age": 24,
        },
    "18":
        {
            "Name": "Ahammad Sazid Talukder",
            "Gender": "Male",
            "Age": 30,
        },
    "13":
        {
            "Name": "Mahin Moktadir",
            "Gender": "Male",
            "Age": 26,
        },
    "19":
        {
            "Name": "Kotha Das Puja",
            "Gender": "Female",
            "Age": 24,
        },
    "05":
        {
            "Name": "Mahfuza Islam",
            "Gender": "Female",
            "Age": 27,
        }






}

#send data
for key,value in data.items():
    ref.child(key).set(value)