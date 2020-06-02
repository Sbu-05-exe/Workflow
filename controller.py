import mysql.connector
import string
import random
import os

'''
======================================================================================
								CONNECT TO DATABASE
======================================================================================

'''

db = mysql.connector.connect(
	host='localhost',
	user='root',
	password='root',
	database='workflowdb'
	)

cursor = db.cursor()

'''
======================================================================================
							READING FROM THE DATABASE
======================================================================================
'''
def describe_table(table_name):
	# run the the describe SQL command to read the databse
	cursor.execute(f'DESCRIBE {table_name}')
	return '\n'.join([str(line) for line in cursor])

def show_tables():
	cursor.execute('SHOW TABLES')

	for x in cursor:
		print(x)

def is_Uniqe(table, field, data):
	print(field)
	cursor.execute(f"SELECT * FROM {table} WHERE %s = %s",(field,data))
	# -- cursor.execute("SELECT * FROM (%s) WHERE (%s) = (%s)", (table, field, data))

	for line in cursor:
		if data[0] == cursor:
			return False

	return True
'''
======================================================================================
								STRING HANDLING FUNCTIONS
======================================================================================

'''
def chop_path(path):
	index = 0
	while index >= 0:
		index = path.find('/')
		path = path[(index+1):]

	return path

def chop_url(url):
	alpha = string.ascii_letters

	if 'http' in url :
		index = url.find('/')
		url = url[index+2:]

	if 'www.' in url:
		index = url.find('.')
		url = url[index+1:]

	while not(url[-1] in alpha):
		url = url[:len(url)-1]

	return url

def generate_PK(name):
	name = name.upper()
	index = name.find('.')

	result = name[0]
	vowels = 'A,E,I,O,U'

	if len(name[:index]) <= 3:
		result = name[:index]
	else:
	# exclude the first letter so we don't iterate over it again
		for letter in name[1:]:
			if not(letter in vowels):
				result = result + letter

			if len(result) >= 3:
				break

	integer = str(int(random.random()*100))
	if len(integer) == 1:
		integer = '0' + integer 

	result = result + integer 
	return result


'''
======================================================================================
								WORKSPACE TABLE
======================================================================================

'''
class WorkspaceTable():
	def __str__(self):
		result = []
		for record in self.Tb:
			result.append(str(record))
		return '\n'.join(result)

	def __init__(self):
		self.Tb = None
		self.setTb()
		self.active_workspace = None

	def setTb(self):
		data = self.get_data_from_Tb()
		self.Tb = list(map(lambda x: self.Record(x[0],x[1],x[2]), data))

	def getTb(self):
		return self.Tb

	def get_data_from_Tb(self):
		cursor.execute('SELECT * FROM TbWorkspace')
		return [line for line in cursor]

	def get_active_workspace(self):
		return self.active_workspace

	def describe(self):
		print(describe_table('TbWorkspace'))

	def insert_new_workspace(self, name_of_workspace):
		# Creates new record in workspace table
		cursor.execute('INSERT INTO TbWorkspace (name) VALUES (%s)', (name_of_workspace,))
		db.commit()
		self.setTb()

	def set_active(self, pk, active=True):
		cursor.execute('UPDATE TbWorkspace SET active = (%s) WHERE id = (%s)',(active, pk))
		db.commit()

		for record in self.Tb:
			if record.id == pk:
				record.active = 1
				self.active_workspace = record
				self.setTb()
				return 'SUCCESSFUL'

		return 'FAILED'

	def log_off(self):
		self.active = None
		for record in self.Tb:
			record.active = 0

		cursor.execute('UPDATE TbWorkspace SET active = False WHERE active = True')
		db.commit()

	def del_workspace(self, pk):
		cursor.execute('DELETE FROM TbWorkspace WHERE id = (%s)', (pk,)) 
		db.commit()
		self.setTb()

	class Record():
		def __str__(self):
			return f"{self.id}, {self.name}, {self.active}"

		def __init__(self, pk, name, active=0):
			self.id = pk
			self.name = name
			self.active = active

'''
======================================================================================
								APPSITE TABLE
======================================================================================

'''
class AppSiteTable():
	def __str__(self):
		return '\n'.join([str(record) for record in self.Tb])

	def __init__(self):

		self.Tb = None
		self.setTb()

	def get_data_from_Tb(self):
		cursor.execute('SELECT * FROM TbAppsite')
		return [record for record in cursor]

	def setTb(self):
		data = self.get_data_from_Tb()
		self.Tb = list(map(lambda x: self.Record(x[0], x[1], x[2], x[3]), data))

	def get_apps(self):
		return [record for record in self.Tb if record.type == 'APP']

	def get_webs(self):
		return [record for record in self.Tb if record.type == 'WEB']

	def insert_web(self, url):
		# Check that the record doesn't already exist
		for record in self.Tb:
			
			if (record.path == url) or (record.name == url):
				
				return record


		name = chop_url(url)

		return self.insert_rec(url, name, 'WEB') 

	def insert_app(self, path):
		# Check that the record doesn't already exist
		for record in self.Tb:
			if record.path == path:
				return 'ALREADY IN TABLE'

		name = chop_path(path)

		
		return self.insert_rec(path, name, 'APP')

	def insert_rec(self, path, name, path_type):

		pk = generate_PK(name)

		while not(is_Uniqe('TbAppsite','ID',pk)):
			pk = generate_PK()

		cursor.execute('INSERT INTO TbAppsite (ID, name, urldir, type) VALUES (%s,%s,%s,%s) ', (pk, name, path, path_type))
		db.commit()
		self.setTb()
		return self.Record(pk, name, path, path_type)

	def describe(self):
		print(describe_table('TbAppsite'))

	def del_appsite(self, pk):
		cursor.execute('DELETE FROM Appsite WHERE AppsiteID=(%s)', (pk,))
		db.commit()
		self.setTb()

	class Record():
		def __str__(self):
			return f'{self.id}, {self.name}, {self.path}, {self.type}'

		def __init__(self, pk, name, path, path_type):
			self.AppsiteID = pk
			self.path = path
			self.name = name
			self.type = path_type

