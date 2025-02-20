from flask import Flask
from flask import render_template
import psycopg2 as dbapi2



'''
	CREATE DATABASE COMMANDS  FOR REMINDER
	
	persons:
		CREATE TABLE persons (id SERIAL  PRIMARY KEY, name VARCHAR(50));
		INSERT INTO persons(name) VALUES ('Marilyn Boyle');
	
	schedules:
		CREATE TABLE schedules ( personid INTEGER NOT NULL REFERENCES persons(id),  drugname VARCHAR(30) NOT NULL, drugtime VARCHAR(30) NOT NULL, PRIMARY KEY(personid, drugname,drugtime));
		INSERT INTO schedules(personid, drugname, drugtime) VALUES (2,'dicloflam', '05:00-14.11.2019');
'''






# FOR HEROKU
dsn = """user='xqvgwlcwdfbnat' password='1811b22121a205b8765fa78bbcb1d84dc8ec5cb7d74ec656e48c73e0c3cc1cf4'
         host='ec2-54-246-100-246.eu-west-1.compute.amazonaws.com' port=5432 dbname='dfqulnedgiurqk'"""
		 
		 


# connection = dbapi2.connect(dsn)
# try:
    # connection = dbapi2.connect(dsn)
    # cursor = connection.cursor()
    # statement = """\dt
    # )"""
    # cursor.execute(statement)
    # connection.commit()
    # cursor.close()
# except dbapi2.DatabaseError:
    # connection.rollback()
# finally:
    # connection.close()






app = Flask(__name__)



def getPersons():
	rows_total = ""
	with dbapi2.connect(dsn) as connection:
		with connection.cursor() as cursor:
			print('=================')
			statement = """SELECT * FROM persons;"""
			cursor.execute(statement)
			for row in cursor:
				print(row)
				rows_total += (str(row)+"\n")
				# title, score, votes = row
				# print('{}: {} ({} votes)'.format(title, score, votes))

	return rows_total


def getSchedules():
	rows_total = ""
	with dbapi2.connect(dsn) as connection:
		with connection.cursor() as cursor:
			print('=================')
			statement = """SELECT * FROM schedules;"""
			cursor.execute(statement)
			for row in cursor:
				print(row)
				rows_total += (str(row)+"\n")
				# title, score, votes = row
				# print('{}: {} ({} votes)'.format(title, score, votes))

	return rows_total



@app.route("/")
def home_page():

	return render_template("index.html")




@app.route("/persons")
def persons_page():
	
	'''
		GET CONTENT OF THE PERSONS DATABASE
	'''

	# return render_template("index.html")
	x = getPersons()
	# return " ----  ----  ----  ---- Persons Page ----  ----  ----  ---- "
	return x


@app.route("/schedules")
def schedules_page():
	'''
		GET CONTENT OF THE DRUGS DATABASE
	'''
	x = getSchedules()
	
	

	# return " ----  ----  ----  ---- Drug Schedules Page Under Development  ----  ----  ----  ---- "
	return x

if __name__ == "__main__":
    app.run()


















































