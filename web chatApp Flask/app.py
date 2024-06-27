############################ COMPLETED THE BEGINNER TASK AND TRIED ADVANCE TASK BUT NOT FULLY COMPLETED#########################################

from flask import Flask,render_template
from flask_socketio import SocketIO,send
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET'] = "add yours"
Socketio = SocketIO(app , cors_allowed_orgins = "*")

client = MongoClient('mongodb://localhost:27017/')
mydb = client['chats']
collection = mydb["chat_messages"]

@Socketio.on('message')

def handle_message(message):
    print("Message received" + message)
    if message != "User connected!":

         # Insert message into MongoDB
        collection.insert_one({"message" :  message})
        send(message ,broadcast=True)



@app.route('/')

def index():
    old_chats = collection.find({})

    for chat in old_chats:
        print(chat)
    return render_template('index.html',old_chats=old_chats)


if __name__ == '__main__':
    
    Socketio.run(app , host= "localhost",debug=True)
