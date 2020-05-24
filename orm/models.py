import peewee
from datetime import datetime
from connection import connect_to_db

database = connect_to_db()

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
	user = peewee.ForeignKeyField(User,related_name='stores', null = True) #relacion uno a muchos
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
	store = peewee.ForeignKeyField(Store,related_name='products', null = True)
	price = peewee.DecimalField(max_digits=5, decimal_places=2) #100.00
	stock = peewee.IntegerField()
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_table = 'products'

	def __str__(self):
		return '{name} - ${price}'.format(name=self.name,price=self.price)


class Category(peewee.Model):
	name = peewee.CharField(max_length=100)
	description= peewee.TextField()
	active = peewee.BooleanField(default=True)
	created_date = peewee.DateTimeField(default=datetime.now)

	class Meta:
		database = database
		db_table = 'categories'

	def __str__(self):
		return self.name

class CategoriesProduct(peewee.Model):
	product = peewee.ForeignKeyField(Product, related_name='categories', null = True)
	category = peewee.ForeignKeyField(Category,related_name='products', null = True)

	class Meta:
		database = database
		db_table = 'categories_products'

	def __str__(self):
		return "{} - {}".format(self.product, self.category)