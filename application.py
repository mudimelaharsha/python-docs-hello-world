from flask import Flask
import pyodbc 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

    import pyodbc 
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = 'tcp:13.89.121.76' 
    database = 'test' 
    username = 'milindvb' 
    password = 'test123456789###' 
    table = '
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Users')

    for row in cursor:
        print(row)
