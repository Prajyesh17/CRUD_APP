from pymongo import MongoClient

# Global variables
global_database_name = "pemdb"
global_collection_name = "users" #these are constant, just refering to the database

def insert_document(document):      #create application, insert document is a function, 
    # Establish a connection to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")    

    try:
        # Connect to the database (use the global variable)
        database = client[global_database_name]

        # Choose a collection (use the global variable)
        collection = database[global_collection_name]

        # Insert the document into the collection
        inserted_document = collection.insert_one(document) #insert_one ? its the name of the attribute we call 

        # Close the connection to the MongoDB server
        client.close()

        return inserted_document.inserted_id  #we get the id of the inserted document 

    except Exception as e:
        print(f"Error: {e}")    #incase error occurs, this will show us why 
        return None

def delete_document(id):   # creatiing a function to delete a document
    # Establish a connection to the MongoDB server, realize that we cut the connection and reestablish after every step
    client = MongoClient("mongodb://localhost:27017/")

    try:    # we are creating the try method so that we can find an error if there is one 
        # Connect to the database (use the global variable)
        database = client[global_database_name]

        # Choose a collection (use the global variable)
        collection = database[global_collection_name]

        # Delete the document from the collection based on the filter query
        deleted_document = collection.delete_one({"_id": id}) #shouldn't we put the inserted id here ? delete one is one of the attributes we call 

        # Close the connection to the MongoDB server
        client.close()

        return deleted_document.deleted_count #returns a count of the number of deleted documents, so if the count is 0, we know that nothing got delted so there is an error in the deletion. 

    except Exception as e:
        print(f"Error: {e}")
        return 0

def find_document(id): #we find the document based on the id 
    # Establish a connection to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")

    try:
        # Connect to the database (use the global variable)
        database = client[global_database_name]

        # Choose a collection (use the global variable)
        collection = database[global_collection_name]

        # Find and fetch the document from the collection based on the filter query
        found_document = collection.find_one({"_id": id}) # same as delete, find one is an attribute of a function, we find using an ID 

        # Close the connection to the MongoDB server
        client.close()

        return found_document

    except Exception as e:
        print(f"Error: {e}")
        return None

params = ["name", "age", "gender", "height"] #? zero clue about this as well. 
document = {} #? no idea what this is 

for param in params:  # find out what this param is. 
    document[param] = input(f"Please enter {param} -> ")

id_returned_after_insertion = insert_document(document)

print("id_returned_after_insertion -> ", id_returned_after_insertion)
print("-------------------------------")
input("Click enter to find the document")

print("Finding the document")
found_document = find_document(id_returned_after_insertion)
print("Found the document ->", found_document)
print("-------------------------------")
input("Click enter to delete the document")

print("Deleting the document")
download_count = delete_document(id_returned_after_insertion)
print("Deleted document ->", download_count)