'''
======================================================================================
								WORKAPPSITE TABLE
======================================================================================
'''

class WorkAppSiteTable():
	def __str__(self):
		return '\n'.join([str(record) for record in self.Tb])

	def __init__(self):
		self.Tb = None
		self.setTb()

	def get_data_from_Tb(self):
		cursor.execute('SELECT * FROM TbWorkAppSite')
		return [record for record in cursor]

	def get_webs(self, fk):
		cursor.execute('''
			SELECT W.ID, A.ID, name, urldir
			FROM TbAppsite A, TbWorkAppSite W
			WHERE A.ID = AppSiteID AND A.TYPE = 'WEB' AND WorkspaceID = (%s)
			''',(fk,))
		
		return [self.Query(x[0], fk, x[1], x[2], x[3], 'WEB') for x in cursor]

	def get_apps(self, fk):
		cursor.execute('''
			SELECT W.ID, A.ID, name, urldir
			FROM TbAppsite A, TbWorkAppSite W
			WHERE A.ID = AppSiteID AND A.TYPE = 'APP' AND WorkspaceID = (%s)
			''', (fk,))

		return [self.Query(x[0], fk, x[1], x[2], x[3], 'APP') for x in cursor]

	def setTb(self):
		data = self.get_data_from_Tb()
		self.Tb = list(map(lambda x: self.Record(x[0], x[1], x[2]), data))

	def insert_rec(self, wID,aID):
		for record in self.Tb:
			if (record.workspaceID == wID) and (record.AppsiteID == aID) :
				return 'ALREADY IN TABLE'

		cursor.execute('''
			INSERT INTO TbWorkAppsite (workspaceID, AppsiteID) 
			VALUES (%s,%s) 
			''', (wID,aID))
		db.commit()
		self.setTb()
		return 'SUCCESSFUL'

	def describe(self):
		print(describe_table('TbWorkAppSite'))

	def del_record(self, pk):
		print('Primary key', pk)
		cursor.execute('DELETE FROM TbWorkAppSite WHERE ID=(%s)', (str(pk),))
		db.commit()
		self.setTb()

	class Record():
		def __str__(self):
			return f'{self.id}, {self.workspaceID}, {self.AppsiteID}'

		def __init__(self, pk, fkWorkID, fkAppsiteID):
			self.id = pk
			self.workspaceID = fkWorkID
			self.AppsiteID = fkAppsiteID

	class Query(AppSiteTable.Record):
		def __init__(self, pk, WorkspaceID, AppsiteID, name, path, path_type):
			super().__init__(AppsiteID, name, path, path_type)
			self.id = pk
			self.WorkspaceID = WorkspaceID

		def get_record(self):
			# Being demoted to a record. Or being stripped of id and workspaceID qualities
			return AppSiteTable.Record(self.AppsiteID, self.name, self.path, self.type)
'''
======================================================================================
								SANDBOX
======================================================================================
'''

def main():
	pass

if __name__ == "__main__":
	main()
'''
======================================================================================
							GLOBAL VARIABLES
======================================================================================

'''
TbWorkspace = WorkspaceTable()
TbWebApps = AppSiteTable()
TbWorkAppSite = WorkAppSiteTable()

# print(TbWorkAppSite)
# print(TbWorkAppSite.get_apps(5))
# TbWorkspace.describe()
# TbWebApps.describe()

'''
======================================================================================
								DATABASE SCHEMA 
======================================================================================
'''
def setup():
	create_TbWorkspace()
	create_TbAppsite()
	create_TbWorkAppsites()
	db.commit()

def create_TbWorkspace():
	cursor.execute('''CREATE TABLE TbWorkspace (
		WorkspaceID INT(10) AUTO_INCREMENT PRIMARY KEY NOT NULL,
		Name VARCHAR(30), NOT NULL, 
		Active BOOLEAN DEFAULT False) ''')
	db.commit()

def create_TbAppsite():
	cursor.execute('''CREATE TABLE TbAppsite (
		ID VARCHAR(5) PRIMARY KEY NOT NULL,
		Name VARCHAR(30) NOT NULL, 
		Destination VARCHAR(255) NOT NULL
		Type ENUM('WEB', 'APP') NOT NULL
		)
		''')
	db.commit()

def create_TbWorkAppsites():
	cursor.execute('''CREATE Table TbWorkAppSite (
		ID int(5) PRIMARY KEY AUTO_INCREMENT,
		WorkspaceID int(10), FOREIGN KEY (WorkspaceID) REFERENCES TbWorkspace(id),
		AppsiteID varchar(5), FOREIGN KEY (AppSiteID) REFERENCES TbAppsite(id)
		)''')

'''
======================================================================================
						 		DELETE FUNCTIONS
======================================================================================

# Hint! You don't need these changes to be commited for them to saved to the database
# Use the functions at OWN RISK
'''

def DELETE_TABLE(Table):
	cursor.execute(f'DROP TABLE {Table}')