import os
from dotenv import load_dotenv
from pathlib import Path 
import pymysql as MySQLdb 

env_path = Path(__file__).parent.absolute() / '.env'

load_dotenv(dotenv_path=env_path)

HOST= os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_NAME')


if __name__ == '__main__':
	try:
		connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE )

		cursor = connection.cursor()

		# ESTAS CONECCIONES DEBEN CERRARSE
		connection.close()
	except MySQLdb.Error as error:
		print(error)
