import os
from dotenv import load_dotenv
from pathlib import Path 
import peewee

def connect_to_db():
	env_path = Path(__file__).parent.parent.absolute() / '.env'
	load_dotenv(dotenv_path=env_path)

	HOST= os.getenv('DB_HOST')
	USER = os.getenv('DB_USER')
	PASSWORD = os.getenv('DB_PASSWORD')
	DATABASE = os.getenv('DB_NAME')


	database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, passwd=PASSWORD
		)
	return database