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

def existsUser():
	try:
		user = User.get(User.id == 10)
		print(user)
	except User.DoesNotExist as error:
		print("El usuario no existe")
	
	user = User.select().where(User.id == 10).first()
	if user:
		print("El usuario existe")
	else:
		print("El usuario no existe en select")

	count = User.select().where(User.id == 10).count()
	if count:
		print("El usuario existe")
	else:
		print("El usuario no existe en count")

	#usando un metodo exists
	flag = User.select().where(User.id == 10).exists()
	if flag:
		print("El usuario existe")
	else:
		print("El usuario no existe en exists")


def creation_tables():
	if Store.table_exists():
		Store.drop_table()

	if User.table_exists():
		User.drop_table()

	if Product.table_exists():
		Product.drop_table()

	User.create_table()
	Store.create_table()
	Product.create_table()

def relationOneToOne():

	#creando usuario
	user = User.create(username='dayana', password='password', email='dayana@gmail.com')
	#crenado su tienda se puede ocupar user_id = 1
	store = Store.create(name='tienda dayana', address='sin direccion', user=user)

	tienda_facil = Store.get(Store.user_id == 1)
	print(tienda_facil)
	#retorna la relacion con el usuario
	print(tienda_facil.user.username)

def relationOneToMany():
	#creando usuario
	user = User.create(username='zoila', password='password', email='zoila@gmail.com')
	#crenado su tienda se puede ocupar user_id = 1
	store1 = Store.create(name='tienda zoila', address='sin direccion', user=user)
	store2 = Store.create(name='tienda villatoro', address='sin direccion', user=user)

	#viendo la info de la primera tienda
	user = User.get(User.id == 1)
	print(user)

	for store in user.stores:
		print(store)

	store1= Store.get(Store.id == 1)
	print(store1.user)

def insert_users():
	User.create(username='dayana', password='password', email='dayana@gmail.com')
	User.create(username='zoila', password='password', email='zoila@gmail.com')

def insert_stores():
	Store.create(name='tienda zoila', address='sin direccion', user_id=1)
	Store.create(name='tienda villatoro', address='sin direccion', user_id=2)

def insert_products():
	Product.create(store_id=1, name='Pan', description='Pan Integral', price=5.5, stock=2)
	Product.create(store_id=1, name='Leche', description='Baja en grasas', price=15.5, stock=10)
	Product.create(store_id=1, name='Jamon', description='de pavo', price=30.90, stock=6)

	Product.create(store_id=2, name='Soda', description='Dieta', price=1.20, stock=2)
	Product.create(store_id=2, name='Fritura', description='Frituras de papa', price=7.90, stock=20)
	Product.create(store_id=2, name='Salda', description='Chile habanero', price=29.30, stock=4)

def create_schema():
	creation_tables()
	insert_users()
	insert_stores()
	insert_products()


def queryn_1():
	#problema que de una sola sentencia se hacen varias consultas
	user = User.get(User.id == 1)
	for store in user.stores:
		for product in store.products:
			print(product)

def joins_schema():
	# on=(Product.store_id = Store.id)
	query = (
		Product.select()
		.join(Store)
		.join(User)
		.where(User.id == 1)
		.order_by(Product.price.desc())
	)

	for product in query:
		print("*" * 10)
		print(product)

class User(peewee.Model):
	username = peewee.CharField(unique=True, max_length=50, index=True)
	password = peewee.CharField(max_length=50)
	email = peewee.CharField(max_length=50, null=True)
	active = peewee.BooleanField(default=True)
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_table = 'users'

	def __str__(self):
		return self.username

class Store(peewee.Model):
	#user = peewee.ForeignKeyField(User, primary_key=True) #relacion uno a uno
	user = peewee.ForeignKeyField(User,related_name='stores') #relacion uno a muchos
	name = peewee.CharField(max_length=50)
	address = peewee.TextField()
	active = peewee.BooleanField(default=True)
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_table = 'stores'

	def __str__(self):
		return self.name

class Product(peewee.Model):
	name = peewee.CharField(max_length=100)
	description= peewee.TextField()
	store = peewee.ForeignKeyField(Store,related_name='products')
	price = peewee.DecimalField(max_digits=5, decimal_places=2) #100.00
	stock = peewee.IntegerField()
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_table = 'products'

	def __str__(self):
		return '{name} - ${price}'.format(name=self.name,price=self.price)


if __name__ == '__main__':
	#createdUser()
	#updatedUser()
	#deletedUser()
	#getUser()
	#sortUser()
	#existsUser()
	#relationOneToOne()
	#creation_tables()
	#relationOneToMany()
	#create_schema()
	#queryn_1()
	joins_schema()


