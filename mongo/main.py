from pymongo import MongoClient
import re


client = MongoClient() #localhost 27017
db = client['minicurso_python'] #la crea sin necesidad de crearlka


def insert_data():
  user1 = {'username': 'codigofacilito1', 'password': 'password123', 'age' : 23}
  user2 = {'username': 'codigofacilito2', 'password': 'password123', 'age' : 24}
  user3 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 25}
  user4 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 26}

  db.users.insert_many( [user1, user2, user3, user4] )
  """
  Salida
  db.users.find()
  { "_id" : ObjectId("5ecad7ff5b771688a8cc5ecc"), "username" : "codigofacilito1", "password" : "password123", "age" : 23 }
  { "_id" : ObjectId("5ecad7ff5b771688a8cc5ecd"), "username" : "codigofacilito2", "password" : "password123", "age" : 24 }
  { "_id" : ObjectId("5ecad7ff5b771688a8cc5ece"), "username" : "codigofacilito3", "password" : "password123", "age" : 25 }
  { "_id" : ObjectId("5ecad7ff5b771688a8cc5ecf"), "username" : "codigofacilito3", "password" : "password123", "age" : 26 }
  """

  # db.users.insert( user1 )

  #result = db.users.insert_one({'username': 'luffy'})
  #print(result.inserted_id)

def get_data():
  for user in db.users.find():
    print(user)

  db.users.find({'username':'codigofacilito1'})
  db.users.find({'username':'codigofacilito1'}).count()
  db.users.find({'username':'codigofacilito1'}).limit(1)

  user = db.users.find_one()
  user = db.users.find_one({'username' : 'codigofacilito1'})


def updated_delete_data():
  users = db.users.find({"$or":[ {'usernames':'codigofacilito1'}, {'age':23} ]})
  users = db.users.find({"$and":[ {'usernames':'codigofacilito1'}, {'age':23} ]})

  db.users.update({'username': 'codigofacilito1'}, {'$set' : { 'age' : 30}  })
  db.users.update_many({'password': 'password123'}, {'$inc': {'age': 1}})

  db.users.delete_one({'username': 'codigofacilito1'})
  db.users.delete_many({'password': 'password123'})

def regex():
  regex = re.compile('codigo')  # LIKE %codigo%
  regex = re.compile('^codigo')  # LIKE %codigo
  regex = re.compile('codigo$')     # LIKE codigo%
 
  users = db.users.find_one({'username' : regex })
  print(users)

if __name__ == '__main__':
  #insert_data()
  #get_data()
  #updated_delete_data()
  regex()
  
