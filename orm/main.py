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
	deletedUser()


