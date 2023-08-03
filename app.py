# we installed extentions, called our database inside mongo db, called a few mongo db functions, which connecting and disconnecting from the server, first - we return all the docs , then we find and update using id, give new data in $set. we created a few routes to html pages that render our pages on front end, update route, lets you update from the front end directly. parametres are the local fields that we are creating in the front end like name and age. , we have get and p0ost requests.
from flask import Flask, render_template, request, redirect, url_for #we get the request to be able to determine if we called a get or a post request   #this is our flask page, this is where we send html the dynamic data to be rendered
from pymongo import MongoClient
from bson import ObjectId


global_database_name = "pemdb"
global_collection_name = "users"

app = Flask(__name__)

def find_all_documents():  #these are functions inside mongo db
    # Establish a connection to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    try:
        # Connect to the database (use the global variable)
        database = client[global_database_name]

        # Choose a collection (use the global variable)
        collection = database[global_collection_name]

        # Find and fetch all documents from the collection
        all_documents = list(collection.find({}))

        # Close the connection to the MongoDB server
        client.close()

        return all_documents

    except Exception as e:
        print(f"Error: {e}")
        return None
    
def find_and_update(id, new_data):
    # Establish a connection to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    try:
        # Connect to the database (use the global variable)
        database = client[global_database_name]

        # Choose a collection (use the global variable)
        collection = database[global_collection_name]

        # Find and fetch all documents from the collection
        collection.update_one({"_id": id}, {"$set": new_data})

        # Close the connection to the MongoDB server
        client.close()

        return 

    except Exception as e:
        print(f"Error: {e}")
        return None




@app.route("/", methods=["POST", "GET"])    #this is the main route since this has ("/") #this is where we create the http post and get requests, 
def home ():
    allData = find_all_documents()
    print(allData)
    return render_template("hello.html", data = allData) #render template is a flask method, here we rendering the hello.html page 
     


#this is the page that sends the request when someone types something into the search bar, it will send that info to the server using a post request 
@app.route("/home", methods=["GET", "POST"])  #this is the /home route, when search for this url it will use this route.
def second_app ():
    print("GET METHOD")
    return render_template("home.html")

@app.route("/house", methods=["GET", "POST"])
def third_app ():
    print("GET METHOD")
    data = find_all_documents()
    print("Data",data)
    return render_template("hello.html", data = data)

@app.route("/new", methods =["GET", "POST"])
def fourth_app ():
    print("GET METHOD")
    data = find_all_documents()
    print("This is our data",data)
    return render_template("New.html", data = data )

@app.route("/update", methods =["GET", "POST"])
def fifth_app ():
    print("POST METHOD")
    id_str = request.args.get("id")
    print(id_str)
    obj_id = ObjectId(id_str)
    parage = request.args.get("age")
    parname = request.args.get("name")  #this is only in a get request, whenever you have params in the url, you can access them using this request.args.get 
    age = {'age':parage, 'name' : parname} # local fields that we are creating 
    find_and_update(obj_id,age) # we are updating the age from the front end 
    data = find_all_documents()
    print("updared data", data )
    return render_template("New.html",data = data ) # this data = data is what sends the data to the html template to be rendered 

if __name__ == '__main__':
    app.run(debug=True)