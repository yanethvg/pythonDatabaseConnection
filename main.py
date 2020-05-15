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


USER_TABLE= """ CREATE TABLE users(
				id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
				username VARCHAR(50) NOT NULL,
				password VARCHAR(50) NOT NULL
			)"""

DROP_USER = "DROP TABLE IF EXISTS `users`"
SHOW_TABLES = "SHOW TABLES"
if __name__ == '__main__':
	try:
		connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE )

		cursor = connection.cursor()
		#eliminando tabla
		cursor.execute(DROP_USER)
		#creando tabla
		cursor.execute(USER_TABLE)
		#mostrando tabla
		cursor.execute(SHOW_TABLES)
		tables = cursor.fetchall()

		for table in tables:
			#print(table)
			print(table[0])


		# ESTAS CONECCIONES DEBEN CERRARSE
		connection.close()
	except MySQLdb.Error as error:
		print(error)
