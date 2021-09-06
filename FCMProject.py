from firebase import firebase
fbconn= firebase.FirebaseApplication(r'https:/chatmessanger-38750.firebaseio.com/')

while True:
    name = input("Enter Your Name")
    email = input("Enter Email")
    
    data_to_upload={
        'Name' : name,
        'Email' : email }
    
    result = fbconn.post('/MyInfo/',data_to_upload)
    print(result)
