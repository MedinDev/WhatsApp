from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://missang:pE2@nxzJqJnwnNS@cluster0.mcv7xkj.mongodb.net/?retryWrites=true&w=majority")
db = cluster["VertexBus"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    res = MessagingResponse()
    user = users.find_one({"number": number})
    if bool(user) == False:
        res.message("Hi, thanks for contacting *The Red Velvet*. \nYou can choose from one of the options below:"
"\n\n* Types\n\n 1 To *contact* us \n 2. To sorder* snacks \n Il.To know our *working hours* \n 4 "
"To get our *address*")
        users.insert_one({"number": number, "status": "main", "messages":[]})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res.message("please enter a valid response")
            return str (res)

        if option == 1:
            res.message("")

        users.update_one ({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})
    return str(res)

if __name__ == "__main__":
    app.run(port=5000)