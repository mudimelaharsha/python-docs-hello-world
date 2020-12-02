from flask import Flask
import pyodbc 
app = Flask(__name__)

@app.route("/")
def hello():
     
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = 'tcp:mibelhewinvm.centralus.cloudapp.azure.com' 
    database = 'test' 
    username = 'milindvb' 
    password = 'test123456789###' 

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    cursor.execute('SELECT * FROM dbo.Users')

    for row in cursor:
        print(row)
    return "hello"
