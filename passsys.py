import hashlib
import json
import random
import string

def setup(file):
    global data, database, filename
    filename = file
    database = open(file, 'r')
    try:
        data = json.loads(database.read())
    except:
        data = {}
    database.close()

def createUser(username, password):
    hashpass, salt = hash(password)
    data[username] = [hashpass, salt]

def checkUser(username, password):
    try:
        salt = data[username][1]
    except KeyError:
        return False
    hashpass = data[username][0]
    if hashpass == hashlib.md5((password + salt).encode('utf-8')).hexdigest():
        return True
    else:
        return False

def hash(hashdata):
    salt = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
    return hashlib.md5((hashdata + salt).encode('utf-8')).hexdigest(), salt

def save():
    database = open(filename, 'w')
    database.write(json.dumps(data))
    database.close()
