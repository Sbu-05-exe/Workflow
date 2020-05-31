import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	password='root',
	database='workflowdb'
	)

cursor = db.cursor()

def get_workspaces():

	result=[]
	cursor.execute('SELECT * FROM TbWorkspace')

	for line in cursor:
		workspace = line[1]
		print(workspace)
		result.append(line[1])

	return result

def describe_workspace():
	cursor.execute('DESCRIBE TbWorkspace')

	for line in cursor:
		print(line)

def delete_new_workspace():
	return None

def insert_new_workspace(name_of_workspace):
	cursor.execute('INSERT INTO TbWorkspace (name) VALUES (%s)', (name_of_workspace,))
	db.commit()

def main():
	pass

if __name__ == "__main__":
	main()