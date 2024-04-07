from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


# database settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskdb'

# Mysql object creation 
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form

        # receiving userdata from frontend in variables 
        firstName = details['fname']
        lastName = details['lname']

        # creating cursor class object..it performs SQL operations
        cur = mysql.connection.cursor()
        
        # execute() --> runs SQL query and return result in 'cur' object.
        # make sure you first manually creates database in mysql and create a table in it..!
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        
        # commit() --> stores data permanently in database
        mysql.connection.commit()

        cur.close()
        return 'success'
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)