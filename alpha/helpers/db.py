import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate(
    'Database.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://alpha-movie-finder-default-rtdb.firebaseio.com/'
})

# Main Ref
ref = db.reference('MovieFinder/')

# Users and Groups
Grps = ref.child('Groups/')
Users = ref.child('Users/')

# All Users And Admins
All = Users.child('All/')
Admins = Users.child('Admins/')

# Data Ref
Data = ref.child('Data/')
Movies = Data.child('Movies/')
Banned = Users.child('Banned')
MGroups = Data.child('AGroups/')
# Funcs
def AddmGroup(Title: str, ID: int):
    data = {ID: Title}
    MGroups.update(data)
    print(f'Added {Title} to Database')

def AddGroup(Title: str, ID: int):
    data = {ID: Title}
    Grps.update(data)
    print(f'Added {Title} to Database')

def AddUser(Username: str, ID: int):
    data = {ID: Username}
    All.update(data)
    print(f'Added User @{Username} to Database')


def AddAdmin(Username: str, ID: int):
    data = {ID: Username}
    Admins.update(data)
    print(f'Promoted User @{Username} As Admin')

def Ban(Reason: str, ID: int, Username: str):
    R = f'{Username}:{Reason}'
    data = {ID: R}
    Banned.update(data)
    print(f'Banned User @{Username}')
# Function to add movies
def AddMvs(Name: str, Details: dict):
    movies_data = Movies.get()
    if movies_data is None:
        movies_data = {}

    if Name in movies_data:
        count = 1
        while f'{Name} {count}' in movies_data:
            count += 1
        new_name = f'{Name} {count}'
        movies_data[new_name] = Details
        Movies.set(movies_data)
        print(f'Added Movie "{new_name}" to Database')
    else:
        movies_data[Name] = Details
        Movies.set(movies_data)
        print(f'Added Movie "{Name}" to Database')

# Usage:

def GetGrps():
    data = Grps.get()
    return data

def GetmGrps():
    data = MGroups.get()
    return data

def GetUsers():
    data = All.get()
    return data


def GetAdmins():
    data = Admins.get()
    return data

def GetMvs():
    data = Movies.get()
    return data

def GetBanned():
    data = Banned.get()
    return data 

def RemAdmin(Id):
    data = Admins.get()
    data.pop(Id, None)
    Admins.set(data)

def Remmgroup(Id):
    data = MGroups.get()
    data.pop(Id, None)
    MGroups.set(data)
    
    
def RemUser(Id):
    data = All.get()
    data.pop(Id, None)
    All.set(data)

def RemMvs(Id):
    data = Movies.get()
    data.pop(Id, None)
    Movies.set(data)
   
def UnBan(Id):
    data = Banned.get()
    data.pop(Id, None)
    Banned.set(data)