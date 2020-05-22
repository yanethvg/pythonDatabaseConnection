import os
from dotenv import load_dotenv
from pathlib import Path 
import peewee
from datetime import datetime

env_path = Path(__file__).parent.parent.absolute() / '.env'
load_dotenv(dotenv_path=env_path)

HOST= os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_NAME')


database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, passwd=PASSWORD)

def createdUser():
	#crea la base de datos con solo ingresar el comando
	if User.table_exists():
		User.drop_table()
	User.create_table()

	#1
	user = User()
	user.username = 'zoila'
	user.password = 'password'
	user.email = 'yaneth94@gmail.com'
	user.save()

	#2
	user = User(username="Erick", password="password", email="erick94@gmail.com")
	user.save()

	#3
	user= {'username': 'cf', 'password': 'password'}
	user = User(**user)
	user.save()

	#4
	#metodo de instancia
	user = User.create(username='dayana', password='password', email='dayana@gmail.com')

	#5
	#retorna un objeto metodo de clase
	query = User.insert(username='melisa', password='password', email='melisa@gmail.com')
	query.execute()

def updatedUser():
	user = User.get( User.id == 1)
	print(user)
	#1 actualizar 
	user.active = False
	user.save()

	#2 actualizar
	query = User.update(active=True).where(User.id == 1)
	query.execute()

def deletedUser():
	#user = User.get( User.id == 1)
	#eliminacion por instancia
	#user.delete_instance()

	query = User.delete().where(User.id == 2)
	query.execute()

def getUser():
	#obtener un registro
	#user = User.get(User.id == 1)
	#print(user)
	#se puede utilizar el metodo select retorna un objeto iterable
	#users = User.select().where(User.id > 3) # select * from users;
	#for user in users: # se veran todos los registros de la tabla
	#	print(user)
	#user = User.select().where(User.id == 1).first() # o usar el metodo get()
	#print(user)
	# se pueden colocar dentro del select los parametros a traer
	#user = User.select(User.username, User.password).where(User.id == 1).first() # o usar el metodo get()
	#print(user.username)
	#print(user.password)
	#and o or
	#user = User.select().where( (User.id == 1) and (User.password == 'password')).first() # o usar el metodo get()
	#print(user)
	#user = User.select().where(User.email >> None ).first() # o usar el metodo get()
	#print(user)
	#para poner not null
	#user = User.select().where( ~User.email >> None ).first() # o usar el metodo get()
	#print(user)
	users = ['zoila', 'dayana']
	# select * from users where username in []
	#users = User.select().where( User.username << users )
	#for user in users: # se veran todos los registros de la tabla
	#	print(user)

	#select * from users where user like '%eduardo%' funcion contains
	#select * from users where user like '%eduardo' funcion startswith
	#select * from users where user like 'eduardo%' funcion endswith
	users = User.select().where( User.username.contains('zoila') )
	for user in users: # se veran todos los registros de la tabla
		print(user)

def sortUser():
	#count= User.select().count()
	#print(count)

	#count= User.select().where(User.id > 2).count()
	#print(count)

	#Uso de metodo limit los primeros dos registros
	#users= User.select().where(User.id > 1).limit(2)
	#for user in users:
	#	print(user)

	#ordenar con metodos +asc() o -desc()
	#users= User.select().where(User.id > 1).order_by(User.username.asc())
	#for user in users:
	#	print(user)

	last = User.select().order_by(User.id.desc()).limit(1).get()
	print(last)

	
class User(peewee.Model):
	username = peewee.CharField(unique=True, max_length=50, index=True)
	password = peewee.CharField(max_length=50)
	email = peewee.CharField(max_length=50, null=True)
	active = peewee.BooleanField(default=True)
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_tables = 'users'

	def __str__(self):
		return self.username

if __name__ == '__main__':
	#createdUser()
	#updatedUser()
	#deletedUser()
	#getUser()
	sortUser()


