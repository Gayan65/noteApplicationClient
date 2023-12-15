import sys
import gc
import os
import time
import datetime
from getpass import getpass

#USER CLASS 
class User:
        def __init__(self, name, password):
            self.name = name
            self.password = password
            self.notes = []

        def __str__(self):
            return f"{self.name}({self.password})"    
        #Adding notes
        def add_note(self, note):
            self.notes.append(note)

# NOTES CLASS
class Note:
        def __init__(self, id, subject, note, user, date):
            self.id = id
            self.subject = subject
            self.note = note
            self.user = user
            self.date = date
        
        def __str__(self):
            return f"{self.id}{self.subject}{self.note}{self.user}{self.date}"
        

note_instances = []
userAuth = False

#PASSING USER INPUT TO INT 
def try_parse(input, base = None):
    try:
        return int(input, base) if base else int(input)
    except Exception:
        return 0

#CHECKING USER INPUT HAVING BLANK OR NONE 
def string_blank_input(input):
    if(input == "" or input.isspace()):
        return True
    else:
        return False
    
#MAIN MENU FUNCTION
def main_menu(auth, user):
    start = True
    while start:
        if(auth):
            os.system('clear')
            print("WELCOME TO THE NOTE APP")
            time.sleep(0.5)
            print("User Account : " + user.name)
            print("")
            time.sleep(0.5)
            print("__MAIN MENU__")
            print("")
            print("1. Create a note ")
            print("2. Retrieve a note")
            print("3. Logout")
            print("")
            userChoice = input("Make your choice : ")
            
            #Parsing user input between 1 - 3 options
            while try_parse(userChoice) > 3 or try_parse(userChoice) < 1:
                #print(try_parse(userChoice))
                print("invalid Input !, ")
                userChoice = input("Make your choice : ")
            userChoice = int(userChoice)

            #Checking user choice 1
            if(userChoice == 1):
                os.system('clear')
                print("__CREATE NOTES MENU__")
                print("")
                continueFrame = True
                while continueFrame:
                    #Checking existing instance/ objects in Note class and add id according to that
                    id = 1
                    for obj in gc.get_objects():
                        if isinstance(obj, Note):
                            id += 1

                    userSubject = input("Add the Subject : ")

                    #Handling Can not leave the subject blank
                    while try_parse(string_blank_input(userSubject)): #THERE IS A ISSUE
                        print("Subject cannot leave blank,")
                        userSubject = input("Add the Subject : ")
                    time.sleep(0.25)
                    userNote = input("Add the note : ")
                    #Handling Can not leave the note body blank
                    while try_parse(string_blank_input(userNote)):
                        print("Note body cannot leave blank,")
                        userNote = input("Add the note : ")
                    time.sleep(0.25)
                    userDate = datetime.datetime.now()
                    
                    #Creating new note object and adding to the list under note_instances
                    noteObj = Note(id, userSubject, userNote, user, userDate)
                    note_instances.append(noteObj)
                    user.add_note(noteObj)
                    choice = input("You want to continue (Y/N) : ")
                    choice = choice.upper()
                    if(choice == "Y"):
                        continueFrame = True
                        os.system('clear')
                    else:
                        continueFrame = False
                        os.system('clear')
            #Checking user choice 2
            elif(userChoice == 2):
                os.system('clear')
                print("__RETRIEVE NOTES MENU__")
                print("")
                #Printing all notes
                print("%-10s %-25s %15s %15s" % ("ID", "SUBJECT", "USER", "DATE"))
                for instance in note_instances:
                    print("%-10s %-25s %15s %15s" % (instance.id, instance.subject, instance.user.name, instance.date.strftime("%x")))
                    time.sleep(0.5)
                print("")
                print("You have a Search option")
                print("1. Search by ID")
                print("2. Search by keyword")
                print("3. Main Menu")
                userSearchChoice = input("Your Choice : ")
                #Parsing user input between 1 - 3 options
                while try_parse(userSearchChoice) > 3 or try_parse(userSearchChoice) < 1:
                    print("invalid Input")
                    userSearchChoice = input("Make your choice : ")
                userSearchChoice = int(userSearchChoice)

                #Searching Notes by it's ID from note_instances list
                if(userSearchChoice == 1):
                    userSerachedID = input("Type note id : ")
                    #Checking user input is a numeric value
                    while try_parse(not userSerachedID.isnumeric()):
                        print("invalid input!,")
                        userSerachedID = input("Type note id : ")
                    os.system('clear')
                    print("__FULL NOTE VIEW__")
                    print("")
                    userSerachedID = int(userSerachedID)
                    for instance in note_instances:
                        if(userSerachedID == instance.id):
                                print(" ID              : ",(instance.id))
                                print(" SUBJECT         : ",(instance.subject))
                                print(" BODY            : ",(instance.note))
                                print(" USER            : ",(instance.user.name))
                                print(" DATE            : ",(instance.date.strftime("%x")))
                                print("")
                                choice = input("Continue (Y/N) : ")
                                choice = choice.upper()
                                if(choice == "Y"):
                                    if(user.name == instance.user.name):
                                        userDeleteChoice = input("Do you want to delete this (Y/N) : ")
                                        userDeleteChoice = userDeleteChoice.upper()
                                        if(userDeleteChoice == "Y"):
                                            #Deleting note 
                                            note_instances.remove(instance)
                                            os.system('clear')
                                            print("Please wait ....")
                                            time.sleep(0.5)
                                            print("Note successfully deleted ! ")
                                            time.sleep(2)
                                            os.system('clear')
                                            continue
                                        else:
                                            os.system('clear')
                                            continue
                                else:
                                    os.system('clear')
                #Searching Notes by it's substring from note_instances list
                elif(userSearchChoice == 2):
                    userSearchedString = input("Type your key word : ")
                    userSearchedString = userSearchedString.upper()
                    os.system('clear')
                    for instance in note_instances:
                        if(userSearchedString in instance.subject.upper() or userSearchedString in instance.note.upper()):
                            print("%-10s %-25s %15s %15s" % ("ID", "SUBJECT", "USER", "DATE"))
                            print("%-10s %-25s %15s %15s" % (instance.id, instance.subject, instance.user.name, instance.date.strftime("%x")))
                            time.sleep(0.5)
                            choice = input("continue (Y/N) : ")
                            choice = choice.upper()
                            if(choice == "Y"):
                                os.system('clear')
                                continue
                            else:
                                os.system('clear')
                                break
                #Back to the previous loop
                elif(userSearchChoice == 3):
                    continue
            else:
                return main

#MAIN FUNCTION
def main() -> int:
    while True:
        os.system('clear')
        userName = input("Username : ")
        password = getpass("Password : ")

#USERNAME AND PASSWORD HARDCODED
        u1 = User("user1", "pass1")
        u2 = User("user2", "pass2")
        users = [u1, u2]

#CHECK USER LOGIN
        userID = 0
        for user in users:
            if(userName == user.name and password == user.password):
                userAuth = True
                os.system('clear')
                break
            else:
                userAuth = False
            userID += 1
        if(userAuth):
             main_menu(userAuth, user)
        else:
             print("Invalid user credentials, Try again...")
             time.sleep(1)
             continue

#RUNNING THE MAIN FUNCTION
if __name__ == '__main__':
    sys.exit(main())