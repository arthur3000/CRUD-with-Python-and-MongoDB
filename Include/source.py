from pymongo import MongoClient
import pprint
import json
from bson import json_util

client = MongoClient('mongodb://localhost:27017')
db = client.appUsers
users = db.users

def mainMenu():
    print("WELCOME TO THE FANTASTIC GENERIC APP")
    print("1. Create user" + "\n" +
          "2. Read all users" + "\n" +
          "3. Update a user" + "\n" +
          "4. Delete a user" + "\n" +
          "0. Exit" + "\n")
    print("Please select an option: ", end="")
    return int(input())


def addUser():
    print("**ADD A USER**")
    print("Please enter the name of the JSON file: ", end="")
    fileName = str(input())
    try:
        sourceFile = open(fileName, "r")
        json_data = json.load(sourceFile)
        users.insert_one(json_data)
    except FileNotFoundError:
        print("Sorry, the file is not here")


def printAllUsers():
    print("**SHOW ALL USERS BY NAME**")
    sortedUsers = users.find().sort('firstName', 1)
    for user in sortedUsers:
        pprint.pprint(user)


def modifyUser():
    print("**FIND AND MODIFY A USER**")
    print("Please enter the username of the user you wish to change: ", end="")
    username = str(input())
    print("Please enter the user's new information ")
    print("First name:", end="")
    firstName = str(input())
    print("Last name:", end="")
    lastName = str(input())
    result = users.find_one_and_update(
        {'username': username},
        {'$set': {'firstName': firstName, 'lastName': lastName}})
    if result != None:
        print("User modified successfully")
    else:
        print("We couldn't update the user! ):")


def deleteUser():
    print("**FIND AND DELETE A USER**")
    print("Please enter the username of the user you wish to delete: ", end="")
    username = str(input())
    result = users.delete_one({'username': username})
    if result != None:
        print("User deleted successfully")
    else:
        print("We couldn't find the user! I guess your work is done")


if __name__ == '__main__':
    keepGoing = True
    while keepGoing:
        option = mainMenu()
        if option == 1:
            addUser()
            continue
        if option == 2:
            printAllUsers()
            continue
        if option == 3:
            modifyUser()
            continue
        if option == 4:
            deleteUser()
            continue
        if option == 0:
            keepGoing = False
            continue
    print("Press enter to exit...")
    input()