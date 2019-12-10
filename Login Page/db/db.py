import mysql.connector

# Make a connection to the server and database
con = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="",
    database="python app"
)

cursor = con.cursor()

# Make a function to access the db
def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `email`=%s AND `password`=%s", tup)

        return (cursor.fetchone())
    except:
        return False

def user_register(tup):
    try:
        cursor.execute("INSERT INTO `admin` (`name`, `email`, `password`) VALUES (%s, %s, %s)", tup)
        con.commit()
        return cursor.rowcount
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

