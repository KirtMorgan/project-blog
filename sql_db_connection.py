import pyodbc

##Variables to create a connection##
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'ArticlesDB'
username = 'SA'
password = 'Passw0rd2018'

###Making a connection
docker_Articles_Db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

###Creationg a cursor that can excecute SQL functions on connected database
cursor = docker_Articles_Db.cursor()